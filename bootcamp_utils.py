"""Contains utilities and code for use in the 2017 Python bootcamp."""

import numpy as np

def ecdf(data):
    """Compute x, y values for an empirical distribution function."""

    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)

    return x, y
