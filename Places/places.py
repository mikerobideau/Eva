#!/usr/bin/env python

import requests
import geocoder

API_KEY = ' AIzaSyCBkdF3pOZq71G_JT78s3B0iqHgmWEHpMg'
URL_BASE = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
RADIUS = 15000
MAX_RESULTS = 10

def search(args):
	keywords = ' '.join(args)

	g = geocoder.ip('me')

	latlng = '%s,%s' % (g.latlng[0], g.latlng[1])

	url = (
           '%s?location=%s'
           '&radius=%s'
           '&keyword=%s'
           '&key=%s') % (URL_BASE, latlng, RADIUS, keywords, API_KEY)

	#print url

	r = requests.get(url)

	json = r.json()

	if json['status'] == 'ZERO_RESULTS':
		msg_text = 'No results found.'

	i = 1
	place_msgs = []
	for place in json['results']:
		if i > MAX_RESULTS:
			break
		if 'vicinity' in place:
			place_msg = '%s. %s (%s)' % (i, place['name'], place['vicinity'])
		else:
			place_msg = '%s. %s' % (i, place['name'])
		
		place_msgs.append(place_msg)
		i += 1

	msg_text = ' '.join(place_msgs)
	msg = {'msg': msg_text}
	return msg