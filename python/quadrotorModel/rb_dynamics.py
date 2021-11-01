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
# Rigid body dynamics model of a quadrotor.
#
# LAST EDITED:
# 10-26-2021
#
# *****************************************************************************


# Modules *********************************************************************
from dataclasses import dataclass
import constants
import numpy as np
import utils


# Class
@dataclass(order=False, frozen=False)
class RBDYNAMICS:
    m: float  # mass of the quadrotor
    I: np.ndarray  # constant inertia matrix R[3x3]


small: int
