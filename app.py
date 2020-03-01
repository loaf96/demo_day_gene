import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy

import tensorflow as tf 
import json
import numpy as np
from tensorflow import keras as tfk
from tensorflow.keras import optimizers
import datetime
import os

from fields import TestField

tf.enable_eager_execution()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'JAHDHRJSHD'

# code below is for the purpose of ensuring that the user is directed towards
# the correct desired paage when navigating the site as well as some of the interactive
# capabilites of the site (i.e. 'output' page's function for producing the unit text)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/inspiration")
def zipf():
    """Render Home Page."""
    return render_template("inspiration.html")

@app.route("/about")
def about():
    """Render Home Page."""
    return render_template("about.html")

@app.route("/sidebyside")
def sidebyside():
    """Render Home Page."""
    return render_template("sidebyside.html")

@app.route("/input")
def input():
    """Render Home Page."""
    return render_template("input.html")


@app.route("/mission")
def mission():
    """Render Home Page."""
    return render_template("mission.html")

@app.route("/process")
def visual1():
    """Render Home Page."""
    return render_template("process.html")

@app.route("/data")
def data():
    """Render Home Page."""
    return render_template("data.html")

@app.route("/test")
def test():
    """Render Home Page."""
    return render_template("test.html")

@app.route("/models")
def models():
    """Render Home Page."""
    return render_template("models.html")

@app.route("/test2", methods=['GET', 'POST'])
def test2():
    form = TestField()
    if form.validate_on_submit():
        flash(f'Your Test Data is {form.testfield.data}!', 'success')
        return redirect('/')
    return render_template("test2.html", form=form)

@app.route("/output", methods=['POST'])
def output():

# the functions and variables below are for the purpose of creating the 'outline' of our
# model so when we load the weights in, it knows what it should do with them and how to use 
# them for making a predicition. 

    def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
        model = tf.keras.Sequential([\
                                    tf.keras.layers.Embedding(vocab_size, embedding_dim,\
                                                            batch_input_shape=[batch_size, None]),\
                                    tf.keras.layers.Dropout(0.2), \
                                    tf.keras.layers.LSTM(rnn_units,\
                                                        return_sequences=True,\
                                                        stateful=True,\
                                                        recurrent_initializer='glorot_uniform'
                                                        ),
                                    tf.keras.layers.Dropout(0.2),
                                    tf.keras.layers.Dense(vocab_size)
                                                        ])
        return model

# load in weights from Alice in Wonderland 

    type1 = request.form.get("type1")

    if type1 == "alice":
        
        sng_gud = pd.read_csv('lotsofwrds4.csv')
        sng_gud = [str(x) for x in sng_gud['0']]
        vocab = sorted(set(sng_gud))
        wrd_num = {u:i for i, u in enumerate(vocab)}
        num_wrd = np.array(vocab)
        sng_int = np.array([wrd_num[c] for c in sng_gud])

        vocab_size = len(vocab)
        embedding_dim = 128
        rnn_units = 512
        checkpoint_dir = 'training_cps_8_1_1000_128_512_50__1LSTM_glorot-uniform_alice001'

        label1 = "Alice in Wonderland"

# load in weights from Freud 

    elif type1 == "freud":

        sng_gud = pd.read_csv('lotsofwrds.csv')
        sng_gud = [str(x) for x in sng_gud['0']]
        vocab = sorted(set(sng_gud))
        wrd_num = {u:i for i, u in enumerate(vocab)}
        num_wrd = np.array(vocab)
        sng_int = np.array([wrd_num[c] for c in sng_gud])

        vocab_size = len(vocab)
        embedding_dim = 128
        rnn_units = 1024
        # checkpoint_dir = 'training_cps_8_1_1000_128_512_50__1LSTM_glorot-uniform_freud003'
        checkpoint_dir = 'training_cps_6_1_1000_128_1024_10__1GRU_glorot-uniform_freud10'
        label1 = "Freud - Dream Psychology"

# load in weights from lyric database

    elif type1 == "rap":

        sng_gud = pd.read_csv('lotsofwrds3.csv')
        sng_gud = [str(x) for x in sng_gud['0']]
        vocab = sorted(set(sng_gud))
        wrd_num = {u:i for i, u in enumerate(vocab)}
        num_wrd = np.array(vocab)
        sng_int = np.array([wrd_num[c] for c in sng_gud])

        vocab_size = len(vocab)
        embedding_dim = 128
        rnn_units = 512
        checkpoint_dir = 'training_cps_8_3_246361_128_512_50__1LSTM_glorot-uniform01_2020.02.19-004029'

        label1 = "Rap Lyrics"

# load in weights of fairytale database

    elif type1 == "grimm":
        
        sng_gud = pd.read_csv('lotsofwrds2.csv')
        sng_gud = [str(x) for x in sng_gud['0']]
        vocab = sorted(set(sng_gud))
        wrd_num = {u:i for i, u in enumerate(vocab)}
        num_wrd = np.array(vocab)
        sng_int = np.array([wrd_num[c] for c in sng_gud])

        vocab_size = len(vocab)
        embedding_dim = 128
        rnn_units = 512
        checkpoint_dir = 'training_cps_8_1_1000_128_512_10__1LSTM_glorot-uniform_grimm1'

        label1 = "Grimm's Fairy Tales"

    model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)
    model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
    model.build(tf.TensorShape([1, None]))

    temp = 1.0

# function below generates the text based off of the seed inputed, or a unique string without a seed. 

    def generate_text(model, start_string):
        num_generate = 60
        start_str = start_string.split(' ')
        input_eval = [wrd_num[s] for s in start_str]
        input_eval = tf.expand_dims(input_eval, 0)
        text_generated = []
        temperature = temp
        model.reset_states()
        for i in range(num_generate):
            predictions = model(input_eval)
            predictions = tf.squeeze(predictions, 0)
            predictions = predictions / temperature
            predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
            input_eval = tf.expand_dims([predicted_id], 0)
            text_generated.append(num_wrd[predicted_id])
        return (start_string + ' ' + ' '.join(text_generated))
    text1 = request.form.get("text1")
    try:
        lmno = generate_text(model, start_string=text1)
    except:
        lmno = "ERROR GENERATING TEXT, Try Using different words"
    return render_template("test.html", output=lmno, type1=label1)

if __name__ == '__main__':
    app.run(debug=True)
