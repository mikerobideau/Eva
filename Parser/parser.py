#!/usr/bin/env python


task_keywords = {
    'soundboard': ['soundboard', 'play']
}

def parse(text):
    words = text.split(' ')
    task = get_task(words[0])
    if not task:
        print "Sorry, I don't know what you mean."
    else:
        print 'Okay, running task %s' % (task)

def get_task(word):
    for task in task_keywords:
        for keyword in task_keywords[task]:
            if word == keyword:
                return task
    return None
