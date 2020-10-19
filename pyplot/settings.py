import matplotlib.pyplot as plt

default_margins_inches = {'left': 0.5, 'right': 0.5, 'top': 0.5, 'bottom': 0.5}
default_size = (3, 2)


def set_settings(title, xlabel, ylabel, legend, size=None, margins=None):
    if not size:
        size = default_size

    if not margins:
        margins = {
            'left': default_margins_inches['left'] / size[0],
            'right': 1 - default_margins_inches['right'] / size[0],
            'top': 1 - default_margins_inches['top'] / size[1],
            'bottom': default_margins_inches['bottom'] / size[1]
        }

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.subplots_adjust(**margins)
    plt.minorticks_on()

    plt.grid(which='major', linestyle='-', linewidth=0.1)
    plt.gcf().set_size_inches(size, forward=True)

    if legend:
        plt.legend()
