import numpy as np
import pandas as pd

# Reads our CSV data, normalizes & one hot encodes data
# and returns an X Matrix and Y Vector
def get_data():
	data = pd.read_csv("ecommerce_data.csv")
	data = data.to_numpy()
	
	X = data[:,:-1]
	Y = data[:,-1]
	
	X[:,1] = normalize(X[:,1])
	X[:,2] = normalize(X[:,2])
	
	N, D = X.shape
	X2 = np.zeros([N, D+3])
	X2[:,:D-1] = X[:,:-1]
	
	# One Hot Encode (For Time of Day values 0 - 3)
	t = X[:,-1].astype(int)
	for i in range(N):
		X2[i, t[i]+D-1] = 1

	return X2, Y

# Takes in a column, normalizes the data and returns it 
# (Returns decimal values in range -1 to 1)
def normalize(c):
	c = c - c.mean() / c.std()
	return c

# Returns Inputs and Outputs for only two of our Outputs (0 & 1)
# These correspond to Bounce & Add to Cart
def get_binary_data():
	X, Y = get_data()
	X = X[Y<=1]
	Y = Y[Y<=1]
	return X, Y
	

X, Y = get_binary_data()