import time
from sensors.temperature import read_temperature
from sensors.humidity import read_humidity
from sensors.air_pressure import read_air_pressure
from sensors.light import read_light_levels
from sensors.motion import read_motion
from utils import log_to_csv


for _ in range(5):
    data_dict = {
    "temperature": read_temperature(),
    "humidity": read_humidity(),
    "air pressure": read_air_pressure(),
    "light": read_light_levels(),
    "motion":read_motion()
}
    log_to_csv("sensor_data.csv", data_dict)
    print(f"Logged temperature: {data_dict['temperature']}°C")
    print(f"Humidity percentage: {data_dict['humidity']}%")
    print(f"Current Air Pressure: {data_dict['air pressure']} hPa")
    print(f"Light Levels: {data_dict['light']} lux")
    print(f"Is the object in motion? – {data_dict['motion']}")
    time.sleep(1)