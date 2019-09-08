import numpy as np
import pandas as pd

from sklearn.utils import shuffle
from Process import get_binary_data

X, Y = get_binary_data()
X, Y = shuffle(X, Y)		# Make sure test sets don't have the same targets

# Split data into train and test sets
Xtrain = X[:-100]
Ytrain = Y[:-100]
Xtest = X[-100:]
Ytest = Y[-100:]

# Random weights to begin
D = X.shape[1]
W = np.random.randn(D)
b = 0

# Returns a decimal between 0 & 1
def sigmoid(z):
	return 1 / (1 + np.exp(-z))

# Returns predictions based off a matrix, the weights, and the bias term
def forward(X, W, b):
	return sigmoid(X.dot(W) + b)

# Returns a decimal between 0 and 1
def classification_rate(Y, P):
	return np.mean(Y == P)

# Returns the error rate
def cross_entropy(Y, P):
	return -np.mean(Y * np.log(P) + (1 - Y) * np.log(1 - P))

train_costs = []
test_costs = []
learning_rate = .001	# Arbitrary value set based on experimentation

# Configure our optimal weights & bias term using gradient descent
for i in range(10000):
	pYtrain = forward(Xtrain, W, b)
	pYtest = forward(Xtest, W, b)
	
	ctrain = cross_entropy(Ytrain, pYtrain)
	ctest = cross_entropy(Ytest, pYtest)
	train_costs.append(ctrain)
	test_costs.append(ctest)
	
	W -= learning_rate * Xtrain.T.dot(pYtrain - Ytrain)
	b -= learning_rate * (pYtrain - Ytrain).sum()
	if i % 1000 == 0:
		print(i, ctrain, ctest)

# Print the End Results
print("Final Train Classification Rate:", classification_rate(Ytrain, np.round(pYtrain)))
print("Final Test Classification Rate:", classification_rate(Ytest, np.round(pYtest)))

