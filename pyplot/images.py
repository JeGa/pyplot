import math

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid1


def _image_reshape(_image):
    if _image.shape[0] == 1:
        cmap = "gray"
        _image = np.squeeze(_image)
    else:
        cmap = None
        _image = np.moveaxis(_image, 0, -1)

    return _image, cmap


def subgrid(fig, pos, images, gridsize, padding, titles=None):
    """
    Plot image grid on an existing plot.
    Be sure to create the axes for the subgrid before.

    :param fig: Matplotlib figure to plot on.
    :param pos: Position of the plot with tuple (nrows, ncols, index).
    :param images: Numpy array with shape (n, channels, height, width).
    :param gridsize: Size of the grid (rows, cols).
    :param padding: Padding between the images.
    :param titles: List of titles or None.
    """
    _grid = mpl_toolkits.axes_grid1.ImageGrid(
        fig, pos, nrows_ncols=gridsize, axes_pad=padding
    )
    _grid = [i for i in _grid]

    for i in range(images.shape[0]):
        img, cmap = _image_reshape(images[i])
        _grid[i].imshow(img, cmap=cmap)

        if titles:
            _grid[i].set_title(titles[i])

    for ax in _grid:
        ax.set_axis_off()


def image_grid(images, filepath, title, subtitles=None, padding=0.01):
    """image_grid

    :param images: Numpy array with shape (batch_size, channels, height, width).
    :param filepath: Full path with extension to save to.
    :param title: Figure title.
    :param subtitles: List of titles for each image.
    :param padding: Padding between images.
    """
    rows, cols = get_grid_size(images.shape[0])

    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(3, 3))
    axes = axes.flatten()

    fig.suptitle(title)

    for i, (img, ax) in enumerate(zip(images, axes)):
        img, cmap = _image_reshape(img)
        ax.imshow(img, cmap=cmap, aspect="auto")

        if subtitles is not None:
            ax.set_title(subtitles[i])

    for ax in axes:
        ax.set_axis_off()

    fig.subplots_adjust(
        wspace=padding,
        hspace=padding,
        left=0.05,
        right=0.95,
        top=0.95,
        bottom=0.05,
    )

    plt.savefig(filepath)


def image(_image, filepath, **kwargs):
    """image

    :param _image: Numpy array with shape (channels, height, width).
    :param filepath: Full path with extension to save to.
    :param kwargs: Gets forwarded to imshow.
    """
    _image, cmap = _image_reshape(_image)

    _, ax = plt.subplots()

    ax.imshow(_image.squeeze(), cmap=cmap, **kwargs)
    ax.axis("off")

    plt.savefig(filepath, bbox_inches="tight")


def get_grid_size(n, square=True):
    """get_grid_size

    Returns rows and columns so that n images fit into the grid.

    :param n: Number of images.
    :param square: If True, always returns rows == columns.

    :returns: (rows, columns)
    """
    if n < 1:
        raise ValueError("n needs to be at least one")

    num = math.ceil(math.sqrt(n))

    col = row = num

    if square:
        return row, col

    if n <= (num * (num - 1)):
        row = num - 1

    return row, col


def test():
    for i in range(1, 17):
        print(i, get_grid_size(i))
