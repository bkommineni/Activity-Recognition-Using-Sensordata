import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


frame = pd.read_csv("./../FeaturesCsvFile/featuresfile_10.csv")
print(len(frame))
walk_points = frame.loc[frame['Label'] == "walking"]
run_points = frame.loc[frame['Label'] == "running"]

means_walk = []
means_walk.append(walk_points['TimeDiffPeaks-x'].median())
means_walk.append(walk_points['TimeDiffPeaks-y'].median())
means_walk.append(walk_points['TimeDiffPeaks-z'].median())

means_run = []
means_run.append(run_points['TimeDiffPeaks-x'].median())
means_run.append(run_points['TimeDiffPeaks-y'].median())
means_run.append(run_points['TimeDiffPeaks-z'].median())

N = 3
ind = np.arange(N)
axes = ['TimeDiffPeaks-x','TimeDiffPeaks-y','TimeDiffPeaks-z']

fig, ax = plt.subplots()
rect1 = ax.bar(ind,means_walk,width=0.2,color='g',align='center',alpha=0.5)
rect2 = ax.bar(ind+0.2,means_run,width=0.2,color='r',align='center',alpha=0.5)

ax.set_ylabel('Avg Time Diff')
ax.set_title('Walk vs Run')
ax.set_xticks(ind + 0.2 / 2)
ax.set_xticklabels(('TimeDiffPeaks-x','TimeDiffPeaks-y','TimeDiffPeaks-z'))

ax.legend((rect1[0], rect2[0]), ('Walk', 'Run'))
plt.savefig('./../images/AvgTimeDiff_walk_run_10.png',dpi=1000)