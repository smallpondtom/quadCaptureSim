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
