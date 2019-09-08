# Logistic Regression

## What is it?

Logistic regression despite it's name, is actually a supervised classification model in
machine learning. Put simply, this means we are trying to predict categories from a
series of inputs and we have existing training data to work with.

### Relation to a Neuron

Similar to a neuron in the brian, logistic regression shares the following characteristics:

1. Many inputs -> One output
2. Spike or no spike -> 0/1 output
3. Synapse strengths -> Linear Weights

### Theory

The output of logistic regression is computed using a sigmoid function. This is a function
with a finite limit as x approaches infinity and a finite limit as x approaches negative
infinity.

While there are multiple sigmoid functions, the equation we use is the following:


This gives us a value between 0 and 1 as a result, with a y-int of 0.5. This is useful
for probability because we can directly interpret that as a percentage likelihood and
round it to get a prediction. Anything above 0.5 gives us class 1, anything below gives
us class 0.

The sigmoid function in code:

```
def sigmoid(z):
	return 1 / (1 + np.exp(-z))

# X = Inputs, W = weights, b = bias term
def forward(X, W, b):
	return sigmoid (X.dot(W) + b)
```

### Interpretation of Output

We can interpret the output as the probability that y belongs to class 1.
p(y = 1 | x) = σ(wTx) ∈ (0, 1)

It should be fairly intuitive that if we round this output, we will predict the class.
(Ex. an output of .6 is a 60% probability of class 1, so we should round .6 to 1)
```
Predict round(p(y = 1) | x)
```

### Similarity to Linear Regression

It's also intuitive that our model is similar to linear regression.

Logistic: y = σ(wTx)
Linear: y = wTx

In very simple scenarios, we can interpret the weights similarly, but once the models
become more complicated (i.e. neural networks) this is no longer the case.

## Training Weights

### Closed form solution to the Bayes Classifier

To be completed

### Cross Entropy Error Function - Theory

J = -{ tlog(y) + (1-t)log(1-y) }
t = target
y = output of logistic regression

Note that if t = 1, only the first term matters. Whereas if t = 0, only the second term
matters.

We want to do this for all of our data simultaneously

J = -Σ tlog(y) + (1-t)log(1-y)

In code (Inefficient version)
```
# T = Targets
# Y = Predictions
def cross_entropy(T, Y):
	E = 0
	for i in range(N):
		if T[i] == 1:
			E -= np.log(Y[i])
		else:
			E -= np.log(1 - Y[i])
	return E
```
In code (Simpler Version)

```
# Y = Targets
# P = Predictions
def cross_entropy(Y, P):
	return -np.mean(Y * np.log(P) + (1 - Y) * np.log(1 - P))
```

### Maximizing the likelihood

P(y = 1 | x) = σ(wTx)
Likeilhood = π y^t(1 - y)^(1-t)
log(Likelihood) = Σ tlog(y) + (1-t)log(1-y)

Since the log(Likelihood) is the opposite of the Cross Entropy Error, Maximizing the
likelihood is the same as minimizing the cross entropy error.

### Updating weights using gradient descent

Idea: Take small steps in the direction of the derivative of the error function.

This is more difficult than linear regression, as it requires us to split the error
into three partial derivatives.

Our result is:
∂J/∂w = Σ (y - t)x
Since aTb = Σab, we can rewrite this as:
∂J/∂w = XT(Y - T)

Note that the bias is when all x values are 1, so we can write this as Σ (y - t)

We can introduce the bias term as a column of 1s in X

In code:
```
# Learning rate is usually set through intuition/experimentation
# Iterations can stop when the change in the derviative becomes small
# w = weights, T = targets, Y = Predictions, X = inputs

learning_rate = 0.1
for i in range(100):
	w -= learning_rate * X.T.dot(pyTrain - Ytrain)
	b -= learning_rate * (pYtrain - Ytrain).sum()
```








