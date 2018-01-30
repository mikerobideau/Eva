#!/usr/bin/env python

import sys
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.eva
things = db.things

CATEGORY_DELIMS = ['to', 'category', 'in', 'for', 'under']
TAG_DELIMS = ['tag']

def parse_args(args):
    name_words = []
    category_words = []
    tag_words = []
    working_on = 'name'
    for word in args:
        word_is_delim = False
        if working_on == 'name':
            for ctg_delim in CATEGORY_DELIMS:
                if word == ctg_delim:
                    working_on = 'category'
                    word_is_delim = True

        if working_on == 'name':
            name_words.append(word)
        elif working_on == 'category':
            if not word_is_delim:
                category_words.append(word)

    name = ' '.join(name_words)
    category = ' '.join(category_words)

    if len(name) == 0 or len(category) == 0:
        return None

    record = {'name': name, 'category': category}

    return record

def add(args):    
    record = parse_args(args)

    if not record:
        msg_text ="To add something, the pattern is: 'Add blank to blank'"
    
    else:
        result = things.insert_one(record)
        msg_text = 'Added %s to %s' % (record['name'], record['category'])

    msg = {'msg': msg_text}
    print msg
    return msg

def search(args):
    category = ' '.join(args)
    print 'Searching in %s' % (category)
    results = things.find({'category': category})
    records = []
    if results:
        msg_text = results[0]['name']
        for r in results:
            print r
            records.append(r)
    else:
        msg_text = 'No results found.'

    msg = {'msg': msg_text, 'records': records}
    return msg