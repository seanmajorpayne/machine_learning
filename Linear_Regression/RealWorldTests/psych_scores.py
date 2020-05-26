import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Test Scores for General Psychology

The data (X1, X2, X3, X4) are for each student.
X1 = score on exam #1
X2 = score on exam #2
X3 = score on exam #3
X4 = score on final exam
"""

def normalizeData(X, D):
	for i in range(D):
		X[:, i] = X[:, i] / np.amax(X[:, i])
	return X

def plotData(X, Y, title):
	plt.scatter(X, Y)
	plt.title(title)
	plt.show()

def getWeights(X, Y):
	w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
	return w

def getPredictions(X, w):
	Yhat = X.dot(w)
	return Yhat

def getR2(Y, Yhat):
	d1 = Y - Yhat
	d2 = Y - np.mean(Y)
	r2 = 1 - (d1.dot(d1) / d2.dot(d2))
	return r2

def fit(X, Y):
	w = getWeights(X, Y)
	Yhat = getPredictions(X, w)
	r2 = getR2(Y, Yhat)
	print("The R2 value is:", r2)

# Load Data
df = pd.read_excel('data/mlr03.xls')

# Convert to Numpy
X = df.values.astype(float)
N = X.shape[0]
D = X.shape[1]

X = normalizeData(X, D)

# Break up into vectors
test_one = X[:, 0]
test_two = X[:, 1]
test_three = X[:, 2]
final_test = X[:, 3]

# Padding for bias term
ones = np.ones(N)


Y = final_test

# Run test 1 vs. final test
plotData(test_one, final_test, "Test one vs. Final")
X = np.column_stack((test_one, ones))
fit(X, Y)

# Run test 2 vs. final test
plotData(test_two, final_test, "Test two vs. Final")
X = np.column_stack((test_two, ones))
fit(X, Y)

# Run test 3 vs. final test
plotData(test_three, final_test, "Test three vs. Final")
X = np.column_stack((test_three, ones))
fit(X, Y)



