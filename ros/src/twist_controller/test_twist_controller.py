import pytest
import twist_controller

class TwistTester(object):
    def __init__(self):
        self.controller = twist_controller.Controller()
        self.vehicle_mass = 1736.35
        # fuel_capacity = 13.5
        # brake_deadband = 0.1
        # decel_limit = -5
        # accel_limit = 1.0
        # wheel_radius = 0.24123
        # wheel_base = 2.8498
        # steer_ratio = 14.8
        # max_lat_accel = 3.0
        # max_steer_angle = 8.0

@pytest.fixture(scope="module")
def twist_tester():
    return TwistTester()

def test_vehicle_at_rest_stays_at_rest(twist_tester):
    current_velocity = 0.0
    target_linear_velocity = 0.0
    target_angular_velocity = 0.0
    
    throttle, brake, steering = twist_tester.controller.control(
        current_velocity=current_velocity,
        linear_velocity=target_linear_velocity,
        angular_velocity=target_angular_velocity,
        dbw_enabled=True
    )
    
    assert throttle == 0.0
    assert brake == 700 # Required to stop idling vehicle
    assert steering == 0.0

def test_vehicle_in_motion_stays_in_motion(twist_tester):
    current_velocity = 20.0
    target_linear_velocity = 20.0
    target_angular_velocity = 0.0

    throttle, brake, steering = twist_tester.controller.control(
        current_velocity=current_velocity,
        linear_velocity=target_linear_velocity,
        angular_velocity=target_angular_velocity,
        dbw_enabled=True
    )
    assert throttle > 0.0 and throttle <= 1.0
    assert brake == 0.0
    assert steering == 0.0

def test_returns_zero_when_dbw_disabled(twist_tester):
    throttle, brake, steering = twist_tester.controller.control(
        current_velocity = 123.0,
        linear_velocity = -456.0,
        angular_velocity = 789.0,
        dbw_enabled=False
    )
    assert throttle == 0.0
    assert brake == 0.0
    assert steering == 0.0