import RPi.GPIO as GPIO
import time
from itinerary import get_time_to_work_text
from weather import get_weather_at_home_text
from datetime import datetime, timedelta
import vlc
import os

#player = vlc.MediaPlayer(
#    "http://chai5she.lb.vip.cdn.dvmr.fr/franceinter-midfi.mp3")

sensor = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
current = GPIO.input(sensor)
previous = current
def printState(current):
    print 'GPIO pin %s is %s' % (sensor, 'HIGH' if current else 'LOW')
printState(current)
while True:
    current = GPIO.input(sensor)
    if current != previous:
        printState(current)
	# player.play()
    previous = current
    time.sleep(0.1)
GPIO.cleanup()
