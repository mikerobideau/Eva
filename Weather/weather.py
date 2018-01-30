#!/usr/bin/env python

import requests
import geocoder

API_KEY='9d568f7976a0cbb68c5dc1bef1bb866f'

def current(args):
	g = geocoder.ip('me')
	url = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s&units=imperial' % (g.latlng[0], g.latlng[1], API_KEY)
	r = requests.get(url)
	
	json = r.json()
	location = json['name']
	weather = json['weather']
	primary_description = weather[0]['description']
	main = json['main']
	temp = int(main['temp'])

	msg_text = 'In %s, it\'s %s degrees. The current weather is %s.' % (location, temp, primary_description)
	msg = {'msg': msg_text}
	return msg