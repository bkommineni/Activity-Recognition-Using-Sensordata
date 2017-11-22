import json
import matplotlib.pyplot as plt
from pprint import pprint

with open('./../Data/surada_walking_10.json') as data_file:
    walking_data = json.load(data_file)

x_axis_walk_data = walking_data['xAxis']
y_axis_walk_data = walking_data['yAxis']
z_axis_walk_data = walking_data['zAxis']

timestamp_data = walking_data['sensorTimeStamps']



plt.subplot(3,1,1)
plt.plot(timestamp_data, x_axis_walk_data, color='r')
plt.ylabel("Acceleration")
plt.title("x-axis")

plt.subplot(3,1,2)
plt.plot(timestamp_data, y_axis_walk_data, color='g')
plt.ylabel("Acceleration")
plt.title("y-axis")

plt.subplot(3,1,3)
plt.plot(timestamp_data, z_axis_walk_data, color='y')
plt.xlabel("Time(ms)")
plt.ylabel("Acceleration")
plt.title("z-axis")
plt.legend()

plt.subplots_adjust(hspace=0.8)
plt.suptitle("Walking")
plt.savefig('./../images/Acceleration_walk.png',dpi=1000)
