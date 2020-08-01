# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:34:20 2020

@author: Krish Naik
"""

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='Playing Card Prediction Vgg16.h5'

# Load your trained model
model = load_model(MODEL_PATH)




def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    image = image/255.
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    preds=np.argmax(model.predict(image), axis=1)

    if preds==0:
        preds="The Card is Ten of Clubs"
    elif preds==1:
        preds="The Card is Two of Clubs"
    elif preds==2:
        preds="The Card is Three of Clubs"
    elif preds==3:
        preds="The Card is Four of Clubs"
    elif preds==4:
        preds="The Card is Five of Clubs"
    elif preds==5:
        preds="The Card is Six of Clubs"
    elif preds==6:
        preds="The Card is Seven of Clubs"
    elif preds==7:
        preds="The Card is Eight of Clubs"
    elif preds==8:
        preds="The Card is Nine of Clubs"
    elif preds==9:
        preds="The Card is Ace of Clubs"
    elif preds==10:
        preds="The Card is Jack of CLubs "
    elif preds==11:
        preds="The Card is King of Clubs"
    elif preds==12:
        preds="The Card is Queen of Clubs"
    elif preds==13:
        preds="The Card is Ten of Diamond"
    elif preds==14:
        preds="The Card is Two of Diamond"
    elif preds==15:
        preds="The Card is Theee of Diamond"
    elif preds==16:
        preds="The Card is Four of Diamond"
    elif preds==17:
        preds="The Card is Five of Diamond"
    elif preds==18:
        preds="The Card is Six of Diamond"
    elif preds==19:
        preds="The Card is Seven of Diamond"
    elif preds==20:
        preds="The Card is Eight of Diamond"
    elif preds==21:
        preds="The Card is Nine of Diamond"
    elif preds==22:
        preds="The Card is Ace of Diamond"
    elif preds==23:
        preds="The Card is Jack of Diamond"
    elif preds==24:
        preds="The Card is King of Diamond"
    elif preds==25:
        preds="The Card is Queen of Diamond"
    elif preds==26:
        preds="The Card is Ten of Hearts"
    elif preds==27:
        preds="The Card is Two of Hearts"
    elif preds==28:
        preds="The Card is Three of Hearts"
    elif preds==29:
        preds="The Card is Four of Hearts"
    elif preds==30:
        preds="The Card is Five of Hearts"
    elif preds==31:
        preds="The Card is Six of Hearts"
    elif preds==32:
        preds="The Card is Seven of Hearts"
    elif preds==33:
        preds="The Card is Eight of Hearts"
    elif preds==34:
        preds="The Card is Nine of Hearts"
    elif preds==35:
        preds="The Card is Ace of Hearts"
    elif preds==36:
        preds="The Card is Jack of Hearts"
    elif preds==37:
        preds="The Card is King of Hearts"
    elif preds==38:
        preds="The Card is Queen of Hearts"
    elif preds==39:
        preds="The Card is Ten of Spades"
    elif preds==40:
        preds="The Card is Two of Spades"
    elif preds==41:
        preds="The Card is Three of Spades"
    elif preds==42:
        preds="The Card is Four of Spades"
    elif preds==43:
        preds="The Card is Five of Spades"
    elif preds==44:
        preds="The Card is Six of Spades"
    elif preds==45:
        preds="The Card is Seven of Spades"
    elif preds==46:
        preds="The Card is Eight of Spades"
    elif preds==47:
        preds="The Card is Nine of Spades"
    elif preds==48:
        preds="The Card is Ace of Spades"
    elif preds==49:
        preds="The Card is Jack of Spades"
    elif preds==50:
        preds="The Card is King of Spades"
    else:
        preds="The Card is Queen of Spades"


    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)
