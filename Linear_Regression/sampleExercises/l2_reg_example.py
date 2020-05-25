import numpy as np
import matplotlib.pyplot as plt

# This program demonstrates the effect of L2 Regularization
# through contrived sample data.

# Create sample data
N = 25
X = np.linspace(0, 20, N)
Y = 0.5*X + np.random.randn()

X = np.vstack([np.ones(N), X]).T

# Add outliers
Y[-1] = Y[-1] + 15
Y[-2] = Y[-2] + 10

# Plot X vs Y and the lines of best fit
# for standard regression vs L2 regression
def plotData(X, Y, Yhat, Yhat_l2):
	print(X.shape, Y.shape)
	plt.scatter(X, Y)
	plt.plot(X, Yhat, label="Yhat")
	plt.plot(X, Yhat_l2, label="Yhat with L2 Reg")
	plt.legend()
	plt.show()

# Fit without regularization and return prediction
# Takes an X matrix and Y vector
def standardFit(X, Y):
	w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
	Y_hat = X.dot(w)
	print(Y_hat)
	return Y_hat

# Fit with L2 Regularization and return prediction
# Takes an X matrix, Y vector, and D (# of X cols)
def fitWithL2Reg(X, Y, D):
	lamda = 1000
	identity = np.eye(D)
	w = np.linalg.solve(lamda * identity + X.T.dot(X), X.T.dot(Y))
	Y_hat = X.dot(w)
	return Y_hat

Yhat = standardFit(X, Y)
Yhat_l2 = fitWithL2Reg(X, Y, 2)
plotData(X[:, 1], Y, Yhat, Yhat_l2)