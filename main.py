# coding: utf-8

from itinerary import get_time_to_work_text
from weather import get_weather_at_home_text
import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
import vlc
import os


# consts
CHANNEL_PROXIMITY_SENSOR = 7
MINUTES_TO_KEEP_ON = 10
DEPARTURE_HOUR = 9
DEPARTURE_MINUTE = 0

# sound level
cmd = "amixer set PCM -- 100%"
os.system(cmd)


# vars
is_playing = False
last_say_hour = ''
last_run_datetime = datetime.now() + timedelta(days=-1)
player = vlc.MediaPlayer(
    "http://chai5she.lb.vip.cdn.dvmr.fr/franceinter-midfi.mp3")


def setup_proximity_sensor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(CHANNEL_PROXIMITY_SENSOR, GPIO.IN)


def say(text):
    print text
    cmd = 'pico2wave -l fr-FR -w lookdave.wav ".. %s" && aplay lookdave.wav' % text
    os.system(cmd)


def presence_detected():
    global last_run_datetime
    today_datetime = datetime.now().replace(hour=5, minute=0)
    is_first_detection_today = last_run_datetime < today_datetime
    is_morning = today_datetime.hour >= 6 and today_datetime <= 12
    if is_first_detection_today and is_morning:
	last_run_datetime = datetime.now()
	is_playing = False
        say(get_weather_at_home_text())
        if is_week_day():
            say(get_time_to_work_text(DEPARTURE_HOUR, DEPARTURE_MINUTE))
        player.play()


def absence_detected():
    is_playing = False
    player.stop()


def is_week_day():
    weekday = datetime.now().weekday()
    return weekday > 0 and weekday < 5


def say_hour():
    # global last_say_hour
    current_text = 'il est %s heure %s' % (datetime.now().hour+1, datetime.now().minute)
    
    if last_say_hour is not current_text:
        last_say_hour = current_text    
	player.audio_set_volume(0)
    	say('il est %s heure %s' % (datetime.now().hour, datetime.now().minute))
    	player.audio_set_volume(100)

def run_loop():
    global last_run_datetime
    THRESHOLD = 1000

    total = 0
    nb_off = 0
    was_on = False
    time_to_stop = 0

    say("Radio Raspberry prêt")

    while True:
        value = GPIO.input(CHANNEL_PROXIMITY_SENSOR)

        if value == GPIO.LOW:
            nb_off = nb_off + 1

        total = total + 1
	
	if is_playing and datetime.now().minute % 5 == 0:
	    say_hour()

        if total >= THRESHOLD:
	    # print nb_off
            if nb_off < THRESHOLD * 0.3:
                time_to_stop = time.time() + (MINUTES_TO_KEEP_ON * 60)

                if not was_on:
                    presence_detected()
                    was_on = True

            elif was_on and time.time() > time_to_stop:
                absence_detected()
                was_on = False

            total = 0
            nb_off = 0
	
	sleep_time = 0.001
	today_datetime = datetime.now().replace(hour=5, minute=0)
	has_detected_person_today = last_run_datetime > today_datetime
        #if has_detected_person_today:
	    #sleep_time = 60
	time.sleep(sleep_time)


setup_proximity_sensor()
run_loop()