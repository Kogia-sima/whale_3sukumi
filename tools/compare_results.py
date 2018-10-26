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

DATA_FILES = ['../whale_3sukumi/output/0/data.npy',
              '../whale_3sukumi/output/1/data.npy',
              '../whale_3sukumi/output/2/data.npy']


def main() -> None:
    all_data = [np.load(f) for f in DATA_FILES]

    output_dir = '../whale_3sukumi/output/compare_results'
    os.makedirs(output_dir, exist_ok=True)

    for i in range(3):
        output_file = os.path.join(output_dir, 'compare_{}.png'.format(i))

        each_mins = [np.min(data[:, :, i], axis=1) for data in all_data]

        ax = plt.gca()
        ax.boxplot(each_mins)
        ax.set_xticklabels(['w=0.0', 'w=0.1', 'w=0.2'])

        plt.ylim([0, None])
        plt.ylabel('minimum population')
        plt.savefig(output_file, dpi=300)
        plt.clf()


if __name__ == '__main__':
    main()
