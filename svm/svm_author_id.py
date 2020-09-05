#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from tools.email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]





#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score
#clf = svm.SVC(kernel='linear')
clf = svm.SVC(kernel='rbf', C=10000)
t0 = time()
clf.fit(features_train,labels_train)
print ("training time:", round(time()-t0, 3), "s")
t1 = time()
prediction = clf.predict(features_test)
ans1 = prediction[10]
ans2 = prediction[26]
ans3 = prediction[50]
count = 0
for predict in prediction:
    if predict == 1:
        count = count + 1
print(count)
print(ans1, ans2, ans3)
print ("prediction time:", round(time()-t1, 3), "s")
print('accuracy score: ', accuracy_score(labels_test, prediction))
#########################################################


