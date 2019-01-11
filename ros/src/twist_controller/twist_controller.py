
GAS_DENSITY = 2.858
ONE_MPH = 0.44704

import rospy
from pid import PID
from yaw_controller import YawController
from lowpass import LowPassFilter

class Controller(object):
    def __init__(self, vehicle_mass, brake_deadband, decel_limit, accel_limit, 
        wheel_radius, wheel_base, steer_ratio, max_lat_accel, max_steer_angle):
        
        self.vehicle_mass = vehicle_mass
        self.brake_deadband = brake_deadband
        self.decel_limit = decel_limit
        self.accel_limit = accel_limit
        self.wheel_radius = wheel_radius
        self.wheel_base = wheel_base
        self.steer_ratio = steer_ratio
        self.max_lat_accel = max_lat_accel
        self.max_steer_angle = max_steer_angle
        min_speed = 0.1
        self.yaw_controller = YawController(self.wheel_base, self.steer_ratio,
                                            min_speed, self.max_lat_accel, 
                                            self.max_steer_angle)

        kp = 0.3
        ki = 0.1
        kd = 0.0
        min_throttle = 0.0
        max_throttle = 0.2
        self.throttle_controller = PID(kp, ki, kd, min_throttle, max_throttle)

        tau = 0.5 # rc time constant
        sample_time = 0.02 #s
        self.v_lpf = LowPassFilter(tau, sample_time)
        self.last_time = rospy.get_time()
    



    def control(self, v_x, target_v_x, target_w_z, dbw_enabled):
        # Return throttle, brake, steer
        throttle = 0.0
        brake = 0.0
        steer = 0.0
        if not dbw_enabled:
            return throttle, brake, steer
        v_x = self.v_lpf.filt(v_x)
        steer = self.yaw_controller.get_steering(target_v_x, target_w_z, v_x)
        
        v_x_error = target_v_x - v_x
        
        current_time = rospy.get_time()
        sample_time = current_time - self.last_time
        self.last_time = current_time

        throttle = self.throttle_controller.step(v_x_error, sample_time)
        brake = 0.0

        if v_x == 0:
            throttle = 0.0
            brake = 700.0 # N*m
        elif throttle < 0.1 and v_x_error < 0.0:
            throttle = 0.0
            decel = max(v_x_error, self.decel_limit)
            brake = abs(decel)*self.vehicle_mass*self.wheel_radius

        return throttle, brake, steer
