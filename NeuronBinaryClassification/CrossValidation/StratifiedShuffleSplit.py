from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd


perceptron = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')
X = perceptron.values[:, 1:44]
y = perceptron.values[:, 44]

sss = StratifiedShuffleSplit(n_splits=10, test_size=0.3, random_state=1)
scores = []
k = 1
for train_index, test_index in sss.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)
    ppn.fit(X_train, y_train)
    y_pred = ppn.predict(X_test)
    score = accuracy_score(y_test,y_pred)
    scores.append(score)
    print ('Iter%2d: Acc: %.3f' % (k, score))
    k +=1
    # print("TRAIN:", train_index, "TEST:", test_index)

print ('\nCV accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))










