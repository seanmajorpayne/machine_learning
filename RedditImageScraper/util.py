# Util v1.0 - For RIS
# This program contains a series of helper methods for the RIS program.

import requests
import csv
import cv2
import imageio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, sys

x, y = 96, 96

# Grab the initial URL from the user (Parameters to be added)
def get_start_url(subreddit, category, timeframe):
	url = 'https://www.reddit.com/r/' + subreddit + '/' + category + '/.json?t=' + timeframe
	return url

# Reddit requires a specific user agent for scraping programs
# Please change this value to specify what you're doing.
def request_site(url):
	headers = {'user-agent': 'python3:machine-learning-project v1.0 by u/yourusername'}
	response = requests.get(url, headers=headers)
	return response

# Converts an image to a Numpy array
def image_to_numpy(im):
	im = np.mean(im, axis=2)		# rgb 3 channel -> 1 channel b&w
	im = cv2.resize(im, dsize=(x, y), interpolation=cv2.INTER_LINEAR)
	im = im / 255.0					# Normalize data 0-1
	im = im.reshape(1, x*y)
	return im

# Downloads an image from the web, calls image_to_numpy and returns numpy Array
def get_image(url):
	r = request_site(url)
	if r.status_code == 200:	
		im = imageio.imread(r.content)						
		return image_to_numpy(im)
	else:
		print("Failed to Download Image:", url, "Reason:", r)

# Reads in data from a CSV file and grabs the image portion of the data.
def get_data():
	df = pd.read_csv('scraped_images.csv', header=None)
	X = df.to_numpy()
	X = X[:,1:]
	return X

# Appends a matrix to a csv file. Creates file if it doesn't exist.
def save_csv(matrix):
	file_location = os.path.join(sys.path[0], 'app/static/tmp/scraped_images.csv')
	print(file_location)
	with open(file_location,"w+") as my_csv:
 		csvWriter = csv.writer(my_csv,delimiter=',')
 		csvWriter.writerows(matrix)
 		print("done")

# Plots an image from a given numpy array
def plot_image(im):
	im = im.reshape(x, y)
	plt.imshow(im, cmap='gray')
	plt.show()

# Builds a URL for a JSON request using a post id & subreddit
def url_builder(post_id, subreddit):
	url = ('https://gateway.reddit.com/desktopapi'
			'/v1/subreddits/' + subreddit + '?rtj=only'
			'&redditWebClient=web2x&app=web2x-client-production'
			'&allow_over18=&include=identity%2CprefsSubreddit'
			'&after=' + str(post_id) + '&dist=5&layout=card&sort=top&t=all')			
			
	return url