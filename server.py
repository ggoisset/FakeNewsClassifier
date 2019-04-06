from flask import Flask, render_template, request
import pickle
import pandas as pd
import re


# Used by bow pickle file
def clean_article(article):
    art = re.sub("[^A-Za-z0-9' ]", '', str(article))
    art2 = re.sub("[( ' )(' )( ')]", ' ', str(art))
    art3 = re.sub("\s[A-Za-z]\s", ' ', str(art2))
    return art3.lower()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('input_text.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form['article_box']
        result = [result]
        result = bow.transform(result)
        result = pd.DataFrame(result.toarray())
        result.columns = bow.get_feature_names()

        prediction_array = model.predict(result)

        if prediction_array[0] == 0:
            print("It is probably real")
            result_message = "It is probably real"
        else:
            print("It is probably fake")
            result_message = "It is probably fake"

        return render_template("result.html", result=result_message)


if __name__ == '__main__':
    # Import models: clean article, bag of words, classifier
    bow = pickle.load(open("bow.pkl", "rb"))
    model = pickle.load(open("model.pkl", "rb"))

    app.run(debug=True)
