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
from JsonParse import JsonParserFirst

id_dict = {}

# Sends a request to the specified URL
# Returns Json if response is 200, otherwise throws an error
def getJson(url):
	r = request_site(url)
	if r.status_code != 200:
		raise Exception("Unable to connect to Website, Response is not 200")
	return r.json()

# Scrapes the site for a user specified number of iterations. 
def main():
	url, subreddit = get_start_url()
# 	json_response = getJson(url)
# 	print(json.dumps(
# 		json_response,
# 		sort_keys=True,
# 		indent=4,
# 		separators=(',', ': ')
# 	))
# 	parser = JsonParserFirst(json_response)
# 	posts = parser.getPosts()
	
	r = request_site("https://www.reddit.com/r/photocritique/comments/9i2i44/got_stuck_in_london_for_24hrs_when_i_missed_my/")
	print(r.json())
	

if __name__ == '__main__':
	main()