import matplotlib
from textblob import TextBlob
import re
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score, f1_score, roc_curve, auc
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize, WhitespaceTokenizer, TweetTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Set up random seed, for reproductability of randomness
np.random.seed(18)

# Import dataset
df1 = pd.read_csv('train.csv')

# Eyeball dataset, decision to select only columns "text" and "label"
print(df1.head())
print(df1.keys())
df1 = df1[['text', 'label']]

# Getting rid of empty lines
df1 = df1[df1.text.isna() == False]
length_df1 = len(df1)
#print(length_df1)

# Build sublist of original df1, contains 3000 lines picked at random
random_indexes = list(np.random.choice(length_df1-2, 3000, replace=False))
#print(random_indexes)
df1 = df1.iloc[random_indexes]
