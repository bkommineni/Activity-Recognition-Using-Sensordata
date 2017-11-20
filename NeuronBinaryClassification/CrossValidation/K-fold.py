from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
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

kfold = StratifiedKFold(n_splits=32, random_state=1).split(X_train, y_train)
scores = cross_val_score(estimator=ppn, X=X_train, y=y_train, cv=32, n_jobs=1)

# scores = []
# for k, (train, test) in enumerate(kfold):
#     ppn.fit(X_train[train], y_train[train])
#     score = ppn.score(X_test[test], y_test[test])
#     scores.append(score)
#     print ('Fold: %2d, Class dist. : %s, Acc: %.3f' % (k+1, y_train[train], score))
#
#
# print ('\nCV accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))









