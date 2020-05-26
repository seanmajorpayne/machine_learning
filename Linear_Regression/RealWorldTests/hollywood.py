import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Hollywood Movies

The data (X1, X2, X3, X4) are for each movie
X1 = first year box office receipts/millions
X2 = total production costs/millions
X3 = total promotional costs/millions
X4 = total book sales/millions
"""

def normalizeData(X, D):
	for i in range(D):
		X[:, i] = X[:, i] / np.amax(X[:, i])
	return X

def plotData(X, Y, title):
	plt.scatter(X, Y)
	plt.title(title)
	plt.show()

def plot3D(X1, X2, Y):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(production_costs, promotion_costs, Y)
	plt.show()

def getWeights(X, Y):
	w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
	return w

def fit(X, w):
	return X.dot(w)

def calculateR2(Y, Yhat):
	d1 = Y - Yhat
	d2 = Y - np.mean(Y)
	r2 = 1 - (d1.dot(d1) / d2.dot(d2))
	return r2

def evaluateRelationship(X, Y):
	w = getWeights(X, Y)
	Yhat = fit(X, w)
	r2 = calculateR2(Y, Yhat)
	print("The R2 value is:", r2)

# Load Data
df = pd.read_excel('data/mlr04.xls')

# Convert to Numpy
X = df.values
N = X.shape[0]
D = X.shape[1]

X = normalizeData(X, D)

# Get the vectors
box_office_receipts = X[:, 0]
production_costs = X[:, 1]
promotion_costs = X[:, 2]
book_sales = X[:, 3]

# Padding
ones = np.ones(N)

# Production Costs vs. Box Office Receipts
plotData(production_costs, box_office_receipts, "Production Costs vs. Box Office Receipts")
X = np.column_stack((production_costs, ones))
Y = box_office_receipts
evaluateRelationship(X, Y)

# Promotional Costs vs. Box Office Receipts
plotData(promotion_costs, box_office_receipts, "Promotional Costs vs. Box Office Receipts")
X = np.column_stack((promotion_costs, ones))
Y = box_office_receipts
evaluateRelationship(X, Y)

# Book Sales vs. Box Office Receipts
plotData(book_sales, box_office_receipts, "Book Sales vs. Box Office Receipts")
X = np.column_stack((book_sales, ones))
Y = box_office_receipts
evaluateRelationship(X, Y)

# Production Costs vs. Promotional Costs
plotData(production_costs, promotion_costs, "Production Costs vs. Promotional Costs")
X = np.column_stack((production_costs, ones))
Y = promotion_costs
evaluateRelationship(X, Y)

# Production Costs & Promotional Costs vs. Box Office Receipts
X = np.column_stack((production_costs, promotion_costs, ones))
Y = box_office_receipts
plot3D(production_costs, promotion_costs, box_office_receipts)
evaluateRelationship(X, Y)

