from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(_name_)
model = joblib.load("model.pkl")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
        height  = request.form["height"]
        height = int(height)
        print(height)
        weight = model.predict([[height]])

        return render_template('index.html', 
                        prediction_text="Weight = {}".format(weight))
    
if _name_ == "_main_":
    app.run()