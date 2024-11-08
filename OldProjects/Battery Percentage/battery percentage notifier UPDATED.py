from win11toast import toast
import psutil
from time import sleep

battery = psutil.sensors_battery()
loop = True
prevPercentage = 0

try:
    thisMessage = f'{battery.percent}% Remaining'
    print("Battery Percentage", thisMessage)
    toast("Battery Percentage", thisMessage)
    sleep(5)
    if loop:
        print("Battery not yet fully charged!")
        toast("Battery not yet fully charged!")
except:
    print("No battery is installed, e.g. it is a desktop computer!")
    toast("Battery Percentage", "No battery is installed, e.g. it is a desktop computer!")

while True:
    battery = psutil.sensors_battery()
    if battery.percent == 100:
        print("Battery now fully charged!")
        toast("Battery now fully charged!")
        break
    elif loop==False:
        print("Battery not yet fully charged!")
        toast("Battery not yet fully charged!")
        break
    else:
        if battery.percent > prevPercentage:
            batteryMessage = f'Battery Percentage: {battery.percent}% Remaining'
            print(batteryMessage)
            toast(batteryMessage)
    prevPercentage = battery.percent
