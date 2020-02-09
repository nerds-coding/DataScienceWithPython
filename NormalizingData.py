#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:37:23 2020

@author: anupprakash
"""


import pandas as pd 
from sklearn.ensemble import ExtraTreesClassifier

from sklearn.preprocessing import Normalizer

filename = "/Users/anupprakash/Downloads/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

array = data.values


# separate array into input and output components

X = array[:,0:8]
Y = array[:,8]
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)
# summarize transformed data
#set_printoptions(precision=3)
print(normalizedX[0:5,:])
 