# -*- coding: utf-8 -*-
# *****************************************************************************
#
# Copyright (c) 2021
# Georgia Institute of Technology
# Tomoki Koike
# <tkoike3@gatech.edu>
#
# *****************************************************************************
#
# DESCRIPTION:
# Utility function file for basic mathematical and auxiliary operations.
#
# LAST EDITED:
# 10-26-2021
#
# *****************************************************************************


# Modules *********************************************************************
import numpy as np


def skew_sym3(vec: np.ndarray) -> np.ndarray:
    """
    skew_sym3

    Transform a 3 dimensional vector to a skew symmetric matrix for cross
    product manipulation.

    Parameters
    ----------
    vec : np.ndarray
        Input 3 dimensional vector.

    Returns
    -------
    np.ndarray:
        Resulting skew symmetric matrix.
    """
    a = np.reshape(vec, (3))  # reshape the input matrix to 1 by 3
    return np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])


def main():
    a = np.array([[1], [3], [4]])
    b = skew_sym3(a)
    print(b)


if __name__ == "__main__":
    main()
