import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Perceptron(object):

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


df = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')

y = df.iloc[0:100, 44].values
y = np.where(y == 'walking', -1, 1)
X = df.iloc[0:100, [32, 34]].values

ppn = Perceptron(eta=0.1, n_iter=40)
ppn.fit(X,y)
plt.plot(range(1,len(ppn.errors_) +1),ppn.errors_,marker='o')
plt.xlabel('Epochs')
plt.ylabel('NUmber of updates')
plt.show()


#An epoch is a measure of the number of times all of the training features are
#used once to update the weights.For batch training all of the training samples
#pass through the learning algorithm simultaneously in one epoch before weights are updated.



