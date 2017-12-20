from pathlib import Path
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from scipy import stats
import numpy as np

#my_file = Path("/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/FeaturesCsvFile/featuresfile.csv")
#df = pd.read_csv(my_file)

#X_train = df.values[:, 2:45]
#Y_train = df.values[:, 45]

test_file = Path("/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/FeaturesCsvFile/featuresfile_10.csv")


df_test = pd.read_csv(test_file)
X = df_test.values[:, 2:45]
Y = df_test.values[:, 45]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)


#Using gini impurity
df_gini = DecisionTreeClassifier(criterion = 'gini')
df_gini.fit(X_train, Y_train)

arr = df_gini.feature_importances_

print(arr)

tree.export_graphviz(df_gini,feature_names=df_test.columns.values[2:45],out_file='tree_gini_10.dot')

#Predicting using test data
Y_predict_gini = df_gini.predict(X_test)

#print(Y_predict_gini)

#Calculating accuracy score
score = accuracy_score(Y_test,Y_predict_gini)
#print(len(Y_test))

print(score)


