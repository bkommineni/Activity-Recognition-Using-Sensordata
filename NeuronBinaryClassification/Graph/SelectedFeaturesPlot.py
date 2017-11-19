from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)
ppn.fit(X_train, y_train)
allArrays = np.array([])

for i in range(0,10):
    y_pred = ppn.predict(X_test)
    if(len(allArrays) == 0):
        allArrays = np.array(ppn.coef_)
    else:
        allArrays = np.add(allArrays,np.array(ppn.coef_))

header = list(perceptron.head(1))
print header


for x in xrange(0, len(header)):
    print x,

plotGraph(allArrays,header)





