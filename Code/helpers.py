import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks
from numpy.linalg import norm


def butter_lowpass_filter(data):
    cutoff = 2
    order = 8
    normal_cutoff = cutoff / 100
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='lowpass', analog=False)
    y = filtfilt(b, a, data)
    return y


def gyr_butter_lowpass_filter(data):
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


def calc_uz(t, data, acc, s):
    if t == 0:
        uz = data[0, 1:]
    else:
        uz = np.dot(data[t-1, 1:], s) + np.dot(acc[t, 1:], 1-s)
    return uz


def calc_ux(uz):
    temp = np.array([0, 1, 0])
    ux = np.cross(temp, uz)
    return ux


def calc_uy(ux, uz):
    return np.cross(uz, ux)


def calc_R(t, data, acc):
    uz = calc_uz(t, data, acc, 0.5)
    ux = calc_ux(uz)
    uy = calc_uy(ux, uz)
    return np.array([np.dot(ux, 1/norm(ux)), np.dot(uy, 1/norm(uy)), np.dot(uz, 1/norm(uz))])


def derived_theta(t, data, acc):
    R_transposed = np.transpose(calc_R(t, data, acc))
    Omega_prime = np.dot(R_transposed, np.transpose(data[t, 1:]))
    return Omega_prime[2]