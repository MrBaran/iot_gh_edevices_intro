from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()
number = ghs.greenhouse.house_number

print("IoT Greenhouse - Electronic Devices Introduction.")
print("House Number: " + number)
print()

print("Investigate basic digital electonics.")
print("Use the toggle switch to activate the red LED lamp.")
print("Jumpers must be positioned on J1 as specified in activity.")
while ghs.switches.push_button.is_off():
    #investigate temperature service
    state = ghs.switches.toggle.get_value()
    if state == ghs.switches.SWITCH_ON:
        ghs.lamps.red.on()
    else:
        ghs.lamps.red.off()
    sleep(.5)
    
print()
print("Test code completed.")
