# importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request
from flask import Flask

app = Flask(__name__)

#model = pickle.load(open("model.pkl", "r"))


@app.route("/")
@app.route("/templates")
def home():
    return render_template('input_text.html')




# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 12)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/templates", methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form
        result = ValuePredictor(to_predict_list)

        if int(result) == 1:
            prediction = 'Probably fake'
        else:
            prediction = 'Probably true'

        return render_template('result.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)