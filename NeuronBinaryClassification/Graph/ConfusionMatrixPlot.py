from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd


perceptron_train = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')
perceptron_test = pd.read_csv('../FeaturesCsvFile/featuresfile_10.csv')



X_train = perceptron_train.values[:, 2:45]
y_train = perceptron_train.values[:, 45]
X_test = perceptron_test.values[:, 2:45]
y_test = perceptron_test.values[:, 45]

ppn = Perceptron(n_iter=40, eta0=0.1, random_state=1)
ppn.fit(X_train, y_train)
y_pred = ppn.predict(X_test)
confmt = confusion_matrix(y_test,y_pred)

fig, ax = plt.subplots(figsize=(2.5,2.5))
ax.matshow(confmt, cmap=plt.cm.Blues)
for i in range(confmt.shape[0]):
    for j in range(confmt.shape[1]):
        ax.text(x=j, y=i, s=confmt[i,j],va='center',ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
# plt.savefig('./images/scatter_AvgAbsDiffxy_dt_train_3_val_10.png',dpi=1000)
plt.show()




