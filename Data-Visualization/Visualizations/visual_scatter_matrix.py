from pandas.plotting import scatter_matrix
import pandas as pd
import matplotlib.pyplot as plt

frame = pd.read_csv("./../FeaturesCsvFile/featuresfile.csv")

frame = frame.loc[:,["Bin7,x","Bin10,x","Bin3,z","TimeDiffPeaks-z","AvgAbsDiff-x","AvgAbsDiff-y","AvgAbsDiff-z"
                    ,"AvgAcc-x","AvgAcc-y"]]
scatter_matrix(frame)
plt.savefig('./../images/scatter_matrix_9_features.png',dpi=1000)
