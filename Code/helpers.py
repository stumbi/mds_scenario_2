import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks


def butter_lowpass_filter(data):
    cutoff = 2
    order = 8
    normal_cutoff = cutoff / 100
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='lowpass', analog=False)
    y = filtfilt(b, a, data)
    return y


def helper_find_peaks(data):
    ret, _ = find_peaks(data, height=0.7)
    return ret


def push_data_to_zero(data):
    mean = np.mean(data)


def normalize(data):
    temp = 0
    for i in data:
        temp += (i*i)
    return np.sqrt(temp)