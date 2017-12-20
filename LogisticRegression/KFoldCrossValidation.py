from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
import pandas as pd

lr_data = pd.read_csv('H:/mastersProject/activity_analyzer/LogisticRegression/Data/featuresfile.csv')
X = lr_data.values[:, 1:44]
y = lr_data.values[:, 44]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
lr = LogisticRegression(C=100.0, random_state=1)
lr.fit(X_train, y_train)
kfold = StratifiedKFold(n_splits=32, random_state=1).split(X_train, y_train)
scores = cross_val_score(estimator=lr, X=X_train, y=y_train, cv=10)

print(scores)
