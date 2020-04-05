#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

base = pd.read_csv('dataset.csv')
base.isna().sum()
base.head()

base.head()
base['Admitted'] = [1 if chance > 0.8 else 0 for chance in base['Chance of Admit ']]
base.head()


labels = ['Yes', 'No']
x_pos = [0, 1]

admitted = len(base[base['Admitted'] == 1])
not_admitted = len(base[base['Admitted'] == 0])

plt.bar(x_pos, [admitted, not_admitted])
plt.xticks(x_pos, labels)
plt.title('Admitted students')


toefl = base.iloc[:, 2].values
gre   = base.iloc[:, 1].values
cgpa  = base.iloc[:, 6].values


x = pd.DataFrame(np.c_[toefl, gre, cgpa], columns=['toefl','gre', 'cgpa'])
y = base.iloc[:, -1].values



X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.20, random_state=42)

logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)

cnf_matrix = metrics.confusion_matrix(y_test, predictions)
sns.heatmap(cnf_matrix, annot=True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

print(metrics.classification_report(y_test, predictions))

print("Accuracy: ", metrics.accuracy_score(y_test, predictions))
print("Precision: ", metrics.precision_score(y_test, predictions))
print("Recall: ", metrics.recall_score(y_test, predictions))
