import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Thunder Basin Antelope Study

The data (X1, X2, X3, X4) are for each year.
X1 = spring fawn count/100
X2 = size of adult antelope population/100
X3 = annual precipitation (inches)
X4 = winter severity index (1=mild,
5=severe)
"""

def plotData(X, Y, title):
	plt.scatter(X, Y)
	plt.title(title)
	plt.show()

def normalizeData(X, D):
	"""Normalize each column of X to
	be between 0-1
	"""
	for i in range(D):
		X[:, i] = X[:, i] / np.amax(X[:,i])
	return X

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

def calculateValues(X, Y):
	w = getWeights(X, Y)
	Yhat = getPredictions(X, w)
	r2 = getR2(Y, Yhat)
	print("The R2 Value is:", r2)

# Load Data
df = pd.read_excel("data/mlr01.xls")

# Convert to Numpy
X = df.values
N = X.shape[0]
D = X.shape[1]

X = normalizeData(X, D)

fawn_count = X[:, 0]
adult_population = X[:, 1]
precipitation = X[:, 2]
winter_severity = X[:, 3]

# Make plots to visualize relationships
plotData(fawn_count, adult_population, "Fawn Count vs. Adult Population")
plotData(fawn_count, precipitation, "Fawn Count vs. Precipitation")
plotData(fawn_count, winter_severity, "Fawn Count vs. Winter Severity")
plotData(adult_population, precipitation, "Adult Population vs Precipitation")
plotData(adult_population, winter_severity, "Adult Population vs. Winter Severity")
plotData(precipitation, winter_severity, "Precipitation vs. Winter Severity")

# Create padding
ones = np.ones(8)

# Precipitation vs. Fawn Count
X = np.column_stack((precipitation, ones))
Y = fawn_count
calculateValues(X, Y)

# Precipitation vs. Adult Population
X = np.column_stack((precipitation, ones))
Y = adult_population
calculateValues(X, Y)

# How weather affects fawn count
X = np.column_stack((winter_severity, precipitation, ones))
Y = fawn_count
calculateValues(X, Y)

# How weather affects adult population
X = np.column_stack((winter_severity, precipitation, ones))
Y = adult_population
calculateValues(X, Y)

# How weather and adult population affects fawn count
X = np.column_stack((winter_severity, precipitation, adult_population, ones))
Y = fawn_count
calculateValues(X, Y)