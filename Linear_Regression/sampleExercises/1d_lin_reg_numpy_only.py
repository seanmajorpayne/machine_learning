import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the Data
df = pd.read_csv('data/data_1d.csv', header=None)

X = df[0].to_numpy()
Y = df[1].to_numpy()

# One way to calculate is by using the equations for a and b
# and dividing by N on both sides
def oneWayToCalculate(X, Y):
	denom = X.dot(X) - X.mean() * X.sum()
	a = (X.dot(Y) - Y.mean() * X.sum()) / denom
	b = (Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / denom
	return a, b

# The other way to calculate is by using the equations for a and b
# and dividing by N^2 on both sides.
def anotherWayToCalculate(X, Y):
	denom = np.mean(X**2) - np.mean(X)**2
	a = (np.mean(X*Y) - np.mean(X) * np.mean(Y)) / denom
	b = (np.mean(Y) * np.mean(X**2) - np.mean(X) * np.mean(X*Y)) / denom
	return a,b

# Plot a scatter plot with the line of best fit
def plotResults(X, Y, Y_hat):
	plt.scatter(X, Y)
	plt.plot(X, Y_hat)
	plt.show()

def calculateRSquared(Y, Y_hat):
	d1 = Y - Y_hat
	d2 = Y - Y.mean()
	r2 = 1 - (d1.dot(d1) / d2.dot(d2))
	return r2

# Calculate and plot the first example
a, b = oneWayToCalculate(X, Y)
Y_hat = a*X + b
plotResults(X, Y, Y_hat)
r2 = calculateRSquared(Y, Y_hat)
print(r2)

print("The R2 value for the first method is:", r2)

# Calculate and plot the second example
a, b = anotherWayToCalculate(X, Y)
Y_hat = a*X + b
plotResults(X, Y, Y_hat)
r2 = calculateRSquared(Y, Y_hat)
print(r2)

print("The R2 value for the second method is:", r2)