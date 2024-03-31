from datetime import datetime 
import psutil

battery = psutil.sensors_battery()
percent = int(battery.percent)

while True:
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S") 
    battery_2 = psutil.sensors_battery()
    percent_2 = int(battery_2.percent)
    if percent_2 != percent:
        print(f"Заряд батареи сменился: {percent_2}% в {current_time}")
        battery = psutil.sensors_battery()
        percent = int(battery.percent)
