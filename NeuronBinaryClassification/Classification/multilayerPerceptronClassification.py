from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import pandas as pd


# multi_layer = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')
# X = multi_layer.values[:, 1:44]
# y = multi_layer.values[:, 44]
# X_train, X_test, y_train, y_test = train_test_split(X, y)
multi_layer_train = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')
multi_layer_test = pd.read_csv('../FeaturesCsvFile/featuresfile_10.csv')

X_train = multi_layer_train.values[:, 2:45]
y_train = multi_layer_train.values[:, 45]
X_test = multi_layer_test.values[:, 2:45]
y_test = multi_layer_test.values[:, 45]

scaler = StandardScaler()
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
mlp.fit(X_train,y_train)
y_pred = mlp.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print('\nAccuracy of Perceptron Score: %.2f' % mlp.score(X_test,y_test))
print('\nAccuracy of Accuracy Score : %.2f' % accuracy_score(y_test,y_pred))