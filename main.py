import pickle
import numpy as np
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint

app=Flask(__name__ , static_folder='static')

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
  return render_template('predict.html')

@app.route('/about.html')
def about():
  return render_template('about.html')

@app.route('/facts.html')
def facts():
  return render_template('facts.html')

@app.route('/education.html')
def education():
  return render_template('education.html')

@app.route('/predict.html')
def predd():
  return render_template('predict.html')

@app.route('/predict.html',methods=['POST','GET'])
def predict():
  print(request.form)
  final=[]
  final.append(float(request.form["in1"]))
  final.append(float(request.form["in2"]))
  final.append(float(request.form["in3"]))
  final.append(float(request.form["in4"]))
  final.append(float(request.form["in5"]))
  final.append(float(request.form["in6"]))
  final.append(float(request.form["in7"]))
  final.append(0)
  final = [final]
  final = np.array(final)
  final[0][4]=final[0][4]/final[0][0]
  final[0][5]=final[0][5]/final[0][0]
  final[0][6]=final[0][6]/final[0][0]
  final[0][7]=(2*final[0][3])/(final[0][1]+final[0][2])
  from sklearn.preprocessing import PolynomialFeatures
  poly = PolynomialFeatures(degree = 2)
  final = poly.fit_transform(final)
  prediction=model.predict(final)
  out=prediction
  return render_template('predict.html',prediction_text='The Price of the Diamond is ${}'.format(out[0]))

                          
if __name__ == "__main__":
  app.run(debug=False)