# Sentiment Analysis

## Data Source

Data located here:
https://cs.jhu.edu/~mdredze/datasets/sentiment/index2.html

This data was provide by the following people and was originally used for research in
their paper listed below:

John Blitzer, Mark Dredze, Fernando Pereira. Biographies, Bollywood, Boom-boxes and Blenders: Domain Adaptation for Sentiment Classification. Association of Computational Linguistics (ACL), 2007. [PDF]

## Goal

This project served as my first introduction to NLP and applying a logistic regression
model using NLP. It also introduced me to the tools beautifulsoup and sklearn.



## Functionality
The program reads in a series of Amazon Reviews and analyzes the text to determine if 
reviews are positive or negative.

The words are processed to remove filler words (the, and, or) and punctuation is stripped.
The words are also lemmatized, which determines the lemma of the word 
(ex. studies, studying -> study) to reduce the size of our resulting matrix.

The words are assigned an index corresponding to rows in a matrix. Each row represents
a review. For every instance of the word in the review, the value is increased by 1. The
last value represents 0 (negative) or 1 (positive)

Example:
```
	w1,w2,w3     p/n
r1 [ 2, 3, 1,  ...0]
r2 [ 1, 0, 5, ....1]
```

These are then split up into train and test data and run through sklearn to score the
model. Without any special configuration, the training data is around an 85% accuracy
and the test is at 78%, which is fairly good for this purpose.