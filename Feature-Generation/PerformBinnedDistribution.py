import json
import numpy as np
import decimal
from pprint import pprint

with open('data/bhargavi_running_20.json') as data_file:
    data = json.load(data_file)

x_axis_data = data['xAxis']
y_axis_data = data['yAxis']
z_axis_data = data['zAxis']
timestamps = data['sensorTimeStamps']

maximum_x = np.array(x_axis_data).max()
minimum_x = np.array(x_axis_data).min()

bin_size_x = (maximum_x-minimum_x)/11

bins_x = np.arange(minimum_x,maximum_x,bin_size_x)

freq, bins = np.histogram(x_axis_data,bins_x)

#pprint(freq)

sum = 0
for i in range(0,10):
    sum += freq[i]

#pprint(sum)

#pprint(len(x_axis_data))

fractions_arr = []

for i in range(0,10):
    fractions_arr.append(decimal.Decimal(freq[i])/decimal.Decimal(len(x_axis_data)))

#pprint(fractions_arr)