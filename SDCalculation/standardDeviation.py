import json,statistics,math
import numpy as np

class Stddev(object):

    def __init__(self,lst):
        self.lst = lst

    def calMean(self): #Average
        return statistics.mean(self.lst)

    # def calMedian(self): #Median
    #      return statistics.median(self.lst)

    def calStd(self): #Standard Deviation
        return statistics.stdev(self.lst)

    def calAvgRstAccln(self,x,y,z): #Average Resultant Acceleration
        result = 0
        for xi,yi,zi in zip(x,y,z):
            result += math.sqrt((xi**2)+(yi**2)+(zi**2))

        return result/self.lst

    def calBinnedDist(self): #Binned Distribution
        rangeVal = max(self.lst)-min(self.lst)
        binKey = []
        for i in np.arange(min(self.lst),max(self.lst),rangeVal/10):
            binKey.append(i)

        #bins = dict.fromkeys(binKey)
        return binKey



if __name__ == '__main__':
    with open('data/data.json') as data_file:
        data = json.load(data_file)

    zAxis_data = data["zAxis"]
    yAxis_data = data["yAxis"]
    xAxis_data = data["xAxis"]

    zAxis = Stddev(zAxis_data)
    yAxis = Stddev(yAxis_data)
    xAxis = Stddev(xAxis_data)
    allAxis = Stddev(len(xAxis_data))

    print  "\nStandard Deviation of zAxis is " + str(round(zAxis.calStd(),2))
    print  "Standard Deviation of yAxis is " + str(yAxis.calStd())
    print  "Standard Deviation of zAxis is " + str(xAxis.calStd())

    # print  "\nMedian of zAxis is " + str(zAxis.calMedian())
    # print  "Median of yAxis is " + str(yAxis.calMedian())
    # print  "Median of xAxis is " + str(xAxis.calMedian())

    print  "\nMean of zAxis is " + str(zAxis.calMean())
    print  "Mean of yAxis is " + str(yAxis.calMean())
    print  "Mean of xAxis is " + str(xAxis.calMean())

    print "\nAverage Resultant Acceleration is " + str(allAxis.calAvgRstAccln(xAxis_data,yAxis_data,zAxis_data))

    print "\nBinned Distribution of zAxis is " + str(Stddev(zAxis_data).calBinnedDist());
    print "Binned Distribution of yAxis is " + str(Stddev(yAxis_data).calBinnedDist());
    print "Binned Distribution of xAxis is " + str(Stddev(xAxis_data).calBinnedDist());




