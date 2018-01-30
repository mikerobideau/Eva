#!/usr/bin/env python

import requests

API_KEY = '9397c07249c55dd4e067b7dc787cac5e'
URL_BASE = 'https://api.themoviedb.org/3'
POSTER_BASE = 'http://image.tmdb.org/t/p'
POSTER_SIZE = 'w500'

def search(args):
	keywords = '+'.join(args)
	url = '%s/search/movie?api_key=%s&query=%s' % (URL_BASE, API_KEY, keywords)

	#print url
	
	r = requests.get(url)
	
	json = r.json()
	movie = json['results'][0]
	title = movie['title']
	overview = movie['overview']
	poster_path = movie['poster_path']
	width = 500
	height = 725

	msg_text = '%s: %s' % (title, overview)
	poster_path = '%s/%s/%s' % (POSTER_BASE, POSTER_SIZE, poster_path)
	msg = {'msg': msg_text, 'img_url': poster_path, 'img_width': width, 'img_height': height, 'args': [title]}

	return msg