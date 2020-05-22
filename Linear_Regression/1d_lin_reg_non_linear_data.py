import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create empty arrays to store data
X = []
Y = []

# The file has a number of strange characters that need to be removed
non_decimal = re.compile(r'[^\d]+')

for line in open('data/moore.csv'):
	d = line.split('\t')
	x = int(non_decimal.sub('', d[2].split('[')[0]))
	y = int(non_decimal.sub('', d[1].split('[')[0]))
	X.append(x)
	Y.append(y)

X = np.array(X)
Y = np.array(Y)
Y = np.log(Y)

def getAandB(X, Y):
	denom = X.dot(X) - X.mean() * X.sum()
	a = (X.dot(Y) - Y.mean() * X.sum()) / denom
	b = (Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / denom
	return a, b

def calculateRSquared(Y, Y_hat):
	d1 = Y - Y_hat
	d2 = Y - Y.mean()
	r2 = 1 - (d1.dot(d1) / d2.dot(d2))
	print("The R2 Value is:", r2)
	return r2

def plotPredictionLine(X, Y, Y_hat):
	plt.scatter(X, Y)
	plt.plot(X, Y_hat)
	plt.show()

a, b = getAandB(X, Y)
Y_hat = a*X + b
r2 = calculateRSquared(Y, Y_hat)
plotPredictionLine(X, Y, Y_hat)
print("time to double:", np.log(2)/a, "years")