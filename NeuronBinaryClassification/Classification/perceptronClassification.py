from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import pandas as pd



perceptron = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')

X = perceptron.values[:, 1:44]
y = perceptron.values[:, 44]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
ppn = Perceptron(n_iter=40, eta0=0.1, random_state=1)
ppn.fit(X_train, y_train)
y_pred = ppn.predict(X_test)
print('\nAccuracy of Accuracy Score : %.2f' % accuracy_score(y_test,y_pred))
print('\nAccuracy of Perceptron Score: %.2f' % ppn.score(X_test,y_test))
print ('\nConfustion Metrix')
print (confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))



#precision = The precision is the ratio tp / (tp + fp)
#where tp is the number of true positives and fp the number of false positives.
#The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.