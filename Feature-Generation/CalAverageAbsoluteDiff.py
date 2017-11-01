import json
import numpy as np
from pprint import pprint

with open('data/bhargavi_running_20.json') as data_file:
    data = json.load(data_file)

x_axis_data = data['xAxis']
y_axis_data = data['yAxis']
z_axis_data = data['zAxis']
timestamps = data['sensorTimeStamps']

#np.average takes an optional weight parameter. If it is not supplied mean and average are equivalent

x = np.array(x_axis_data)
x_mean = np.mean(x, dtype=np.float64)
absValuesX = []
for x in x_axis_data:
    absValuesX.append(abs(x_mean-x))
AverageAbsoluteDiffX = np.average(absValuesX)
pprint(AverageAbsoluteDiffX)

y = np.array(y_axis_data)
y_mean = np.mean(y, dtype=np.float64)
absValuesY = []
for y in y_axis_data:
    absValuesY.append(abs(y_mean-y))
AverageAbsoluteDiffY = np.average(absValuesY)
pprint(AverageAbsoluteDiffY)

z = np.array(z_axis_data)
z_mean = np.mean(z, dtype=np.float64)
absValuesZ = []
for z in z_axis_data:
    absValuesZ.append(abs(z_mean-z))
AverageAbsoluteDiffZ = np.average(absValuesZ)
pprint(AverageAbsoluteDiffZ)
