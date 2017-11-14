import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('../FeaturesCsvFile/featuresfile.csv'
                 , header=None)
df.tail()

y = df.iloc[0:1, 1].values
y = np.where(y == 'Label', -1, 1)

X = df.iloc[0:1, [32, 33]].values

# plot data
plt.scatter(X[:50, 0], X[:50, 1],
            color='red', marker='o', label='walking')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='blue', marker='x', label='running')

plt.xlabel('walking')
plt.ylabel('running')
plt.legend(loc='upper left')

plt.tight_layout()
#plt.savefig('./images/02_06.png', dpi=300)
plt.show()