# RIS - Reddit Image Scraper v1.0
# This program scrapes a specified subreddit for image data, converts the images
# into a numpy array of size 96x96 & stores them in a CSV file.
# The downloaded data is intended to help with ML projects.
# Currently, only the top posts of all time are scanned, but this will be changed in
# future versions.

import json
import numpy as np
from util import save_csv, url_builder, request_site, get_image, get_start_url
from time import sleep

id_dict = {}

# Gets the URL & Score from JSON data.
def get_data(p, first):
	if first:
		score, url = p['data']['ups'], p['data']['url']
	else:
		score, url = p['score'], p['media']['content']
	return score, url

# Extracts the upvote count from the initial JSON.
def extract_upvotes_first(json):
	try:
		return(int(json['data']['score']))
	except KeyError:
		print("Failed to Extract Upvotes")
		return(-1)

# Extracts the upvote count from the infinite scroll JSON.
# Note that the JSON value locations are different
def extract_upvotes(json):
	try:
		return(int(json['score']))
	except KeyError:
		print("Failed to Extract Upvotes")
		return(-1)

# Extracts post data from the initial JSON. Also gets the id of the
# last post which will be used for future JSON requests.
def json_to_first_posts(json):
	post_container = json['data']['children']
	posts = [p for p in post_container
				if len(p['data']['name']) <= 9					# Remove Ads,
				and p['data']['post_hint'] == 'image']			# and non-image posts	
	posts.sort(key=extract_upvotes_first, reverse=True)
	for p in posts:
		id_dict[p['data']['name']] = p['data']['score']
	return posts, posts[-1]['data']['name']

# Extracts post data from the infinite scroll JSON. Also gets the id of the
# last post which will be used for future JSON requests
def json_to_posts(json):
	post_container = json['posts']
	posts = [p for p in post_container.values()
				if len(p['id']) <= 9					# Remove Ads,
				and p['media'] != None
				and p['media']['type'] == 'image'		# and non-image posts
				and p['id'] not in id_dict]				# no duplicates
	posts.sort(key=extract_upvotes, reverse=True)
	for p in posts:
		id_dict[p['id']] = p['score']
	return posts, posts[-1]['id']

# Gets the posts & reload_id and returns them
def get_posts(json, first):
	if(first):
		posts, reload_id = json_to_first_posts(json)
	else:
		posts, reload_id = json_to_posts(json)
	return posts, reload_id

# Adds image data into a Numpy array and returns it.
def process_images(j, first):
	posts, reload_id = get_posts(j, first)
	X = np.zeros((len(posts), 96*96+1))
	for i, p in enumerate(posts):
		score, url = get_data(p, first)
		sleep(1)
		im = get_image(url)
		X[i,0], X[i,1:] = score, im
	return X, reload_id	

# Scrapes the specified URL and saves numpy data into a CSV.
def scrape_site(url, first):
	r = request_site(url)
	if r.status_code == 200:
		X, reload_id = process_images(r.json(), first)
		save_csv(X)
		return reload_id
	else:
		print("Error Scraping Website, Could Not Connect")

# Scrapes the site for a user specified number of iterations. 
def main():
	url, subreddit = get_start_url()
	print("Starting Scrape Iteration:", 1)
	reload_id = scrape_site(url, True)
	url = url_builder(reload_id, subreddit)
	for i in range(1):
		print("Starting Scrape Iteration:", i+2)
		reload_id = scrape_site(url, False)
		url = url_builder(reload_id, subreddit)
		

if __name__ == '__main__':
	main()