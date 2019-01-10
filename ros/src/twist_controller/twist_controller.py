
GAS_DENSITY = 2.858
ONE_MPH = 0.44704


class Controller(object):
    def __init__(self, *args, **kwargs):
        # TODO: Implement
        pass

    def control(self, current_velocity, linear_velocity, angular_velocity,
                dbw_enabled):
        # Return throttle, brake, steer
        throttle = 0.0
        brake = 0.0
        steer = 0.0
        if not dbw_enabled:
            return throttle, brake, steer
        
        if current_velocity == 0:
            throttle = 0.0
            brake = 700.0
        else:
            throttle = 1.0
            brake = 0.0

        return throttle, brake, steer
