

def get_timestamps_peaks(list_of_peaks):
    timestamps = []
    for i in range(0,len(list_of_peaks)):
        timestamps.append(list_of_peaks[i][1])
    return timestamps