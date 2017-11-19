from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
import pandas as pd

def plot_decision_regions(X, y_plot, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y_plot))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, cl in enumerate(np.unique(y_plot)):
        plt.scatter(x=X[y_plot == cl, 0], y=X[y_plot == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    edgecolor='black',
                    marker=markers[idx],
                    label=cl)


if __name__ == "__main__":
    perceptron = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')
    X = perceptron.values[:, 32:34]
    y = perceptron.values[:, 44] #label : walking/runing
    y_plot = np.where(y == 'walking', -1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y_plot, test_size=0.3)
    ppn = Perceptron(n_iter=40, eta0=0.1, random_state=1)
    ppn.fit(X_train, y_train)
    y_pred = ppn.predict(X_test)
    plot_decision_regions(X, y_plot, classifier=ppn)
    plt.xlabel('TimeDiffPeaks-y')
    plt.ylabel('TimeDiffPeaks-z')
    L=plt.legend()
    L.get_texts()[0].set_text('Walking')
    L.get_texts()[1].set_text('Running')
    plt.tight_layout()
    plt.title('TimeDiffPeaks-y vs TimeDiffPeaks-z')
    # plt.savefig('./perceptron_2.png', dpi=300)
    plt.show()