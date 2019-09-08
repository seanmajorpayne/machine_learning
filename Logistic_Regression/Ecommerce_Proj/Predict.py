import numpy as np

from Process import get_binary_data

X, Y = get_binary_data()

N, D = X.shape[0], X.shape[1]

W = np.random.randn(D)
b = 0

def sigmoid(z):
	return 1 / (1 + np.exp(-z))

def forward(X, W, b):
	return sigmoid(X.dot(W) + b)
	
P_Y_given_X = forward(X, W, b)
predictions = np.round(P_Y_given_X)

def classification_rate(Y, P):
	return np.mean(Y == P)

c = classification_rate(Y, predictions)
print("Score:", c)
E = cross_entropy(Y, predictions)
print("Error:", E)
