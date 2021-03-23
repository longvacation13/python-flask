# https://python-explorer.tistory.com/13
from flask import Flask, request
app = Flask(__name__) 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os
import firebase_admin 
from firebase_admin import credentials

cred = credentials.Certificate("heroku-pro-firebase-adminsdk-na1xm-9e49a017fd.json")
firebase_admin.initialize_app(cred)


@app.route('/')
def hello_world(): 
 print(os.getcwd)
 return "hello python!"
 
if __name__ == '__main__': 
 app.run() 
 

