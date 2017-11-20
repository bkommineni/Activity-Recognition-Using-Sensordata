from pathlib import Path
from sklearn import tree
import pandas as pd

from pandas.plotting import scatter_matrix
import numpy as np
from numpy import loadtxt, where
from pylab import scatter, show, legend, xlabel, ylabel
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from Classifier.decision_region import plot_decision_regions

my_file = Path("/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/FeaturesCsvFile/featuresfile.csv")
df = pd.read_csv(my_file)

X = df.values[:, 2:45]
Y = df.values[:, 45]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)


logistic = LogisticRegression(C=1e5,random_state=1)

logistic.fit(X_train,Y_train)

print(logistic.intercept_)
print(logistic.coef_)
print(len(logistic.coef_))

lg_score_train_Data = logistic.score(X_train,Y_train)

print(lg_score_train_Data)

lg_score_test_Data = logistic.score(X_test,Y_test)

print(lg_score_test_Data)

walk_points = where(Y == "walking")
run_points = where(Y == "running")
#scatter(X[walk_points, 0], X[walk_points, 1], marker='o', c='b')
#scatter(X[run_points, 0], X[run_points, 1], marker='x', c='r')
#legend(['walking', 'running'])
#show()

#plt.scatter(walk_points,run_points,marker='o',c='b',alpha=0.5)
#plt.scatter(run_points,marker='r',c='r',alpha=0.5)
#plt.show()

#scatter_matrix(df)
##X_combined = np.vstack((X_train,X_test))
#y_combined = np.hstack((Y_train,Y_test))
#plot_decision_regions(X=X_combined,y=y_combined,classifier=logistic,test_idx=range(105,150))
#plt.show()


