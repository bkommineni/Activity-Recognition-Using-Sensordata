def cal_peaks(readings,timestamps):
    flag = False
    prev_val = readings[0]

    # allPeaks has list of all up and down peaks
    # up peaks has peaks from where the values start increasing
    # down peaks has peaks where the values start decreasing

    # Calculating Peaks for each axis
    allPeaksList = []
    upPeaksList = []
    downPeaksList = []

    for i in range(1, len(readings) - 1):
        if readings[i] > prev_val:
            if not flag:
                flag = True
                peak = []
                peak.append(prev_val)
                peak.append(timestamps[i])
                allPeaksList.append(peak)
                downPeaksList.append(peak)
            prev_val = readings[i]
        else:
            if flag:
                flag = False
                peak = []
                peak.append(prev_val)
                peak.append(timestamps[i])
                allPeaksList.append(peak)
                upPeaksList.append(peak)
            prev_val = readings[i]

    return allPeaksList