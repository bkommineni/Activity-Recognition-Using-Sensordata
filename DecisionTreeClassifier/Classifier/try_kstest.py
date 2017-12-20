from pathlib import Path
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from scipy import stats
import numpy as np

my_file = Path("/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/FeaturesCsvFile/featuresfile.csv")
df = pd.read_csv(my_file)

X = df.values[:, 10]

walk = []
run = []

labels = df.values[:,44]

w = 0
r = 0

for i in range(0,len(labels)):
    if(labels[i] == "walking"):
        walk.append(df.values[i, 42])
        w = w+1
    elif(labels[i] == "running"):
        run.append(df.values[i,42])
        r = r+1

print(len(walk))

print(len(run))

print(len(labels))

print(type(walk))

print(stats.kstest(walk, 'norm'))

print(stats.kstest(run, 'norm'))
