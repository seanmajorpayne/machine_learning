# Reddit Image Scraper

## Project Overview

The goal of this project is to harvest data for machine learning projects. Currently,
the program downloads images from Reddit, formats them into 96x96 pixel images, downgrades
them from 3-channel RGB to 1-channel B&W, converts to a numpy array and saves them
into a CSV.

Following Reddit's API Guidelines, this program makes roughly 60 requests per minute to
the site. Please respect Reddit's guidelines and do not change this value.

In the current state, the program will only pull from the top posts of all time, but this
will be changed soon.

## File Descriptions
1. RIS.py - Scrapes website for images & saves them to CSV
2. util.py - Series of helper methods
3. plot_images.py - A test program to see the downloaded images


### Downloaded Data format

File Type: CSV
```
Col1, Col2... Col9216
Upvotes, Image_Data
```
- Upvotes are a real number value (This will be reformatted soon)
- Image_Data consists of float values from 0-1. One value per column.

## How to Run
The first iteration of this program is not user friendly. In the future, a user interface
will be created for ease of use.

1. Open the util.py file and change the user_agent value to a specific name. See the [Reddit
API](https://github.com/reddit-archive/reddit/wiki/API) for more details.

2. In the RIS.py file, change the range value in the forloop for the number of iterations
that you desire. (Each iteration downloads JSON which contains another 25 images)

## Challenges & Limitations

Reddit uses an infinite scrolling user interface which complicates scraping. HTML can
not be conveniently parsed, so the program relies on working with JSON data.

The JSON data from the initial page load request is in a different format
than the subsequent requests for infinite scrolling posts. This required separate
methods to parse. (Although I may be able to remedy this in the near future).

Additionally, the JSON data is not guaranteed to be in a consistent order, so the data
must be resorted based on the number of upvotes a post received.

## Checklist & Future Revisions
- [x] First Draft Uploaded
- [x] Revisit JSON Request Types & condense if possible
- [x] Add parameters for specifying category & timeframe
- [x] Get test application working in Flask
- [ ] Add User Interface to Github
- [ ] Write documentation for how to download/use
- [ ] Host on Web for demo



