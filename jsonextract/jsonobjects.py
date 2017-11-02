import csv
import decimal
import json
import os
import statistics

import numpy as np

from CalPeaks import cal_peaks
from GetTimeStampsPeaks import get_timestamps_peaks


def generate_binned_distribution(data):
    x_axis_data = data['xAxis']
    y_axis_data = data['yAxis']
    z_axis_data = data['zAxis']

    bins_x = get_bins(x_axis_data)
    bins_y = get_bins(y_axis_data)
    bins_z = get_bins(z_axis_data)
    fractions_arr_x = make_bins(bins_x, x_axis_data)
    fractions_arr_y = make_bins(bins_y, y_axis_data)
    fractions_arr_z = make_bins(bins_z, z_axis_data)
    fractions_arr = [fractions_arr_x, fractions_arr_y, fractions_arr_z]
     # print(fractions_arr)
    return fractions_arr


def make_bins(bins_x, x_axis_data):
    freq, bins = np.histogram(x_axis_data, bins_x)
    sum = 0
    for i in range(0, 10):
        sum += freq[i]
    fractions_arr = []
    for i in range(0, 10):
        fractions_arr.append(freq[i] / decimal.Decimal(len(x_axis_data)))
    return fractions_arr


def get_bins(x_axis_data):
    maximum_x = np.array(x_axis_data).max()
    minimum_x = np.array(x_axis_data).min()
    bin_size_x = (maximum_x - minimum_x) / 11
    bins_x = np.arange(minimum_x, maximum_x, bin_size_x)
    return bins_x


def generate_call_peaks(data):
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

    # Average time difference between peaks for each axis

    avg_time_diff_btwn_peaks_x_axis = np.average(np.diff(timestamps_peaks_x))

    avg_time_diff_btwn_peaks_y_axis = np.average(np.diff(timestamps_peaks_y))

    avg_time_diff_btwn_peaks_z_axis = np.average(np.diff(timestamps_peaks_z))
    list = [avg_time_diff_btwn_peaks_x_axis, avg_time_diff_btwn_peaks_y_axis, avg_time_diff_btwn_peaks_z_axis]

    return list

def generate_absolute_acc_diff(data):
    x_axis_data = data['xAxis']
    y_axis_data = data['yAxis']
    z_axis_data = data['zAxis']
    timestamps = data['sensorTimeStamps']

    # np.average takes an optional weight parameter. If it is not supplied mean and average are equivalent

    x = np.array(x_axis_data)
    x_mean = np.mean(x, dtype=np.float64)
    absValuesX = []
    for x in x_axis_data:
        absValuesX.append(abs(x_mean - x))
    AverageAbsoluteDiffX = np.average(absValuesX)

    y = np.array(y_axis_data)
    y_mean = np.mean(y, dtype=np.float64)
    absValuesY = []
    for y in y_axis_data:
        absValuesY.append(abs(y_mean - y))
    AverageAbsoluteDiffY = np.average(absValuesY)

    z = np.array(z_axis_data)
    z_mean = np.mean(z, dtype=np.float64)
    absValuesZ = []
    for z in z_axis_data:
        absValuesZ.append(abs(z_mean - z))
    AverageAbsoluteDiffZ = np.average(absValuesZ)
    aalist = [AverageAbsoluteDiffX, AverageAbsoluteDiffY, AverageAbsoluteDiffZ]
    return aalist


def generate_average_accleration(data):
    x_axis_data = data['xAxis']
    y_axis_data = data['yAxis']
    z_axis_data = data['zAxis']
    avg_acc = [calMean(x_axis_data), calMean(y_axis_data), calMean(z_axis_data)]
    return avg_acc

def generate_std_dev(data):
    x_axis_data = data['xAxis']
    y_axis_data = data['yAxis']
    z_axis_data = data['zAxis']
    std_dev = [calStd(x_axis_data), calStd(y_axis_data), calStd(z_axis_data)]
    return std_dev


def calMean(self):  # Average
    return statistics.mean(self)


def calStd(self):  # Standard Deviation
    return statistics.stdev(self)


def calAvgRstAccln(self, x, y, z):  # Average Resultant Acceleration
    result = 0
    for xi, yi, zi in zip(x, y, z):
        result += np.math.sqrt((xi ** 2) + (yi ** 2) + (zi ** 2))

    return result / self.lst


if __name__ == '__main__':
    os.remove("featuresfile.csv")
    with open("featuresfile.csv", "a") as cf:
        csvwriter = csv.writer(cf)
        csvwriter.writerow(["BinnedDistribution", "PeaksList", "Average Absolute Difference", "Average Acceleration"
                            , "Standard Deviation"])

    file_path = "data.json"
    with open(file_path) as f:
        for line in f:
            j_content = json.loads(line)
            bin_dis = generate_binned_distribution(j_content)
            list_of_peaks = generate_call_peaks(j_content)
            aalist = generate_absolute_acc_diff(j_content)
            avgacclist = generate_average_accleration(j_content)
            stddevlist = generate_std_dev(j_content)
            with open("featuresfile.csv", "a") as cf:
                csvwriter = csv.writer(cf)
                csvwriter.writerow([bin_dis, list_of_peaks, aalist, avgacclist, stddevlist])