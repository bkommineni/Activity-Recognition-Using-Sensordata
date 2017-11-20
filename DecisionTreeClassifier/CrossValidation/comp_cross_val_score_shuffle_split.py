from sklearn.model_selection import cross_val_score
from pathlib import Path
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from scipy import stats
import numpy as np

from sklearn import svm

my_file = Path("/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/FeaturesCsvFile/featuresfile.csv")
df = pd.read_csv(my_file)

X = df.values[:, 2:45]
Y = df.values[:, 45]
df_gini = DecisionTreeClassifier(criterion = 'gini')
cv = ShuffleSplit(n_splits=3, test_size=0.4, random_state=0)
scores = cross_val_score(df_gini,X,Y,cv=cv)

print(scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))



