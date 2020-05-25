import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# This program predicts systolic blood 
# pressure based on age and weight.

# Data is (X1, X2, X3) for each patient
# X1 = Blood Pressure
# X2 = Age in Years
# X3 = Weight in Pounds

# Convert all dataframes to numpy arrays
def convertToNumpy(X, X2, X3, Y):
	X = np.array(X)
	X2 = np.array(X2)
	X3 = np.array(X3)
	Y = np.array(Y)
	return X, X2, X3, Y

# Plot scatter plots
def plotData(X, Y):
	plt.scatter(X, Y)
	plt.show()

# Calculate the R^2
def calculateRSquared(X, Y):
	# Calculate the weights
	w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))

	# Calculate the Predictions
	Y_hat = X.dot(w)

	d1 = Y - Y_hat
	d2 = Y - Y.mean()
	r2 = 1 - (d1.dot(d1) / d2.dot(d2))
	return r2

# Load Data and add padding of 1s to each dataset 
df = pd.read_excel('data/mlr02.xls') # Data from college.cengage.com
df = df.astype(float)
df['ones'] = 1
X = df[['X2', 'X3', 'ones']]
Y = df['X1']
X2_only = df[['X2', 'ones']]
X3_only = df[['X3', 'ones']]

# Convert to Numpy
X, X2_only, X3_only, Y = convertToNumpy(X, X2_only, X3_only, Y)

# Plot both data to observe linear relationship
plotData(X2_only[:,0], Y)
plotData(X3_only[:,0], Y)

# Print the R^2 Values
print("The R2 for X2_only is:", calculateRSquared(X2_only, Y))
print("The R2 for X3_only is:", calculateRSquared(X3_only, Y))
print("The R2 for X2 & X3 is:", calculateRSquared(X, Y))

# Add noise to the X matrix
def addNoise(X):
	N, D = X.shape
	noise = np.random.randn(N)
	X_with_noise = np.zeros((N, D+1))
	X_with_noise[:,0:2] = X[:,0:2]
	X_with_noise[:,2] = noise
	X_with_noise[:,3] = X[:,2]
	return X_with_noise

# Test X with noise added to see how R2 is affected
# As seen here, it increases slightly
X_with_noise = addNoise(X)
print("The R2 for X2 & X3 with noise is:", calculateRSquared(X_with_noise, Y))
