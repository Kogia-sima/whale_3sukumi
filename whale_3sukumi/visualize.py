# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('ggplot')
mpl.rcParams['text.color'] = 'black'
mpl.rcParams['savefig.facecolor'] = 'white'
mpl.rcParams['savefig.bbox'] = 'tight'
mpl.rcParams['axes.labelcolor'] = '#000000'
mpl.rcParams['xtick.color'] = '#000000'
mpl.rcParams['ytick.color'] = '#000000'
mpl.rcParams['legend.facecolor'] = '#ffffff'
mpl.rcParams['lines.linewidth'] = 0.8


def single_result(output_file: str, populations: np.ndarray) -> None:
    assert populations.ndim == 2

    plt.plot(populations[:, 0])
    plt.plot(populations[:, 1])
    plt.plot(populations[:, 2])

    plt.ylim(0.0, np.max(populations) * 1.01)

    plt.savefig(output_file, dpi=300)
    plt.clf()


def alpha_merged(output_file: str, populations: np.ndarray) -> None:
    for population in populations:
        plt.plot(population, alpha=0.5)

    plt.ylim(0.0, np.max(populations) * 1.01)
    plt.savefig(output_file, dpi=300)
    plt.clf()


def all(output_dir: str, all_populations: np.ndarray) -> None:
    assert all_populations.shape[2] == 3

    # data_num = all_populations.shape[0]
    # years = all_populations.shape[1]

    output_file = os.path.join(output_dir, 'single_result.png')
    single_result(output_file, all_populations[0])

    # population results for each species
    species_populations = [
        all_populations[:, :, 0],
        all_populations[:, :, 1],
        all_populations[:, :, 2],
    ]

    for i, species_population in enumerate(species_populations):

        output_file = os.path.join(output_dir, 'alpha_merged_{}.png'.format(i))
        alpha_merged(output_file, species_population)
