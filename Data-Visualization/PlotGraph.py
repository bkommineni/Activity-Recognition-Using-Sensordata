import json
import matplotlib.pyplot as plt
from pprint import pprint

with open('data/bhargavi_running_10.json') as data_file:
    data = json.load(data_file)

pprint(data)

x_axis_data = data['xAxis']
y_axis_data = data['yAxis']
z_axis_data = data['zAxis']

timestamp_data = data['sensorTimeStamps']


plt.xlabel("Time(ms)")
plt.ylabel("Acceleration")
plt.plot(timestamp_data, x_axis_data, color='r', label='Ax')
plt.plot(timestamp_data, y_axis_data, color='b',label='Ay')
plt.plot(timestamp_data,z_axis_data, color='g',label='Az')
plt.legend()
plt.show()
