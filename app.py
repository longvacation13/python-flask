# https://python-explorer.tistory.com/13
from flask import Flask
app = Flask(__name__) 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# print("hello world")

@app.route('/')
def hello_world(): 
 
 return "Hello Python!"
 
if __name__ == '__main__': 
 app.run() 
 

