# Note that with polynomials
# y = ax^2 + bx + c
# Even though x is used twice, there is still only one feature
# so linear regression works as this isn't a 3D function

import numpy as np
import matplotlib.pyplot as plt

# Prepare to load data
X = []
Y = []

# Load the Data
for line in open('data/data_poly.csv'):
	x, y = line.split(",")
	x = float(x)
	X.append([1, x, x*x]) # Turn this into a polynomial
	Y.append(float(y))

# Convert to Numpy Array
X = np.array(X)
Y = np.array(Y)

# Plot data
plt.scatter(X[:, 1], Y)
plt.show()

# Calculate the weights
w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))

# Calculate the Predictions
Y_hat = X.dot(w)

# Calculate the R^2
d1 = Y - Y_hat
d2 = Y - Y.mean()
r2 = 1 - (d1.dot(d1) / d2.dot(d2))
print("The R2 value is:", r2)

# Plot the data
plt.scatter(X[:,1], Y)
plt.plot(sorted(X[:,1]), sorted(Y_hat))
plt.show()