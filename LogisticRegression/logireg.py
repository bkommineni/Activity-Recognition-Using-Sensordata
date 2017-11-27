import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import numpy as np

if __name__ == '__main__':

    df_features = pd.read_csv("H:/mastersProject/activity_analyzer/LogisticRegression/Data/featuresfile.csv")
    X_train_data = df_features.values[:, 1:44]
    y_train_data = df_features.values[:, 44]
    df_features_test = pd.read_csv("H:/mastersProject/activity_analyzer/LogisticRegression/Data/featuresfile_10.csv")
    # X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size = 0.33, random_state = 42)
    X_test = df_features_test.values[:, 2:45]
    y_test = df_features_test.values[:, 45]

    lr = LogisticRegression(C=100.0, random_state=1)
    lr.fit(X_train_data, y_train_data)
    predict = lr.predict(X_test)
    logisticRegScore = lr.score(X_test, y_test)
    print(lr.coef_)
    print(logisticRegScore)

    cm = confusion_matrix(y_test, predict, labels=["walking", "running"])
    print(cm)

    # classes = np.unique(y_test)

