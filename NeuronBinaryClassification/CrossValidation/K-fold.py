from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

import numpy as np
import pandas as pd


perceptron = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')
X = perceptron.values[:, 1:44]
y = perceptron.values[:, 44]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)
ppn.fit(X_train, y_train)
y_pred = ppn.predict(X_test)

print 'X train size =', len(X_train)
print 'Y train size =' , len(y_train)

scores = cross_val_score(estimator=ppn, X=X_train, y=y_train, cv=10, n_jobs=1)
print ('\nCV accuracy: %.3f +/- %.3f\n' % (np.mean(scores), np.std(scores)))

kfold = StratifiedKFold(n_splits=10, random_state=1).split(X_train, y_train)
scoress = []
for k, (train, test) in enumerate(kfold):

    ppn.fit(X_train[train], y_train[train])
    y_pred = ppn.predict(X_test)
    score = accuracy_score(y_test,y_pred)
    scoress.append(score)
    print ('Fold: %2d,  Acc: %.3f' % (k+1,  score))

print ('\nCV accuracy: %.3f +/- %.3f' % (np.mean(scoress), np.std(scoress)))









