#!/usr/bin/env python3
#By Luke Taylor and Azmeena Bandeali

import pandas as pd
#from sklearn.model_selection import cross_val_score
from sklearn import cross_validation
import sklearn.tree
import sklearn.ensemble
import sys

if(len(sys.argv) < 2):
	print("Error: Not enough args.")
	print("Usage: thesis_analysis.py filename")
	exit(1)

df = pd.read_csv(sys.argv[1])
x = df.drop(['time'], axis=1)
y = df['time']
x_train,x_test,y_train,y_test = cross_validation.train_test_split(x,y,test_size = 0.1, random_state=127)
for cr in [25,50,75,100,150,200]:
    #regressor = sklearn.tree.DecisionTreeRegressor(criterion='mae', max_depth=cr, random_state=127)
    regressor = sklearn.ensemble.AdaBoostRegressor(n_estimators=100, random_state=127)
    regressor.fit(x_train, y_train)
    R2 = regressor.score(x_test, y_test)
    print(R2)
    #scores = cross_val_score(regressor, df.drop(['time'], axis=1), df['time'], cv=10, scoring='neg_mean_squared_error')
    #print("%s: %.2f %.2f" % (cr, scores.mean(), scores.std()))
#regressor = sklearn.tree.DecisionTreeRegressor(criterion='mse', max_depth=4, random_state=127)
#regressor.fit(df.drop(['time'],axis=1), df['time'])
#print(regressor.predict([[8,8,8,8,False,8]]))

