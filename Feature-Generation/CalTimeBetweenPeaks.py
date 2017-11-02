import json
from CalPeaks import cal_peaks
from GetTimeStampsPeaks import get_timestamps_peaks
import numpy as np
from pprint import pprint

with open('data/bhargavi_running_20.json') as data_file:
    data = json.load(data_file)

x_axis_data = data['xAxis']
y_axis_data = data['yAxis']
z_axis_data = data['zAxis']
timestamps = data['sensorTimeStamps']

allPeaksX = cal_peaks(x_axis_data, timestamps)
allPeaksY = cal_peaks(y_axis_data, timestamps)
allPeaksZ = cal_peaks(z_axis_data, timestamps)

timestamps_peaks_x = get_timestamps_peaks(allPeaksX)

timestamps_peaks_y = get_timestamps_peaks(allPeaksY)

timestamps_peaks_z = get_timestamps_peaks(allPeaksZ)

#Average time difference between peaks for each axis

avg_time_diff_btwn_peaks_x_axis = np.average(np.diff(timestamps_peaks_x))

avg_time_diff_btwn_peaks_y_axis = np.average(np.diff(timestamps_peaks_y))

avg_time_diff_btwn_peaks_z_axis = np.average(np.diff(timestamps_peaks_z))

#pprint(avg_time_diff_btwn_peaks_x_axis)

#pprint(avg_time_diff_btwn_peaks_y_axis)

#pprint(avg_time_diff_btwn_peaks_z_axis)