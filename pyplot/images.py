import numpy as np
import matplotlib.pyplot as plt


def image_grid(images, gray, filepath=None):
    """
    :param images: Numpy array with shape (batch_size, height, width, channels).
    :param gray: If True, the grayvalue color map is used.
    :param filepath: If not None, the image is saved as 'filepath'.
    """
    rows, cols = get_grid_size(images.shape[0])

    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=images.shape[1:3])
    axes = axes.flatten()

    for img, ax in zip(images, axes):
        img = np.squeeze(img)

        if gray:
            cmap = 'gray'
        else:
            cmap = None

        ax.imshow(img, cmap=cmap)
        ax.axis('off')

    plt.tight_layout()

    if filepath:
        plt.savefig(filepath)
    else:
        plt.show()


def image(image_data, gray, filepath=None):
    """
    :param image_data: Numpy array with shape (height, width, channels).
    :param gray: If True, the grayvalue color map is used.
    :param filepath: If not None, the image is saved as 'filepath'.
    """
    if gray:
        cmap = 'gray'
    else:
        cmap = None

    plt.imshow(image_data.squeeze(), cmap=cmap)
    plt.axis('off')

    if filepath:
        plt.savefig(filepath, bbox_inches='tight')
    else:
        plt.show()

def get_grid_size(n):
    """
    Returns rows and columns so that n images fit into the grid.

    :returns: (rows, columns)
    """
    sqrt = np.sqrt(n)

    if n % sqrt == 0:
        return (int(sqrt),) * 2

    return int(sqrt), int(sqrt) + 1
