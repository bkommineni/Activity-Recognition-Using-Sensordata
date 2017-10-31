from math import sqrt
import json

class Stddev(object):

    def __init__(self,lst):
        self.lst = lst
        self.mean = 0

    def calSum(self):
        return sum(self.lst) / len(self.lst)

    def calStd(self):
        self.mean = sum(self.lst) / len(self.lst)
        variance = float(sum([(e - self.mean) ** 2 for e in self.lst])) / (len(self.lst)-1)
        return sqrt(variance)

if __name__ == '__main__':

    with open('data/data.json') as data_file:
        data = json.load(data_file)

    zAxis_data = data["zAxis"]
    yAxis_data = data["yAxis"]
    xAxis_data = data["xAxis"]

    zAxis_std = Stddev(zAxis_data)
    yAxis_std = Stddev(yAxis_data)
    xAxis_std = Stddev(xAxis_data)

    print  "\nStandard Deviation of zAxis is " + str(round(zAxis_std.calStd(),2))
    print  "Standard Deviation of yAxis is " + str(yAxis_std.calStd())
    print  "Standard Deviation of zAxis is " + str(xAxis_std.calStd())





