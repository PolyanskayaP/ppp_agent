import psutil
battery = psutil.sensors_battery()
percent = int(battery.percent)
while True:
    battery_2 = psutil.sensors_battery()
    percent_2 = int(battery_2.percent)
    if percent_2 != percent:
        print(f"Заряд батареи сменился: {percent_2}%")
        battery = psutil.sensors_battery()
        percent = int(battery.percent)
