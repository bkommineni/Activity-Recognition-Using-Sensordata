from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

perceptron = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')

X = perceptron.values[:, 1:44]
y = perceptron.values[:, 44]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

ppn = Perceptron(n_iter=40, eta0=0.1, random_state=1)
ppn.fit(X_train, y_train)

y_pred = ppn.predict(X_test)
print(y_pred)
print('Accuracy of Accuracy Score : %.2f ' % accuracy_score(y_test,y_pred))
print('Accuracy of Perceptron Score: %.2f' % ppn.score(X_test,y_test))