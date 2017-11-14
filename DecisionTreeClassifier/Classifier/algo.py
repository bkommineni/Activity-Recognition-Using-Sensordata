from pathlib import Path
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

my_file = Path("/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/FeaturesCsvFile/featuresfile.csv")
df = pd.read_csv(my_file)

X = df.values[:, 1:5]
Y = df.values[:, 44]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)

#Using gini impurity
df_gini = DecisionTreeClassifier(criterion = 'gini')
df_gini.fit(X_train, Y_train)

arr = df_gini.feature_importances_

print(arr)

tree.export_graphviz(df_gini,feature_names=df.columns.values[1:5],out_file='tree_gini.dot')

#Predicting using test data
Y_predict_gini = df_gini.predict(X_test)

#print(Y_predict_gini)

#Calculating accuracy score
score = accuracy_score(Y_test,Y_predict_gini)

print(score)

cm = confusion_matrix(Y_test,Y_predict_gini)

print(cm)

#Using entropy(information gain)
df_entropy = DecisionTreeClassifier(criterion='entropy')
df_entropy.fit(X_train, Y_train)

tree.export_graphviz(df_entropy,feature_names=df.columns.values[1:5],out_file='tree_entropy.dot')

Y_predict_entropy = df_entropy.predict(X_test)

score_en = accuracy_score(Y_test,Y_predict_entropy)

print(score_en)

