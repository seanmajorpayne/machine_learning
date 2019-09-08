import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression
from bs4 import BeautifulSoup

# Get data & store it

soup = BeautifulSoup(open("sorted_data_acl/electronics/negative.review", "r"), 'lxml')
negative_reviews = soup.find_all('review_text')
soup = BeautifulSoup(open("sorted_data_acl/electronics/positive.review", "r"), 'lxml')
positive_reviews = soup.find_all('review_text')

# Split up text into individual words for analysis. Remove punctuation, short words,
# filler words, and lemmatize the words so we don't count index different forms of the
# same word.

stop_words = set(stopwords.words('english'))
l = WordNetLemmatizer() 

def tokenizer(s):
	s = s.lower()
	tokens = word_tokenize(s)
	words = [l.lemmatize(word) for word in tokens 
			if word.isalpha() 
			and len(word) >= 3
			and not word in stop_words
		]
	return words

word_index = {}
current_index = 0
reviews = []
positive = []
negative = []

for review in negative_reviews:
	reviews.append(review.get_text())
	words = tokenizer(review.get_text())
	negative.append(words)
	for word in words:
		if word_index.get(word) == None:
			word_index[word] = current_index
			current_index += 1

for review in positive_reviews:
	reviews.append(review.get_text())
	words = tokenizer(review.get_text())
	positive.append(words)
	for word in words:
		if word_index.get(word) == None:
			word_index[word] = current_index
			current_index += 1

# Take a word list and turn it into a vector based on the indexes
def words_to_vector(words, label):
	x = np.zeros(len(word_index) + 1)	# Extra column is for the label
	for word in words:
		i = word_index[word]
		x[i] += 1
	x = x / x.sum()						# Normalize
	x[-1] = label
	return x

# Create our Matrix, size (N, D + 1) with labels in the last column
N = len(positive) + len(negative)
data = np.zeros((N, len(word_index) + 1))
i = 0

for word_list in positive:
	data[i,:] = words_to_vector(word_list, 1)
	i += 1

for word_list in negative:
	data[i,:] = words_to_vector(word_list, 0)
	i += 1

# Split our data into train and test sets for analysis
reviews, data = shuffle(reviews, data)

X = data[:,:-1]
Y = data[:,-1]

Xtrain = X[:1000,:]
Ytrain = Y[:1000]
Xtest = X[1000:,:]
Ytest = Y[1000:]

lr = LogisticRegression(solver='liblinear')
lr.fit(Xtrain, Ytrain)
print("Score for Training Sets:", lr.score(Xtrain, Ytrain))
print("Score for Test Sets:", lr.score(Xtest, Ytest))



		
	

	


	
	
