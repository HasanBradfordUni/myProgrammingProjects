from win11toast import toast
import psutil

battery = psutil.sensors_battery()
loop = True

try:
    thisMessage = f'{battery.percent}% Remaining'
    print("Battery Percentage", thisMessage)
    toast("Battery Percentage", thisMessage)
except:
    print("No battery is installed, e.g. it is a desktop computer!")
    toast("Battery Percentage", "No battery is installed, e.g. it is a desktop computer!")


