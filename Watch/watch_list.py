#!/usr/bin/env python

import sys
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.eva
watch_list = db.watch_list

def add(args):    
    media = ' '.join(args)
    record = {
        'name': media
    }
    result = watch_list.insert_one(record)
    msg_text = 'Added %s' % media
    msg = {'msg': msg_text}
    print msg
    return msg

def search(args):
    media = ' '.join(args)
    results = watch_list.find_one({'name': media})
    if results:
        msg_text = 'Found %s' % (results['name'])
    else:
        msg_text = 'No results found.'
    msg = {'msg': msg_text}
    return msg