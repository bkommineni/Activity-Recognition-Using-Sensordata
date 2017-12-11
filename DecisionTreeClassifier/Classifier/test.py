from scipy import stats
import numpy as np

x = np.linspace(-15, 15, 9)
print(type(x))
print(stats.kstest(x, 'norm'))