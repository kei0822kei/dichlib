#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file provides various kind of calculations about space group oprations.
"""
import numpy as np

def get_Ww(W, w):
    """
    get 4 x 4 matrix Ww from the operation
    of rotation part W and translation part w

        Parameters
        ----------
        W : array_like
            rotation part (3 x 3) of space group operation
        w : array_like
            translation part (3) of space group operation

        Returns
        -------
        Ww : array_like
            concatted space group operaton (4 x 4)

        Notes
        -----

        Raises
        ------
    """
    Ww = np.concatenate([W, w.reshape(3,1)], axis=1)
    Ww = np.concatenate([Ww, np.array([0,0,0,1]).reshape(1,4)], axis=0)
    return Ww

def get_detailed_spg_operation(W, w):
    """
    get detailed space group operation information
    such as intrinsic part of translation operation

        Parameters
        ----------
        W : np.array
            rotation part (3 x 3) of space group operation
        w : np.array
            translation part (3) of space group operation

        Returns
        -------
        spg_operation : dict
            informations about a given space group operation

        Notes
        -----

        Raises
        ------
        ValueError
            could not detect index of the operation
    """
    epsilon = 1e-8
    n_max = 20

    Ww_n = np.eye(4, dtype=float)
    Ww = get_Ww(W, w)
    for n in range(1, n_max+1):
        Ww_n = np.dot(Ww_n, Ww)
        if np.all(abs(Ww_n[:3, :3] - np.eye(3)) < epsilon):
            break
        if n == n_max:
            raise ValueError("could not detect index of the operation")
    w_intr = Ww[:3, 3] / n
    spg_operation = {
        'W': W,
        'w': w,
        'w_intr': w_intr,
        'w_loc': w - w_intr,
        'W_index': n
    }
    return spg_operation
