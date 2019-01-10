import pytest
import twist_controller

def test_vehicle_at_rest_stays_at_rest():
    controller = twist_controller.Controller()
    throttle, brake, steering = controller.control()
    assert throttle == 1.0
    assert brake == 0.0
    assert steering == 0.0