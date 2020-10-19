import logging

import numpy as np
import matplotlib.pyplot as plt

import pyplot.settings

logger = logging.getLogger(__name__)


def histogram(data, filepath, xlabel, ylabel, title, ylim=None):
    """
    :param data: Dict of {'label': data}.
    """
    _, ax = plt.subplots()

    # First value of first entry.
    _min = _max = list(data.values())[0][0]

    # Find min and max values.
    for key, value in data.items():
        class_min = int(np.floor(value.min()))
        class_max = int(np.ceil(value.max()))

        if class_min < _min:
            _min = class_min

        if class_max > _max:
            _max = class_max

    for entry_name, entry_data in data.items():
        bins = list(range(_min, 10 + _max, 10))

        hist, bin_edges = np.histogram(entry_data, bins=bins)

        width = bin_edges[1] - bin_edges[0]

        # Each bin represents the fraction of samples.
        hist = hist / hist.sum()

        plt.bar(bin_edges[:-1], hist, width=width, label=entry_name, alpha=0.6)

    if ylim:
        ax.set_ylim(top=ylim)

    pyplot.settings.set_settings(title, xlabel, ylabel, legend=True)
    plt.savefig(filepath)


def plot_line(data, filepath, title, xlabel, ylabel, legend=True):
    plt.figure()

    for label, x, y in data:
        plt.plot(x, y, label=label, linewidth=0.5)

    pyplot.settings.set_settings(title, xlabel, ylabel, legend)
    plt.savefig(filepath)


def scatter(data, filepath, title, xlabel, ylabel, legend=True):
    """
    :param data: Numpy array with (class, x, y).
    """
    fig, ax = plt.subplots(1, 1)

    for i in range(int(data[:, 0].max() + 1)):
        mask = data[:, 0] == i
        ax.scatter(data[mask, 1], data[mask, 2], marker='.', s=1, label=str(i), alpha=0.6)

    pyplot.settings.set_settings(title, xlabel, ylabel, legend)
    plt.savefig(filepath)


# TODO
def lines_confidence(data, filepath, title, xlabel, ylabel, legend=True):
    """
    :param data: Dict with {'label', data} where data = (line, error) and
        line,error are of shape (N, 2).
    """
    fig, ax = plt.subplots(1, 1)

    for label, line_data in data.items():
        line, error = line_data

        ax.plot(line[:, 0], line[:, 1], label=label, linewidth=0.5)

        upper = line[:, 1] + error[:, 1]
        lower = line[:, 1] - error[:, 1]

        ax.fill_between(line[:, 0], lower, upper, alpha=0.1)

    pyplot.settings.set_settings(title, xlabel, ylabel, legend)
    plt.savefig(filepath)


def lines(data, filepath, title, xlabel, ylabel, legend=True):
    """
    :param data: Dict with {'label': data} where data is a numpy array of shape (N, 2).
    """
    fig, ax = plt.subplots(1, 1)

    for label, line in data.items():
        ax.plot(line[:, 0], line[:, 1], label=label, linewidth=0.5)

    pyplot.settings.set_settings(title, xlabel, ylabel, legend)
    plt.savefig(filepath)