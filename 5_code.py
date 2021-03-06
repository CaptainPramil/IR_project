# -*- coding: utf-8 -*-
"""5_Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15h9mfQY7u7W1AbsbDujhkeZBggsQSNfh
"""

from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

import pandas as pd
a1= pd.read_csv('features_positive.csv')
b1= pd.read_csv('features_negative.csv')
print(b1)

#f=pd.concat([a1, b1], axis=1)
a2=pd.read_csv('s1.p.csv')
#print(a2)
b2=pd.read_csv('s1n.csv')
#a=pd.concat([a1,a2],axis=0)
a=a1.merge(a2,on='userid')
b=b1.merge(b2,on='userid')
f=pd.concat([a, b], axis=0)
print(f)

f=f.drop('emoji',axis=1)
f=f.drop('tweet',axis=1)
f=f.drop('userid',axis=1)
f=f.drop('source',axis=1)
f=f.drop('time',axis=1)
print(f)

import numpy as np
X=np.array(f)
print(X)


'''
f1=a1[['+ve_emo_wrdcount','-ve_emo_wrdcount','first_person_plu', 'num_emoji','first_person_sing']]
#f1.head()
f1=np.array(f1)

#print(len(f1))
f2=b1[['+ve_emo_wrdcount','-ve_emo_wrdcount','first_person_plu', 'num_emoji','first_person_sing']]
f2=np.array(f2)
X=np.append(f1,f2,axis=0)
'''

k1=[0]*502
k1=np.array(k1)
k2=[1]*500
k2=np.array(k2)
y=np.append(k1,k2,axis=0)
#print(y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.2,random_state=42)
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix 
model = GaussianNB()
model.fit(X_train,y_train)
print(model.score(X_test,y_test))

#print(y_test)
#m1=model.predict(X_test)

#from sklearn.metrics import confusion_matrix 
#confusion_matrix(y_test,m1)

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
classifier.fit(X_train, y_train)
print(classifier.score(X_test,y_test))

#output=pd.merge(a1, b1,on='userid')
#print(a1)
#print(output)
#df.head()
#df.head()
#inputs = df.drop('num_emoji',axis='columns')
#target = df.num_emoji	
#df = df.reset_index()

#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.3)
#from sklearn.naive_bayes import GaussianNB
#from sklearn.metrics import confusion_matrix 
#model = GaussianNB()
#model.fit(X_train,y_train)
#print(model.score(X_test,y_test))
#print(y_test)
#m1=model.predict(X_test)
#from sklearn.metrics import confusion_matrix 
#confusion_matrix(y_test,m1)

from sklearn.metrics import f1_score
ypred1=classifier.predict(X_test)
ypred2=model.predict(X_test)
ypred3=clf.predict(X_test)
print(f1_score(ypred1,y_test))
print(f1_score(ypred2,y_test))
print(f1_score(ypred3,y_test))

from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))