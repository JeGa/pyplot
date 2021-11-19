import matplotlib.pyplot as plt

import pathlib
import numpy as np
import pyplot.basic
import pyplot.images


output_dir = pathlib.Path("examples")


def examples_basic():
    bar1 = {"1": 10, "2": 3, "3": 30}
    bar2 = {"1": 1, "2": 10, "3": 2}

    pyplot.basic.sorted_bar(
        bar1,
        output_dir / "sorted_bar1.pdf",
        title="bar1",
        xlabel="xlabel",
        ylabel="ylabel",
    )

    pyplot.basic.sorted_bar(
        bar2,
        output_dir / "sorted_bar2.pdf",
        title="bar2",
        xlabel="xlabel",
        ylabel="ylabel",
    )

    pyplot.basic.bar_plot(
        bar1, output_dir / "bar.pdf", title="bar", xlabel="xlabel", ylabel="ylabel"
    )

    N = 200
    x1 = np.concatenate(
        (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
    )
    x2 = np.concatenate(
        (np.random.normal(3, 1, int(0.3 * N)), np.random.normal(8, 1, int(0.7 * N)))
    )

    pyplot.basic.histogram(
        {"test1": x1, "test2": x2},
        output_dir / "hist.pdf",
        title="",
        xlabel="",
        ylabel="",
    )


def examples_image():
    images = np.random.randn(4, 3, 32, 32)
    titles = ["1", "2", "3", "4"]

    pyplot.images.image_grid(
        images, output_dir / "image_grid.pdf", "test", titles, padding=0.3
    )

    gridsize = pyplot.images.get_grid_size(images.shape[0])

    fig, _ = plt.subplots(2, 2)

    pyplot.images.subgrid(fig, (2, 2, 1), images, gridsize, padding=0.2)
    pyplot.images.subgrid(fig, (2, 2, 4), images, gridsize, padding=0.2)

    plt.savefig(output_dir / "subgrid.pdf")


if __name__ == "__main__":
    # examples_basic()
    examples_image()
