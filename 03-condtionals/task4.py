'''
Docstring for 03-condtionals.task4
You are building a smart thermostat alert system
1. If the device_status is "active"
    And temprature > 35 -> Warm:"High temprature alert"
    Else: "Temprature normal"
2. If device is off: "Device is offline"
'''
device_status = "active"
temprature = float(input("Enter the temprature: "))
if device_status == 'active':
    if temprature > 35:
        print("High temprature alert")
    else:
        print("Thermostat is normal")
else:
    print("Device is offline")