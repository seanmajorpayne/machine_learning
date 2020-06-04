# RIS - Reddit Image Scraper v1.0
# This program scrapes a specified subreddit for image data, converts the images
# into a numpy array of size 96x96 & stores them in a CSV file.
# The downloaded data is intended to help with ML projects.
# Currently, only the top posts of all time are scanned, but this will be changed in
# future versions.

import json
import numpy as np
from app.util import save_csv, url_builder, request_site, get_image, get_start_url, plot_image
from time import sleep
from app.JsonParse import JsonParserFirst, JsonParser

id_dict = {}

def postsToNumpy(parser, posts):
	"""Takes a list of posts and extracts
	their scores and pixel values. Returns this
	information as a matrix.
	"""
	X = np.zeros((len(posts), 96*96+1))
	
	upvote_minimum = float('inf')
	
	reload_id = 0
	
	for i, p in enumerate(posts):
		upvotes = parser.getUpvotes(p)
		url = parser.getURL(p)
		id = parser.getId(p)
		
		if upvotes < upvote_minimum:
			upvote_minimum = upvotes
			reload_id = id
		
		id_dict[id] = upvotes	# Prevent duplicates
		sleep(1)
		im = get_image(url)
		X[i,0], X[i,1:] = upvotes, im
	
	return X, reload_id

def getParser(json_response):
	"""Reddit uses two distinct JSON structures.
	One structure is ['data']['children']
	The other structure is ['posts']
	This method returns the correct class to parse the structures.
	"""
	
	if 'data' in json_response:
		return JsonParserFirst(json_response)
	else:
		return JsonParser(json_response, id_dict)


def getJson(url):
	"""Checks if a specified URL is available
	and returns the JSON from that URL
	"""
	r = request_site(url)
	if r.status_code != 200:
		raise Exception("Unable to connect to Website, Response is not 200")
	return r.json()


def scrapeSite(subreddit, category, timeframe):
	url = get_start_url(subreddit, category, timeframe)
	for i in range(1):
	
		json_response = getJson(url)
		
		parser = getParser(json_response)
		
		posts = parser.getPosts()
		matrix_of_posts, reload_id = postsToNumpy(parser, posts)
		
		save_csv(matrix_of_posts)
		url = url_builder(reload_id, subreddit)
	
	
#if __name__ == '__main__':
#	main()