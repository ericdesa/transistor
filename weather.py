# coding: utf-8

import json
import urllib
import urllib2
import time
from yahoo_oauth import OAuth2


def get_weather_at_home():
    url = "https://query.yahooapis.com/v1/public/yql?q=select+%2A+from+weather.forecast+where+woeid%3D%22626021%22+%20and%20+u%3D%22c%22&language=fr-FR&format=json"
    print url

    #oauth = OAuth2(None, None, from_file='weather_yahoo_keys.json')
    # if not oauth.token_is_valid():
    #    oauth.refresh_access_token()
    # result = oauth.session.get(url)
    #result = api_mock()

    request_failed = True
    while request_failed:
        result = urllib.urlopen(url)
        data = json.load(result)

        request_failed = data['query']['count'] == 0
        if request_failed:
            print "request failed, wait 2 seconds"
            time.sleep(2)
        else:
            condition = data['query']['results']['channel']['item']['condition']
            temp = condition['temp'].encode('utf-8')
            condition_code = condition['code']
            condition_text = condition_code_to_text(condition_code)

    return condition_text, temp


def condition_code_to_text(value):
    return {
        '0': 'Il y a une tornade.',
        '1': 'Il y a une tempête tropicale.',
        '2': 'Il y a un houragan.',
        '3': 'Il y a des orages.',
        '4': 'Il y a de la neige fondue.',
        '5': 'Il y a de la neige fondue.',
        '6': 'Il y a de la neige fondue.',
        '7': 'Il y a de la neige fondue.',
        '8': 'Il y a de la pluie verglaçante.',
        '9': 'Il y a de la pluie froide.',
        '10': 'Il y a de la pluie verglaçante.',
        '11': 'Il pleut.',
        '12': 'Il pleut.',
        '13': 'Il y a une averse de neige.',
        '14': 'Il y a une légère chute de neige.',
        '15': 'Il y a de la neige et du vent.',
        '16': 'Il neige.',
        '17': 'Il grêle.',
        '18': 'Il y a de la neige fondue.',
        '19': 'Bordel de merde, un nuage de poussière !',
        '20': 'Il y a du brouillard.',
        '21': 'Il y a de la brume.',
        '22': 'Il y a de la brume.',
        '23': 'Il y a un tempête. Rien que ça.',
        '24': 'Il y a du vent.',
        '25': 'Il fait froid.',
        '26': 'Le temps est couvert.',
        '27': 'Le temps est couvert ce soir.',
        '28': 'Le temps est couvert aujourd\'hui.',
        '29': 'Le temps est couvert ce soir.',
        '30': 'Le temps est couvert aujourd\'hui.',
        '31': 'Le temps est dégagé.',
        '32': 'Le temps est ensolleillé.',
        '33': 'Le temps est ensolleilé.',
        '34': 'Le temps est ensolleilé.',
        '35': 'Il pleut avec de la grêle.',
        '36': 'Il fait chaud.',
        '37': 'Il y a quelques orages.',
        '38': 'Il y a quelques orages.',
        '39': 'Il y a quelques orages.',
        '40': 'Il y a des averses passagères.',
        '41': 'Il neige beaucoup.',
        '42': 'Il neige un peut.',
        '43': 'Il neige beaucoup.',
        '44': 'Le ciel est partiellement couvert.',
        '45': 'Il y a une tempète de neige.',
        '46': 'Il neige beaucoup.',
        '47': 'Il y a quelques orages.',
        '3200': ''
    }[value]


def api_mock():
    return "{\"query\":{\"count\":1,\"created\":\"2017-01-03T19:59:14Z\",\"lang\":\"en-US\",\"results\":{\"channel\":{\"units\":{\"distance\":\"km\",\"pressure\":\"mb\",\"speed\":\"km/h\",\"temperature\":\"C\"},\"title\":\"Yahoo! Weather - Saint-Michel-sur-Orge, Ile-de-France, FR\",\"link\":\"http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-12728218/\",\"description\":\"Yahoo! Weather for Saint-Michel-sur-Orge, Ile-de-France, FR\",\"language\":\"en-us\",\"lastBuildDate\":\"Tue, 03 Jan 2017 08:59 PM CET\",\"ttl\":\"60\",\"location\":{\"city\":\"Saint-Michel-sur-Orge\",\"country\":\"France\",\"region\":\" Ile-de-France\"},\"wind\":{\"chill\":\"27\",\"direction\":\"250\",\"speed\":\"11.27\"},\"atmosphere\":{\"humidity\":\"100\",\"pressure\":\"34473.45\",\"rising\":\"0\",\"visibility\":\"7.24\"},\"astronomy\":{\"sunrise\":\"8:43 am\",\"sunset\":\"5:9 pm\"},\"image\":{\"title\":\"Yahoo! Weather\",\"width\":\"142\",\"height\":\"18\",\"link\":\"http://weather.yahoo.com\",\"url\":\"http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif\"},\"item\":{\"title\":\"Conditions for Saint-Michel-sur-Orge, Ile-de-France, FR at 07:00 PM CET\",\"lat\":\"48.633041\",\"long\":\"2.3129\",\"link\":\"http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-12728218/\",\"pubDate\":\"Tue, 03 Jan 2017 07:00 PM CET\",\"condition\":{\"code\":\"26\",\"date\":\"Tue, 03 Jan 2017 07:00 PM CET\",\"temp\":\"0\",\"text\":\"Cloudy\"},\"forecast\":[{\"code\":\"26\",\"date\":\"03 Jan 2017\",\"day\":\"Tue\",\"high\":\"2\",\"low\":\"0\",\"text\":\"Cloudy\"},{\"code\":\"28\",\"date\":\"04 Jan 2017\",\"day\":\"Wed\",\"high\":\"6\",\"low\":\"1\",\"text\":\"Mostly Cloudy\"},{\"code\":\"34\",\"date\":\"05 Jan 2017\",\"day\":\"Thu\",\"high\":\"4\",\"low\":\"-1\",\"text\":\"Mostly Sunny\"},{\"code\":\"28\",\"date\":\"06 Jan 2017\",\"day\":\"Fri\",\"high\":\"0\",\"low\":\"-2\",\"text\":\"Mostly Cloudy\"},{\"code\":\"26\",\"date\":\"07 Jan 2017\",\"day\":\"Sat\",\"high\":\"5\",\"low\":\"-1\",\"text\":\"Cloudy\"},{\"code\":\"26\",\"date\":\"08 Jan 2017\",\"day\":\"Sun\",\"high\":\"6\",\"low\":\"2\",\"text\":\"Cloudy\"},{\"code\":\"26\",\"date\":\"09 Jan 2017\",\"day\":\"Mon\",\"high\":\"7\",\"low\":\"3\",\"text\":\"Cloudy\"},{\"code\":\"28\",\"date\":\"10 Jan 2017\",\"day\":\"Tue\",\"high\":\"3\",\"low\":\"0\",\"text\":\"Mostly Cloudy\"},{\"code\":\"28\",\"date\":\"11 Jan 2017\",\"day\":\"Wed\",\"high\":\"3\",\"low\":\"0\",\"text\":\"Mostly Cloudy\"},{\"code\":\"28\",\"date\":\"12 Jan 2017\",\"day\":\"Thu\",\"high\":\"3\",\"low\":\"0\",\"text\":\"Mostly Cloudy\"}],\"description\":\"\",\"guid\":{\"isPermaLink\":\"false\"}}}}}}"


def get_weather_at_home_text():
    condition, temp = get_weather_at_home()
    return '%s Il fait %s degrés' % (condition, temp)
