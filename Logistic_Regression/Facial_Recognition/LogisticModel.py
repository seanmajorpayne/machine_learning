import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from util import get_binary_data, error_rate, sigmoid_cost, sigmoid

class LogisticModel:

	def __init__(self):
		pass
	
	# Calculates the sigmoid function for the matrix, weights, and bias term
	def forward(self, X):
		return sigmoid(X.dot(self.W) + self.b)
	
	# Predicts facial expressions based on a matrix X
	def predict(self, X):
		pY = self.forward(X)
		return np.round(pY)
	
	# Fits the model to the training data
	def fit(self, X, Y, learning_rate=10e-7, reg=0, epochs=120000, show_fig=False):
		X, Y = shuffle(X, Y)
		Xvalid, Yvalid = X[-1000:], Y[-1000:]
		X, Y = X[:-1000], Y[:-1000]
		
		N, D = X.shape
		self.W = np.random.randn(D) / np.sqrt(D)
		self.b = 0
		
		costs = []
		best_error = 1
		for i in range(epochs):
			pY = self.forward(X)
			self.W -= learning_rate * (X.T.dot(pY - Y) + reg*self.W)
			self.b -= learning_rate * ((pY - Y).sum() + reg*self.b)
			
			if i % 20 == 0:
				pYvalid = self.forward(Xvalid)
				c = sigmoid_cost(Yvalid, pYvalid)
				costs.append(c)
				error = error_rate(Yvalid, np.round(pYvalid))
				print("i:", i, "cost:", c, "error:", error)
				if error < best_error:
					best_error = error
		print("Best Validation Error:", best_error)
		
		if show_fig:
			plt.plot(costs)
			plt.show()
		
def main():
	X, Y = get_binary_data()
	
	X0 = X[Y==0, :]
	X1 = X[Y==1, :]
	X1 = np.repeat(X1, 9, axis=0)
	X = np.vstack([X0, X1])
	Y = np.array([0]*len(X0) + [1]*len(X1))
	
	model = LogisticModel()
	model.fit(X, Y, show_fig=True)
	model.score(X, Y)
	
if __name__ == '__main__':
	main()
			
			
		

