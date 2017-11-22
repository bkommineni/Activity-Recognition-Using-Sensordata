import json
import matplotlib.pyplot as plt
import numpy as np

with open('./../Data/surada_running_10.json') as data_file:
    running_data = json.load(data_file)

with open('./../Data/surada_walking_10.json') as data_file:
    walking_data = json.load(data_file)

x_axis_run_data = running_data['xAxis']
y_axis_run_data = running_data['yAxis']
z_axis_run_data = running_data['zAxis']

x_axis_walk_data = walking_data['xAxis']
y_axis_walk_data = walking_data['yAxis']
z_axis_walk_data = walking_data['zAxis']

timestamp_run_data = running_data['sensorTimeStamps']

print(len(timestamp_run_data))

timestamp_walk_data = walking_data['sensorTimeStamps']

print(len(timestamp_walk_data))



N_walk = len(timestamp_walk_data)

N_run = len(timestamp_run_data)

ind_walk = np.arange(N_walk)
ind_run = np.arange(N_run)

plt.subplot(3,2,1)
plt.plot(ind_walk, x_axis_walk_data,color='r')
plt.ylabel("Acceleration")
plt.title("x-axis")

plt.subplot(3,2,2)
plt.plot(ind_run, x_axis_run_data,color='r')
plt.ylabel("Acceleration")
plt.title("x-axis")

plt.subplot(3,2,3)
plt.plot(ind_walk, y_axis_walk_data,color='g')
plt.ylabel("Acceleration")
plt.title("y-axis")

plt.subplot(3,2,4)
plt.plot(ind_run, y_axis_run_data,color='g')
plt.ylabel("Acceleration")
plt.title("y-axis")

plt.subplot(3,2,5)
plt.plot(ind_walk, z_axis_walk_data,color='y')
plt.ylabel("Acceleration")
plt.title("z-axis")

plt.subplot(3,2,6)
plt.plot(ind_run, z_axis_run_data,color='y')
plt.ylabel("Acceleration")
plt.title("z-axis")

plt.subplots_adjust(hspace=0.8)
plt.suptitle("Walking vs Running")
plt.savefig('./../images/Acceleration_walk_run.png',dpi=1000)