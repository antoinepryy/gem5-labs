import numpy as np


def mean_cpu_cores(data):
    return np.mean(data, axis=0)


def filter_array(data, index):
    out = data.copy()
    for k in range(len(out)):
        out[k] = data[k][index]
    return out
