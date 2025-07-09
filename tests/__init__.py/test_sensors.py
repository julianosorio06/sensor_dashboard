import pytest
from sensors.temperature import read_temperature
from sensors.humidity import read_humidity
from sensors.air_pressure import read_air_pressure
from sensors.light import read_light_levels
from sensors.motion import read_motion

def test_read_temperature():
    assert isinstance(result, float)
    result = read_temperature()
    assert 23.0 <= result <= 27.0

def test_read_humidity():
    assert isinstance(result, float)
    result = read_humidity()
    assert 30.0 <= result <= 60.0

def test_read_air_pressure():
    assert isinstance(result, float)
    result = read_air_pressure()
    assert 990 <= result <= 1030

def test_read_light_levels():
    assert isinstance(result, float)
    result = read_light_levels()
    assert 100 <= result <= 1000

def test_read_motion():
    result = read_motion()
    assert result in [True, False]