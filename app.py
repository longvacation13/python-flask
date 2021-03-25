# https://python-explorer.tistory.com/13
from flask import Flask, request
app = Flask(__name__) 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os
import firebase_admin 
from firebase import Firebase
from firebase_admin import credentials

cred = credentials.Certificate("heroku-pro-firebase-adminsdk-na1xm-9e49a017fd.json")
config = {
    apiKey: "AIzaSyA-fI8Z3W136-PAcGvc0GUFXGonoTpxmL4",
    authDomain: "heroku-project-75f3a.firebaseapp.com",
    databaseURL: "https://heroku-project-75f3a-default-rtdb.firebaseio.com",
    projectId: "heroku-project-75f3a",
    storageBucket: "heroku-project-75f3a.appspot.com",
    messagingSenderId: "751329215750",
    appId: "1:751329215750:web:69fd3dd5dbf1209ac4ca87",
    measurementId: "G-H9V97HWFRQ"
}
# firebase_admin.initialize_app(cred)
firebase = Firebase(config)


@app.route('/')
def hello_world(): 
 print(os.getcwd)
 return "hello python!"
 
if __name__ == '__main__': 
 app.run() 
 

