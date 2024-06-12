# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:08:18 2024

@author: DELL
"""

import uvicorn #ASGI
from fastapi import FastAPI
from BankNote import BankNote
import numpy as np
import pandas  as pd
import pickle

app = FastAPI()

pickle_in = open("RFclassifier.pkl","rb")
rf = pickle.load(pickle_in)

@app.get('/')

def index():
    return {"Message","Hello, User"}

@app.get('/{name}')
def get_name(name: str):
    return {"Welcome to my project: ", f"Hello {name}"} 

@app.post('/predict')
def predict_type(data:BankNote):
    data = data.dict()
    print(data)
    variance = data["variance"]
    print(variance)
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    prediction = rf.predict([[variance,skewness,curtosis,entropy]])
    
    if prediction[0]>0.5:
        result = "Fake Note"
    else:
        result = "Real Authentic Note"
        
    return {
        'prediction' : result
    }

if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port = 8000)
    

