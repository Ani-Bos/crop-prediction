import os
import sys

import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD, Adam
from keras.utils.np_utils import to_categorical
# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect


# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Some utilites
import numpy as np


from sklearn.metrics import classification_report, confusion_matrix


# Declare a flask app
app = Flask(__name__)

# model=pickle.load(open('model.pkl','rb'))
print('Model loaded. Check http://127.0.0.1:5000/')


# Model saved with Keras model.save()
MODEL_PATH = 'model/my_model.h5'
model=load_model(MODEL_PATH)
model.make_predict_function()         # Necessary
print('Model loaded. Start serving...')

# def model_predict(data, model):
  
@app.route('/')
def hello_world():
    return render_template("index.html");
@app.route('/predictor')
def hello():
    return render_template("predictor.html");
@app.route('/contact')
def hellos():
    return render_template("contact.html");
# @app.route('/')
# def hello_world():
#     return render_template("index.html");

# def model_predict(img, model):
#     img = img.resize((224, 224))

#     # Preprocessing the image
#     x = image.img_to_array(img)
#     # x = np.true_divide(x, 255)
#     x = np.expand_dims(x, axis=0)

#     # Be careful how your trained model deals with the input
#     # otherwise, it won't make correct prediction!
#     x = preprocess_input(x, mode='tf')

#     preds = model.predict(x)
#     return preds

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == "POST":
        inputvalues=[int(x) for x in request.form.values()]
        final=np.array(inputvalues)
        print(type(final), final.shape)
        print("input",inputvalues);
        print(final)
        prediction = model.predict(np.array([24, 5, 2, 90]))
        print(prediction)
        

if __name__ == '__main__':
    app.run(debug=True)