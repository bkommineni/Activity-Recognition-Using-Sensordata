import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

frame = pd.read_csv("./../FeaturesCsvFile/featuresfile_10.csv")

frame['color'] = Series([(0 if x == "walking" else 1) for x in frame['Label']])

my_color_map = ListedColormap(['r','g'],'mycolormap')

#0,red,walking
#1,green,running

plt.subplot(3,1,1)
plt.scatter(frame['TimeDiffPeaks-x'],frame['TimeDiffPeaks-y'],c = frame['color'], cmap=my_color_map
            ,marker='^',facecolors='none',edgecolors='none')
plt.title("(x,y)")

plt.subplot(3,1,2)
plt.scatter(frame['TimeDiffPeaks-y'],frame['TimeDiffPeaks-z'],c = frame['color'], cmap=my_color_map
            ,marker='^',facecolors='none',edgecolors='none')
plt.title("(y,z)")

plt.subplot(3,1,3)
plt.scatter(frame['TimeDiffPeaks-x'],frame['TimeDiffPeaks-z'],c = frame['color'], cmap=my_color_map
            ,marker='^',facecolors='none',edgecolors='none')
plt.title("(x,z)")

plt.suptitle("Time Diff Peaks (x,y,z)")

plt.savefig('./../images/TimeDiffxyz_walk_run_10.png',dpi=1000)
