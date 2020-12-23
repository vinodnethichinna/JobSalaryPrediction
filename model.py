# Random Forest Classifier with TF-IDF 

'''
This model predicts the salary based on Job Description using Classification models.
'''

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier

# Importing the dataset
req_data = pd.read_csv('Data_After_Binning.csv')

#defining target and features.
X = req_data['Job_Description']
y = req_data['Salary_BINS']

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)



#tfidverctorizer
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

#Fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(X_train) 
tfidf_test=tfidf_vectorizer.transform(X_test)

#Initialize a PassiveAggressiveClassifier

#pac=PassiveAggressiveClassifier(max_iter=50)
#pac.fit(tfidf_train,y_train)

rfc=RandomForestClassifier(n_estimators=5000, criterion='entropy', verbose=True, n_jobs=3)
rfc.fit(tfidf_train,y_train)

#Predict on the test set and calculate accuracy
y_pred=rfc.predict(tfidf_test)

#saving the vectorizer.
tfidf = tfidf_vectorizer
pickle.dump(tfidf, open('tfidf.pkl','wb'))

# Saving model using pickle
pickle.dump(rfc, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load( open('model.pkl','rb'))




