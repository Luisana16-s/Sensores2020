# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:32:30 2020

@author: Usuario
"""
import pyodbc as p
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split# dividimos la BD en 70 - 30
from sklearn import preprocessing 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report#CALCULA DIFERENTES MÉTRICAS, PRECISION, F1 SCORE ETC
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC# nos permite SVM
conn=p.connect('Driver={ODBC Driver 17 for SQL Server};'
               'SERVER=servidorlib-16.database.windows.net;'
               'DATABASE=Libros;'
               'UID=Luisa;'
               'PWD=300836Luchis;'
               'Trusted_Connection=no;')
cursor=conn.cursor()
g=pd.read_sql_query("select *from Libros.dbo.matrizD",con=conn)
conn.commit()
B=g.to_numpy()
X=B[:,0:257]
y=B[:,-1]
m,n = X.shape
y= y.reshape((m,1))
X_train, X_test, Y_train, Y_test = train_test_split(X,y,test_size=0.3,random_state=42)
modelo = SVC(kernel='linear')
modelo.fit(X_train, Y_train)
predicciones = modelo.predict(X_test)
AccActual = accuracy_score(Y_test,predicciones)
json_response = json.dumps(classification_report(Y_test, predicciones),indent=2)