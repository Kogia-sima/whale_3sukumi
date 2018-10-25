#!/usr/bin/env python3
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

DATA_FILES = ['output/0/data.npy', 'output/1/data.npy']


def main() -> None:
    data_0 = np.load(DATA_FILES[0])
    data_1 = np.load(DATA_FILES[1])

    data_0_mins = np.min(data_0, axis=1)
    data_1_mins = np.min(data_1, axis=1)

    output_dir = 'output/compare_results'
    os.makedirs(output_dir, exist_ok=True)

    for i in range(3):
        output_file = os.path.join(output_dir, 'compare_{}.png'.format(i))

        data_0_min = data_0_mins[:, i]
        data_1_min = data_1_mins[:, i]

        ax = plt.gca()
        ax.boxplot([data_0_min, data_1_min])
        ax.set_xticklabels(['without consumption', 'with consumption'])

        plt.ylim([0, None])
        plt.ylabel('minimum population')
        plt.savefig(output_file, dpi=300)
        plt.clf()


if __name__ == '__main__':
    main()
