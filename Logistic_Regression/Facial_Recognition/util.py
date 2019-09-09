import numpy as np
import pandas as pd
from sklearn.utils import shuffle

# Get data from the CSV file & convert into Numpy arrays.
# Data is normalized for plotting & for logistic regression
# If there are significantly higher samples of one class, the
# samples need to be balanced.
def get_data(balance_ones=True):
	df = pd.read_csv("fer2013/fer2013.csv")
	data = df.to_numpy()
	N = data.shape[0]
	
	X = np.zeros([N,2304])		# Images are 48x48
	Y = data[:, 0].astype(int)
	for i in range(N):
		x = data[i,1].split()
		X[i] = x
	X = X / 255					# Normalize
	
	return X, Y

# Returns only the data corresponding to the first two emotions
# Used for the logistic regression model
def get_binary_data():
	X, Y = get_data()
	X = X[Y<=1]
	Y = Y[Y<=1]
	X, Y = shuffle(X, Y)
	return X, Y

# Returns the average error given our targets and predictions
def error_rate(targets, predictions):
	return np.mean(targets != predictions)

# Returns the sigmoid function cost
def sigmoid_cost(T, Y):
	return -(T*np.log(Y) + (1-T)*np.log(1-Y)).sum()
	
# Calculates the sigmoid function given a decimal value
def sigmoid(z):
	return 1 / (1 + np.exp(-z))