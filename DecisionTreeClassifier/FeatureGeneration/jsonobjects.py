import csv
import decimal
import json
import os
import statistics
from pathlib import Path

import numpy as np
from FeatureGeneration.CalPeaks import cal_peaks
from FeatureGeneration.GetTimeStampsPeaks import get_timestamps_peaks

ED = 10000


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


def make_bins(bins, axis_data):
    freq, bins = np.histogram(axis_data, bins)
    sum = 0
    for i in range(0, 10):
        sum += freq[i]
    fractions_arr = []
    for i in range(0, 10):
        fractions_arr.append(freq[i] / decimal.Decimal(len(axis_data)))
    return fractions_arr


def get_bins(axis_data):
    maximum = np.array(axis_data).max()
    minimum = np.array(axis_data).min()
    bin_size = (maximum - minimum) / 11
    bins = np.arange(minimum, maximum, bin_size)
    return bins


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


def generate_res_acc(data):  # Average Resultant Acceleration
    result = 0
    x_axis_data = data['xAxis']
    y_axis_data = data['yAxis']
    z_axis_data = data['zAxis']
    for xi, yi, zi in zip(x_axis_data, y_axis_data, z_axis_data):
        result += np.math.sqrt((xi ** 2) + (yi ** 2) + (zi ** 2))

    return result / ED


if __name__ == '__main__':
    my_file = Path("/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/FeaturesCsvFile/featuresfile.csv")
    if my_file.exists() :
        os.remove("/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/FeaturesCsvFile/featuresfile.csv")

    with open("/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/FeaturesCsvFile/featuresfile.csv", "a") as cf:
        csvwriter = csv.writer(cf)
        csvwriter.writerow(["User","Timestamp","Bin1,x","Bin2,x","Bin3,x","Bin4,x","Bin5,x","Bin6,x","Bin7,x","Bin8,x","Bin9,x","Bin10,x",
                            "Bin1,y","Bin2,y","Bin3,y","Bin4,y","Bin5,y","Bin6,y","Bin7,y","Bin8,y","Bin9,y","Bin10,y",
                            "Bin1,z","Bin2,z","Bin3,z","Bin4,z","Bin5,z","Bin6,z","Bin7,z","Bin8,z","Bin9,z","Bin10,z",
                            "TimeDiffPeaks-x","TimeDiffPeaks-y","TimeDiffPeaks-z",
                            "AvgAbsDiff-x","AvgAbsDiff-y","AvgAbsDiff-z",
                            "AvgAcc-x","AvgAcc-y","AvgAcc-z",
                            "StdDev-x","StdDev-y","StdDev-z",
                            "AvgResAcc","Label"])

    file_path = "/Users/bharu/CS690-PROJECTS/ActivityAnalyzer/activity_analyzer/DecisionTreeClassifier/Data/BAS.json"
    with open(file_path) as f:
        for line in f:
            bhargavi_device = 'd4e6b172e6e4600b'
            surada_device = '3093faee1cbda203'
            anjani_device = '8bfa3ca49705cd76'
            j_content = json.loads(line)
            device_id = j_content['deviceid']
            label = j_content['label']
            timestamp = j_content['senseStartTimeMillis']
            bin_dis = generate_binned_distribution(j_content)
            list_of_peaks = generate_call_peaks(j_content)
            aalist = generate_absolute_acc_diff(j_content)
            avgacclist = generate_average_accleration(j_content)
            stddevlist = generate_std_dev(j_content)
            avg_res_acc = generate_res_acc(j_content)

            username = ''
            print(device_id)
            if device_id == bhargavi_device:
                username = 'Bhargavi'
            if device_id == surada_device:
                username = 'Surada'
            if device_id == anjani_device:
                username = 'Anjani'

            with open(my_file, "a") as cf:
                csvwriter = csv.writer(cf)
                csvwriter.writerow([username,timestamp,bin_dis[0][0],bin_dis[0][1],bin_dis[0][2],bin_dis[0][3],bin_dis[0][4],bin_dis[0][5],bin_dis[0][6],bin_dis[0][7],bin_dis[0][8],bin_dis[0][9],
                                    bin_dis[1][0], bin_dis[1][1], bin_dis[1][2], bin_dis[1][3], bin_dis[1][4],bin_dis[1][5], bin_dis[1][6], bin_dis[1][7], bin_dis[1][8], bin_dis[1][9],
                                    bin_dis[2][0], bin_dis[2][1], bin_dis[2][2], bin_dis[2][3], bin_dis[2][4],bin_dis[2][5], bin_dis[2][6], bin_dis[2][7], bin_dis[2][8], bin_dis[2][9],
                                    list_of_peaks[0], list_of_peaks[1],list_of_peaks[2],
                                    aalist[0], aalist[1], aalist[2],
                                    avgacclist[0], avgacclist[1], avgacclist[2],
                                    stddevlist[0], stddevlist[1],stddevlist[2],
                                    avg_res_acc,label])
