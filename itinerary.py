# coding: utf-8

import json
import urllib
from datetime import datetime


def get_time_to_work_text(hour, minute):
    expected_datetime = datetime.now().replace(hour=hour, minute=minute)
    departure_label = "a %d heure %d" % (hour, minute)
    if datetime.now() < expected_datetime:
        timestamp = expected_datetime.strftime("%s")
    else:
        timestamp = datetime.now().strftime("%s")
	departure_label = "maintenant"

    orgin = "14 rue de la noue rousseau, 91240 Saint Michel sur Orge".replace(
        " ", "+")
    destination = "3 avenue du Quebec, 91140 Villebon sur Yvette".replace(
        " ", "+")
    base_path = "https://maps.googleapis.com/maps/api/directions/json"
    url = base_path + "?origin=" + orgin + "&destination=" + destination + "&departure_time=" + \
        timestamp + "&language=fr_FR&traffic_model=pessimistic&key=AIzaSyDuHEkDopG1RK4dxRuYMVSJbHzyoDRI9ds"
    print url
    result = urllib.urlopen(url)
    data = json.load(result)

    duration = data['routes'][0]['legs'][0]['duration_in_traffic']['text']
    summary = data['routes'][0]['summary']

    return 'En partant %s il vous faudra %s pour arriver au travail via %s' % (departure_label, duration, summary)
