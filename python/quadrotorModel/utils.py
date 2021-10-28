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
import numba as nb


@nb.jit
def inv_npmat_jit(mat: np.ndarray) -> np.ndarray:
    """
    inv_npmat_jit

    Fast matrix inversion using numba and numpy.

    Parameters
    ----------
    mat : np.ndarray
        Input matrix.
    """
    return np.linalg.inv(mat)

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
    a = np.reshape(vec, (1, 3))  # reshape the input matrix to 1 by 3
    return np.ndarray([[0, a[3], a[2]], [a[3], 0, -a[1]], -a[2], a[1], 0])










