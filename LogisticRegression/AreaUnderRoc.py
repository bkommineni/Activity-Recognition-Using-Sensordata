# Later as first we have to try Cross Validation Techniques
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.svm import classes

# classes = np.unique(y_test)
# if (pos_label is None and not (np.all(classes == [0, 1]) or
#                                    np.all(classes == [-1, 1]) or
#                                    np.all(classes == [0]) or
#                                    np.all(classes == [-1]) or
#                                    np.all(classes == [1]))):
#     raise ValueError("Data is not binary and pos_label is not specified")
# aroc = roc_auc_score(y_test, predict)
# print(aroc)