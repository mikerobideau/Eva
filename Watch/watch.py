import moviedb
import watch_list

def add_to_watch_list(args):
	return watch_list.add(args)
	
def search_movies(args):
	return moviedb.search(args)