default_margins_inches = {"left": 0.5, "right": 0.5, "top": 0.4, "bottom": 0.4}
default_size = (3, 2)


def set_size(fig, size=None, margins=None):
    if not size:
        size = default_size

    if not margins:
        margins = {
            "left": default_margins_inches["left"] / size[0],
            "right": 1 - default_margins_inches["right"] / size[0],
            "top": 1 - default_margins_inches["top"] / size[1],
            "bottom": default_margins_inches["bottom"] / size[1],
        }

    fig.subplots_adjust(**margins)
    fig.set_size_inches(size, forward=True)


def set_settings(ax, title, xlabel="", ylabel="", legend=True):
    ax.minorticks_on()
    ax.grid(which="major", linestyle="-", linewidth=0.1)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if legend:
        ax.legend()
