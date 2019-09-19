# Perceptron

- Linear binary classifier
- Originally designed for image recognition
- Famous for not being able to solve the XOR problem

## Theory

- Binary Classification
- Uses {-1, 1}

Similar to other linear classifiers

```
wTx + b
= 0 -> Falls directly on the line/hyperplane
> 0 -> Predict +1
< 0 -> Predict -1
prediction = sign(wTx + b)
```

## Training

Iterative procedure where the classification rate goes up (on average) for each epoch.

```
w = random vector (b = 0)
for epoch in xrange(max_epochs):
	get all currently misclassified examples
	if no misclassified examples -> break
	x, y = randomly select one misclassified example
	w = w + nyx // n = 1.0, 0.1, 0.001 etc (learning rate)
```

A line can be defined by its normal vector.
n = (a, b)

The bias term tells us where w intersects the x2 axis. Similar to logistic regression, 
the bias term can always be absorbed into w.

```
Initial: y = w0 + w1x1 + w2x2
New Model: y = w0x0 + w1x1 + w2x2, x0 = 1 (Column of zeros in matrix X)
```

### Training Illustration

If the angle between x & w < 90 degrees, wTx > 0, so target must be -1
Update then becomes w = w - x

If the angle between x & w > 90 degrees, wTx < 0, so target must be +1
Update then becomes w = w + x

Note that one correction will either classify x correctly, or step in the correct
direction.

## perceptron.py

There are three tests run in the perceptron.py file. One is currently commented out. Using
the MNIST data set, the perceptron is able to get a 100% accuracy. However, given the XOR
problem the perceptron guesses at only a 50% accuracy.

Additionally, the perceptron does not know when it can't solve a problem, so it uses all
1000 epochs to continually produce the same result.

## Perceptron Loss Function

The function is defined as:

```
L(y, yhat) = -Σy(wTx)1(y≠yhat)
1 (True) returns 1
1 (False) returns 0
```

Only incorrect sampes contribute to loss.
For misclassification, wTx and y must be of opposite signs, therefore L>=0.

If x is further from w, then the loss is larger.
- wTx = |w||x|cos(89.9) is almost 0, so the loss should be small

The algorithm implemented was...
Stochastic Gradient Descent
```
dL/dw = -Σyx1(y≠yhat)
```



