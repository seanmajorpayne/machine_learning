# Decision Trees

## Decision Tree Intuition

Decision Trees are easy to understand and very difficult to implement. The tree is easily
visualized as a nested series of if/else statements.

A simple example

```
if BMI > 25:
	if BP > 140:
		return "disease"
	else:
		return "no disease"
else:
	return "no disease"
```

There are two challenges when attempting to automate this process.

1. Mathematical - How do we find the optimal thresholds?
2. Programming - How do we build a model with arbitrary depth?

## Basics

On the surface, this doesn't sound like a machine learning model. The process of choosing
the conditions is how we make this an ML model and this is based on information theory.

We only look at one attribute ("input feature", 1 X column) at a time. 

## Geometry

Splits are always orthogonal to the axes when plotted. By splitting multiple times, we can
still end up with highly non-linear data.

## Recursive Model

Since we're working with a tree the model will be recursive.

A simple implementation example of a tree node.

```
Class TreeNode:
	Self.left_node
	Self.right_node
	Self.left_prediction
	Self.right_prediction
```

And simple example of making a prediction
```
def predict_one(x):
	if self.condition(x):
		if self.left_node:
			return self.left_node.predict_one(x)
		else:
			return self.left_prediction
	else:
		if self.right_node:
			return self.right_node.predict_one(x)
		else:
			return self.right_prediction
```

## Information Entropy

How do we choose the best splits in a decision tree?
We want to choose a split that maximizes the reduction in uncertainty.

When it comes to probability, a wide variance indicates that we don't know much about the
data we will get.

A small variance means we are more confident about our predictions.

```
Entropy = E[-log2(p)]
H(p) = -Σp(x)logp(x) --> Information Entropy Equation

p(X=1) = p
p(X=0) = 1 - p

H(p) = -plog(p) - (1-p)log(1-p)

Solve dH/dp = 0 for p

if p = 0.5:
	No way to make a good prediction, always 50% right, 50% wrong
if p = 0.8:
	Always predict 1 for the best chance of being correct
```

Entropy is a measure of how much information we get from finding out the value of a
random variable. It's best to flip a coin with p = 0.5, because we gain the maximum
amount of information from knowing the outcome. Prior to this, we knew nothing about
the value we'd get as a result.

- A uniform distribution yields maximum entropy.

## Maximizing information gain

How do we use information entropy to choose the best attributes for prediction?

One solution: ID3
- Find which column of X produces maximum information gain
- Split data based on this
- Remove it from our set of attributes and repeat on the split data

Another solution:
- Allow more than one split per attribute
- Red -> Green -> Back to Red
- Allows us to split at a threshold, rather than separate all values

If we have a dataset with an attribute that perfectly splits data into two classifiers,
we would want to start there. That ensures that our information gain is >= 0.

In practice, this will rarely be the case, so we'll need to calculate our Entropy/Information
Gain.

### Fit Function

```
Def fit(X, Y):
	Best_IG = 0
	Best_attribute = None
	For c in columns:
		Condition = find_split(X, Y, c)
		Y_left = Y[X[c] meets condition]
		Y_right = Y[X[c] does not meet condition]
		information_gain = H(Y) - p(left)H(Y_left) - p(right)H(Y_right)
		if information_gain > best_IG:
			best_IG = information_gain
			Best_attribute = c

	...
	
	# Once we find the best attribute to split on
	X_left, Y_left, X_right, Y_right = split by best_attribute
	Self.left_node = TreeNode()
	Self.left_node.fit(X_left, Y_left)
	Self.right_node = TreeNode()
	Self.right_node.fit(X_right, Y_right) 
```

### Base Cases

1. If max information gain = 0, make it a leaf node and select the most likely class
2. If we hit max depth, stop recursing and make a leaf node.
	- We need to avoid overfitting. 
	- It's easy to achieve 100% on training sets with a tree of arbitrary depth.
3. If there is only 1 sample, predict the sample's label
4. If >1 sample, but they all have the same label, predict the label

## Choosing the best split

With discrete values, we can split fairly easily, but what about with continuous? Continuous
values give us an infinite number of places to split.

We only need to consider the midpoint of two values in a sorted set X. Our entropy will
not change.

### Algorithm

1. Sort X in column order, sort Y to correspond with X
2. Find boundary points where Y changes values
3. Calculate the information gain at these boundary points
4. Choose the split of maximum information gain







