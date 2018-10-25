# -*- coding: utf-8 -*-

import numpy as np


class Simulator(object):
    """
    Simulator object for 3-sukumi hypothesis.
    """

    def __init__(self, A: np.ndarray, r: np.ndarray, c: np.ndarray,
                 w: np.ndarray) -> None:
        assert A.shape == (3, 3)
        assert r.shape == (3,)
        assert c.shape == (3,)

        self.A = A
        self.r = r
        self.c = c
        self.w = w

    def __call__(self, initial_value: np.ndarray = None,
                 count: int = 1) -> np.ndarray:
        if initial_value is None:
            initial_value = np.ones((3,), np.float64)
        else:
            assert initial_value.shape == (3,)

        # hold all population histories for 3 species
        populations = np.ndarray((count, 3), dtype=np.float64)
        populations[0, :] = initial_value

        for i in range(count - 1):
            # random effect
            rnd = np.random.randn(3) * 0.1

            consumption = self.w * populations[i, :] / np.sum(populations[i, :])

            # transition
            populations[i + 1, :] = self.c + populations[i, :] *\
                (np.exp(self.r + rnd - np.dot(self.A, populations[i, :])) -
                 consumption)

        return populations
