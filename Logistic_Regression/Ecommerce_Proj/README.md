# Ecommerce Project

## Introduction

This is a very simple example of implementing a logistic regression model
on some ecommerce data.

This is an intro project of a logistic regression course by thelazyprogrammer.

## What is my Goal?

My goal was to learn more about how logistic regression models work, including both theory
and computation. This project required the use of normalization, one hot encoding, linear
regression models, gradient descent, and weight training.

## Theory

All of the required theory can be seen in the main logistic regression folder. I have
the math and derivations there.

## Process of Development

In order to maximize my knowledge of the material I went through a methodical process to
study & code. Here are the steps I went through for each project & file.

1. Studied the theory
2. Performed the math calculations on paper, including all derivations
3. Coded the solutions

If I ran into issues or obstacles I couldn't figure out, I would do the following:

1. Peek at the instructor's code to determine the next step
2. Attempt to implement it myself
3. If unable to do so, copy the code & research any lines I didn't understand

** After the course was over recoded the entire program from memory. If I didn't know what,
how, and why I was doing something, I would repeat the entire process above until I understood
it from front to back without assistance. **

## CSV Data Interpretation

The CSV file contains the following columns. Here is how to interpret the data.

```
Is_mobile (0/1)
N_products_viewed (int >= 0)
Visit_duration (real # >= 0)
Is_returning_visitor (0/1)
Time_of_day(0/1/2/3 = 24h split into 4 categories)
User_action(bounce / add_to_cart / begin_checkout / finish_checkout)
```

We use categories for time of day, because we are assuming that users will generally
act the same during certain periods of time (ex. at work) rather than by exact hour.

We want to be able to predict user action.

## Process.py

This file is used to process & format the CSV data. During this process, I learned to
take a CSV & format it for logistic regression. This included the use of normalization
and one-hot encoding.

```
get_data() - Returns a Matrix X (inputs) and a Vector Y (outputs)
get_binary_data() - Returns the same data, but only when Y==0 or Y==1 which correspond
to the user bouncing or adding a product to their cart. This is done to make our data
easier to interpret for logistic regression.
normalize() - Normalizes a column of data using the format data - data.mean / standard dev
```

## Predict.py

This file is not used for an accurate prediction, but demonstrates that if we choose our
weights randomly, our prediction will not (consistently) be accurate. This program gave me
a simple introduction to implementing a sigmoid function & determining the classification
rate of the data.

## logistic_train.py

This file is the full implementation of the logistic regression model with gradient
descent. This code project focused on splitting data into train and test sets, calculating
cross entropy error, and applying a gradient descent to calculate the optimal weights and
bias term.


