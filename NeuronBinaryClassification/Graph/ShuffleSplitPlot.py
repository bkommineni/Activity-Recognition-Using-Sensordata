from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plotGraph(obj1,obj2):
    AxisX = obj2[1:44]
    AxisY = obj1[0]
    y_pos = np.arange(len(AxisX))
    plt.barh(y_pos, AxisY)
    plt.yticks(y_pos, AxisX)
    plt.xlabel('Weights assigned to the features')
    plt.title('What Features are selected the most during 10 iterations of classification ')
    plt.show()

perceptron = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')
X = perceptron.values[:, 1:44]
y = perceptron.values[:, 44]

sss = StratifiedShuffleSplit(n_splits=10, test_size=0.3, random_state=1)
scores = []
allArrays = np.array([])
n = 1;
for train_index, test_index in sss.split(X, y):
    n +=1
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)
    ppn.fit(X_train, y_train)
    y_pred = ppn.predict(X_test)
    if(len(allArrays) == 0):
        allArrays = np.array(ppn.coef_)
    else:
        allArrays = np.add(allArrays,np.array(ppn.coef_))


header = list(perceptron.head(1))
allArrays[:] = [x / n for x in allArrays]
plotGraph(allArrays,header)











