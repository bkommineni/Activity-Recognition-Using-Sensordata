import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




df = pd.read_csv('../FeaturesCsvFile/featuresfile.csv')

y = df.iloc[0:100, 44].values
print (y)
y = np.where(y == 'walking', -1, 1)
print (y)
X = df.iloc[0:100, [32, 34]].values
print (X)
# plot data
plt.scatter(X[:50, 0], X[:50, 1],
           color='red', marker='o', label='walking')
plt.scatter(X[50:100, 0], X[50:100, 1],
           color='blue', marker='x', label='running')

plt.xlabel('peak Y')
plt.ylabel('peak Z')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

