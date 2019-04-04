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

if __name__ == "__main__":
    app.run(debug=True)