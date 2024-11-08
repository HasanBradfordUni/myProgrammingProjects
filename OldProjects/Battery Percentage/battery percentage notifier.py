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

while True:
    if battery.percent == 100:
        print("Battery now fully charged!")
        toast("Battery now fully charged!")
        break
    elif loop==False:
        print("Battery not yet fully charged!")
        toast("Battery not yet fully charged!")
        break
