#!/usr/bin/env python

import sys
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.smartpi
watch_list = db.watch_list

def add():
    try:
        media = sys.argv[2]
        record = {
            'name': media
        }
        result = watch_list.insert_one(record)
        sys.stdout.write('Added record %s \n' % (result.inserted_id))
        return True

    except IndexError:
        sys.stdout.write('Please specify a show or movie \n')
        return False

def search():
    try:
        media = sys.argv[2]
        results = watch_list.find_one({'name': media})
        sys.stdout.write('%s \n' % (results))

    except IndexError:
        sys.stdout.write('Please specify a show or movie \n')

if __name__=='__main__':
    try:
        task = sys.argv[1]
        if task == 'add':
            add()
        elif task == 'search':
            search()
        else:
            sys.stdout.write('I\'m not sure what "%s" is.  You can say "add" or "search". \n' % (task))

    except IndexError:
        sys.stdout.write('Please specify a task.  You can say "add" or "search". \n')
