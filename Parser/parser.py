#!/usr/bin/env python

keyword_map = {
    'watch.add_to_watch_list': ['watchlistadd'],
    'watch.search_movies': ['moviesearch'],
    'places.search': ['placesearch'],
    'weather.current': ['weather', 'temp', 'temperature'],
    'soundboard.play': ['soundboard', 'play'],
    'thing.add': ['add'],
    'thing.search': ['search']
}

def parse(text):
    words = text.split(' ')
    user_start_word = words[0]
    user_args = words[1:]

    for task in keyword_map:
        for keyword in keyword_map[task]:
            if user_start_word == keyword:
                return {'task': task, 'args': user_args}
    return None