# -*- coding: utf-8 -*-
"""LR_task_6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kBFC6fOLiRx8jnUoy3mBRP0lNeuBSBdZ
"""

import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

data = np.loadtxt('data_multivar_nb.txt', delimiter=',')
X, y = data[:, :-1], data[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

svm_classifier = svm.SVC(kernel='linear', C=1)
svm_classifier.fit(X_train, y_train)

y_pred = svm_classifier.predict(X_test)

print('Accuracy SVM:', accuracy_score(y_test, y_pred))
print('Recall SVM:', recall_score(y_test, y_pred, average='weighted'))
print('Precision SVM:', precision_score(y_test, y_pred, average='weighted'))
print('F1 Score SVM:', f1_score(y_test, y_pred, average='weighted'))