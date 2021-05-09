# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:31:41 2020

@author: Hitesh
"""
import pandas as pd
import math
dataset = pd.read_csv(r'G:\Hitesh\Hitesh\TV from flipkart\TV.csv')

Data=dataset.iloc[:,1:]
data=dataset.iloc[:,1:]
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder = LabelEncoder()
Data.iloc[:,0]=labelencoder.fit_transform(Data.iloc[:,0])
Data.iloc[:,1]=labelencoder.fit_transform(Data.iloc[:,1])

x=Data.iloc[:,:-1]

col_transformer = ColumnTransformer(transformers=[('ohe', OneHotEncoder(), [0,1])],remainder='passthrough')

x= col_transformer.fit_transform(x)

from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
scaler_y = StandardScaler()
x=scaler_x.fit_transform(x)
y=scaler_y.fit_transform(Data.iloc[:,-1])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 1000, random_state = 0)
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

from sklearn.metrics import mean_absolute_error
print('RMSE is {}'.format(math.sqrt(mean_absolute_error(y_test, y_pred))))

def output(brand,hd,hdmi,rating,size,speaker,usb):
    topredict=[[brand,hd,hdmi,rating,size,speaker,usb]]
    temp=pd.DataFrame(topredict)
    temp=col_transformer.transform(temp).toarray()
    temp=scaler_x.transform(temp)
    y_pred = regressor.predict(temp)
    y_pred = scaler_y.inverse_transform(y_pred)
    return y_pred
