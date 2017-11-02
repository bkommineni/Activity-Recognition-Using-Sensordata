import json
import numpy as np
import decimal
import csv, os
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

if __name__ == '__main__':
    os.remove("featuresfile.csv")
    with open("featuresfile.csv", "a") as cf:
        csvwriter = csv.writer(cf)
        csvwriter.writerow(["BinnedDistribution", "PeaksList"])

    file_path = "data.json"
    with open(file_path) as f:
        for line in f:
            j_content = json.loads(line)
            bin_dis = generate_binned_distribution(j_content)
            list_of_peaks = generate_call_peaks(j_content)
            with open("featuresfile.csv", "a") as cf:
                csvwriter = csv.writer(cf)
                csvwriter.writerow([bin_dis, list_of_peaks])