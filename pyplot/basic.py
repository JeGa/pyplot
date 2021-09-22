import logging

import matplotlib.pyplot as plt
import sklearn.neighbors
import numpy as np

import pyplot.misc
import pyplot.settings

logger = logging.getLogger(__name__)


def histogram(
    data,
    filepath,
    title,
    xlabel,
    ylabel,
    ylim=None,
    xlim=None,
    bins=20,
    callback=None,
    density=True,
):
    """histogram.

    :param data: Dict of {'label': data} were data is a numpy array of shape (N,).
    :param filepath: Complete path to file with extension.
    :param title: Title for the plot.
    :param xlabel: Label for x axis.
    :param ylabel: Label for y axis.
    :param ylim: Tuple with (bottom, top) limits for y axis.
    :param xlim: Tuple with (left, right) limits for x axis.
    :param callback: Function accepting the axis object for custom stuff.
    :param density: Plot additionally the kernel density estimation with Gaussian kernel.
    """
    fig, ax = plt.subplots()

    cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    for (entry_name, entry_data), color in zip(data.items(), cycle):
        ax.hist(
            entry_data,
            label=entry_name,
            density=True,
            bins=bins,
            alpha=0.6,
            color=color,
        )

        if density:
            kde = sklearn.neighbors.KernelDensity(bandwidth=0.3).fit(
                entry_data.reshape((-1, 1))
            )
            x = np.linspace(entry_data.min(), entry_data.max(), 1000)
            y = kde.score_samples(x.reshape((-1, 1)))

            ax.plot(x, np.exp(y), linewidth=0.5, color=color)

    if ylim:
        ax.set_ylim(ylim)

    if xlim:
        ax.set_xlim(xlim)

    if callback:
        callback(ax)

    pyplot.settings.set_settings(ax, title, xlabel, ylabel, legend=True)
    pyplot.settings.set_size(fig)

    plt.savefig(filepath)
    plt.close()


def lines(
    data, filepath, title, xlabel, ylabel, legend=True, infodict=None, margins=None
):
    """lines

    :param data: Dict with {'label': data} where data is a numpy array of shape (N, 2),
        or {'label': (data, **kwargs)} were kwargs are the arguments for plot().
    :param filepath: Complete path to file with extension.
    :param title: Title for the plot.
    :param xlabel: Label for x axis.
    :param ylabel: Label for y axis.
    :param legend: True to enable legend,
        or a dict with the parameters for plt.legend(**legend).
    :param infodict: If not None, dict is plotted as table besides line plot.
    """
    if infodict:
        fig, (ax, table_ax) = plt.subplots(1, 2)

        table_data = [[key, str(value)] for key, value in infodict.items()]
        table_ax.table(table_data, loc="center", cellLoc="left")

        table_ax.set_axis_off()
    else:
        fig, ax = plt.subplots()

    for label, line in data.items():
        if isinstance(line, tuple):
            ax.plot(line[0][:, 0], line[0][:, 1], label=label, **line[1])
        else:
            ax.plot(line[:, 0], line[:, 1], label=label, linewidth=0.5)

    pyplot.settings.set_settings(ax, title, xlabel, ylabel, legend)
    pyplot.settings.set_size(fig, margins=margins)

    plt.savefig(filepath)
    plt.close()


def lines_confidence(data, filepath, title, xlabel, ylabel, legend=True):
    """lines_confidence

    :param data: Dict with {'label', data} where data = (line, error) and
        line, error are of shape (N, 2).
    :param filepath: Complete path to file with extension.
    :param title: Title for the plot.
    :param xlabel: Label for x axis.
    :param ylabel: Label for y axis.
    :param legend: True to enable legend.
    """
    _, ax = plt.subplots()

    for label, line_data in data.items():
        line, error = line_data

        ax.plot(line[:, 0], line[:, 1], label=label, linewidth=0.5)

        upper = line[:, 1] + error[:, 1]
        lower = line[:, 1] - error[:, 1]

        ax.fill_between(line[:, 0], lower, upper, alpha=0.1)

    pyplot.settings.set_settings(ax, title, xlabel, ylabel, legend)

    plt.savefig(filepath)
    plt.close()


def scatter(
    points, filepath, title, xlabel, ylabel, legend=True, xlim=None, ylim=None, **kwargs
):
    """scatter.

    :param points: Dict with {key: data} where data has shape (N, 2).
    :param filepath: Complete path to file with extension.
    :param title: Title for the plot.
    :param xlabel: Label for x axis.
    :param ylabel: Label for y axis.
    :param legend: True to enable legend.
    :param ylim: Tuple with (bottom, top) limits for y axis.
    :param xlim: Tuple with (left, right) limits for x axis.
    :param kwargs: Forwarded to ax.scatter.
    """
    for z in points.values():
        if z.shape[1] != 2:
            raise ValueError("Points need to be 2D.")

    fig, ax = plt.subplots()

    for key, data in points.items():
        ax.scatter(data[:, 0], data[:, 1], marker=".", label=key, **kwargs)

    if xlim:
        ax.set_xlim(xlim)

    if ylim:
        ax.set_ylim(ylim)

    pyplot.settings.set_settings(ax, title, xlabel, ylabel, legend)
    pyplot.settings.set_size(fig)

    plt.savefig(filepath)
    plt.close()


def bar_plot(data, filepath, title, xlabel, ylabel):
    """bar_plot.

    :param data: Dict with {key: scalar}.
    :param filepath: Complete path to file with extension.
    :param title: Title for the plot.
    :param xlabel: Label for x axis.
    :param ylabel: Label for y axis.
    """
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values())

    pyplot.settings.set_settings(ax, title, xlabel, ylabel, legend=False)
    pyplot.settings.set_size(fig)

    plt.savefig(filepath)
    plt.close()


def sorted_bar(data, filepath, title, xlabel, ylabel):
    """sorted_bar.

    The color is always the same for each key when you call this function multiple times
    with the same keys but different data.

    :param data: Dict with {key: scalar}.
    :param title: Title for the plot.
    :param xlabel: Label for x axis.
    :param ylabel: Label for y axis.
    """
    fig, ax = plt.subplots()

    # Sort keys
    sorted_keys = sorted(data.keys())
    color_map = pyplot.misc.get_colormap(sorted_keys)

    # Sort values
    sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))
    colors = [color_map[key] for key in sorted_dict.keys()]

    ax.bar(sorted_dict.keys(), sorted_dict.values(), color=colors)

    pyplot.settings.set_settings(ax, title, xlabel, ylabel, legend=False)
    pyplot.settings.set_size(fig)

    plt.savefig(filepath)
    plt.close()
