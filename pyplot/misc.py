import numpy as np
import matplotlib.pyplot as plt


def get_colormap(keys):
    """get_colormap.

    :param keys: A list of keys.
    :return: A dict with {key: color} where the colors are from matplotlibs axes.prop_cycle.
    """
    return {
        key: color
        for key, color in zip(keys, plt.rcParams["axes.prop_cycle"].by_key()["color"])
    }


def enumerate_array(y):
    """enumerate_array

    :param y: Numpy array with shape (N,)
    :return: Numpy array with shape (N, 2) where first column is the enumeration.
    """
    x = np.arange(y.shape[0])

    return np.stack((x, y), axis=1)
