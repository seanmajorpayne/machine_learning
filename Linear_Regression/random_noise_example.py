import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# This program demonstrates that adding a column
# of random noise improves the R^2 for linear regression

# Prepare for data loading
X = []
Y = []

# Open the file and load the data
for line in open('data/data_2d.csv'):
	x1, x2, y = line.split(',')
	X.append([float(x1), float(x2), 1])
	Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

def plot3dData(X, Y):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(X[:,0], X[:,1], Y)
	plt.show()

# Find the weights
def getWeights(X, Y):
	w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
	return w

# Get the Predictions
def getPredictions(X, w):
	Y_hat = X.dot(w)
	return Y_hat

def calculateRSquared(Y, Y_hat):
	d1 = Y - Y_hat
	d2 = Y - Y.mean()
	r2 = 1 - (d1.dot(d1) / d2.dot(d2))
	return r2


w = getWeights(X, Y)
Y_hat = getPredictions(X, w)
plot3dData(X, Y)
r2 = calculateRSquared(Y, Y_hat)
print("The R2 value without noise is:", r2)

def addNoise(X):
	N, D = X.shape
	noise = np.random.randn(N)
	X_with_noise = np.zeros((N, D+1))
	X_with_noise[:,0:2] = X[:,0:2]
	X_with_noise[:,2] = noise
	X_with_noise[:,3] = X[:,2]
	return X_with_noise

X_with_noise = addNoise(X)
w = getWeights(X, Y)
Y_hat = getPredictions(X, w)
r2 = calculateRSquared(Y, Y_hat)
print("The R2 value with noise is:", r2)