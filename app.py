import numpy as np
import pandas as pd
import pickle

from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #tfidverctorizer
    tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
    data = request.form.values()
    
    final_features = tfidf.transform(data)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The Job Description falls in the Following Salary Bin : {}'.format(output))

    
        
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls 
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
