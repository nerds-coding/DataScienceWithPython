#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:45:03 2020

@author: anupprakash
"""






import pandas as pd 
from sklearn.ensemble import ExtraTreesClassifier

from sklearn.preprocessing import Normalizer

filename = "/Users/anupprakash/Downloads/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)


array = data.values
X = array[:,0:8]
Y = array[:,8]

# feature extraction


model = ExtraTreesClassifier()
model.fit(X, Y)
print(model.feature_importances_)