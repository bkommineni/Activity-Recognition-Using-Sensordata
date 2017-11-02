import json
import numpy as np
import decimal
import csv, os

def generate_binned_distribution(data):
    x_axis_data = data['xAxis']
    y_axis_data = data['yAxis']
    z_axis_data = data['zAxis']
    timestamps = data['sensorTimeStamps']

    # print(x_axis_data)
    maximum_x = np.array(x_axis_data).max()
    minimum_x = np.array(x_axis_data).min()
    bin_size_x = (maximum_x - minimum_x) / 11
    bins_x = np.arange(minimum_x, maximum_x, bin_size_x)
    freq, bins = np.histogram(x_axis_data, bins_x)
    sum = 0
    for i in range(0, 10):
        sum += freq[i]
    fractions_arr = []
    for i in range(0, 10):
        fractions_arr.append(freq[i] / decimal.Decimal(len(x_axis_data)))
    print(fractions_arr)
    with open("featuresfile.csv", "a") as cf:
        csvwriter = csv.writer(cf)
        csvwriter.writerow(fractions_arr)

if __name__ == '__main__':
    os.remove("featuresfile.csv")
    file_path = "data.json"
    with open(file_path) as f:
        for line in f:
            j_content = json.loads(line)
            generate_binned_distribution(j_content)
