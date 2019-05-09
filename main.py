# See https://docs.pycom.io for more information regarding library specifics

from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE
import pycom
import time

pycom.heartbeat(False)

py = Pysense()

# display the reset reason code and the sleep remaining in seconds
# possible values of wakeup reason are:
# WAKE_REASON_ACCELEROMETER = 1
# WAKE_REASON_PUSH_BUTTON = 2
# WAKE_REASON_TIMER = 4
# WAKE_REASON_INT_PIN = 8
print("Wakeup reason: " + str(py.get_wake_reason()) + "; Approximate sleep remaining: " + str(py.get_sleep_remaining()) + " sec")
time.sleep(0.5)

# enable wakeup source from INT pin
py.setup_int_pin_wake_up(False)

# enable activity and also inactivity interrupts, using the default callback handler
py.setup_int_wake_up(True, True)

acc = LIS2HH12()
mp = MPL3115A2(py,mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
mpp = MPL3115A2(py,mode=PRESSURE) # Returns pressure in Pa. Mode may also be set to ALTITUDE, returning a value in meters
si = SI7006A20(py)
lt = LTR329ALS01(py)
# enable the activity/inactivity interrupts
# set the acceleration threshold to 2000mG (2G) and the min duration to 200ms
acc.enable_activity_interrupt(2000, 200)

# check if we were awaken due to activity
if acc.activity():
    pycom.rgbled(0xFF0000)
    logRun(acc,mp,mpp,si,lt)
else:
    pycom.rgbled(0x00FF00)  # timer wake-up
time.sleep(0.1)

# go to sleep for 1 hour maximum if no accelerometer interrupt happens
py.setup_sleep(3600)
py.go_to_sleep()
################################################################################
# print("Light (channel Blue lux, channel Red lux): " + str(lt.light()))
