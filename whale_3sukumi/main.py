#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Dict

import os
import sys
import traceback
import json
import argparse
import numpy as np

from whale_3sukumi import simulator
from whale_3sukumi import visualize


def load_data(filename: str) -> Dict[str, np.ndarray]:
    with open(filename, 'r') as fp:
        data = json.load(fp)

    for key in ['A', 'r', 'c', 'w']:
        if key not in data.keys():
            raise Exception('invalid file format')

        data[key] = np.array(data[key])

    return data


def argparser(args: List[str] = sys.argv[1:]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Whale 3-sukumi hypothesis simulation'
    )
    parser.add_argument(
        'param_file', type=str,
        help='JSON file that contains simulation parameters'
    )
    parser.add_argument(
        '--years', type=int, default=150,
        help='Number of transitions for each simulation'
    )
    parser.add_argument(
        '--nums', type=int, default=100,
        help='Number of simulations to be executed'
    )
    parser.add_argument(
        '--output', default='output',
        help='output directory to which the simulation results are saved'
    )

    return parser.parse_args(args)


def main() -> None:
    try:
        args = argparser()

        data = load_data(args.param_file)
        sim = simulator.Simulator(**data)

        initial_value = np.ones((3,), dtype=np.float64)
        all_populations = np.ndarray((args.nums, args.years, 3))

        # simulate
        for i in range(args.nums):
            all_populations[i, :, :] = sim(initial_value, args.years)

        # create output_directory
        os.makedirs(args.output, exist_ok=True)

        np.save(os.path.join(args.output, 'data.npy'), all_populations)
        visualize.all(args.output, all_populations)

    except Exception:
        traceback.print_exc()
        sys.exit(2)


if __name__ == '__main__':
    main()
