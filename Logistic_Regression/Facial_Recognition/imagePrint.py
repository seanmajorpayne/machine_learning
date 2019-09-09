# This file plots the images in matplotlib with their corresponding labels

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from util import get_data

X, Y = get_data()	# Don't need to balance samples to print

labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

true = 1
i = 0
while true:
	data = X[i].reshape(48,48)
	print(data)
	plt.imshow(data, cmap='gray')
	plt.title(labels[Y[i]])
	plt.show()
	quit = input('To quit type "Y"')
	if quit == "Y":
		true = 0
	i += 1