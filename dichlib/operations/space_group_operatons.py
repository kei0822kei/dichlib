#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file provides various kind of calculations about space group oprations.
"""
import numpy as np
from dichlib.operations import point_group_operatons

def get_Ww(W, w):
    """
    get 4 x 4 matrix Ww from the operation
    of rotation part W and translation part w

    Args:
        W (3x3 numpy array): rotation part (3 x 3) of space group operation
        w (numpy array): translation part (3) of space group operation

    Returns:
        array: concatted space group operaton (4 x 4)

    Raises:
        ValueError: description

    Examples:
        description

        >>> print_test ("test", "message")
          test message

    Note:
        description
    """
    Ww = np.concatenate([W, w.reshape(3,1)], axis=1)
    Ww = np.concatenate([Ww, np.array([0,0,0,1]).reshape(1,4)], axis=0)
    return Ww


def get_index(W, w, get_translation=False):
    """
    get index of |(W, w)| (mod tau)
    tau means translation operation

    Args:
        W (3x3 numpy array): rotation part (3 x 3) of space group operation
        w (numpy array): translation part (3) of space group operation
        get_translation (bool) (optional): If True, return translation
          part when rotation part becomes identity matrix.

    Returns:
        int: index of space group operation (W, w)
        array: translation part when rotation part becomes identity matrix

    Raises:
        ValueError: could not detect index of the operation

    Examples:
        description

        >>> print_test ("test", "message")
          test message

    Note:
        description
    """
    epsilon = 1e-8
    n_max = 10
    Ww_n = np.eye(4, dtype=float)
    Ww = get_Ww(W, w)
    for n in range(1, n_max+1):
        Ww_n = np.dot(Ww_n, Ww)
        if np.all(abs(Ww_n[:3, :3] - np.eye(3)) < epsilon):
            break
        if n == n_max:
            raise ValueError("could not detect index of the operation")
    if get_translation:
        return n, Ww_n[:3, 3]
    else:
        return n


def get_separated_translation_part(W, w):
    """
    get separated translation part from translation part w

    Args:
        W (3x3 numpy array): rotation part (3 x 3) of space group operation
        w (numpy array): translation part (3) of space group operation

    Returns:
        tuple: (w_intr, w_loc)

    Raises:
        ValueError: description

    Examples:
        description

        >>> print_test ("test", "message")
          test message

    Note:
        description
    """
    index, total_translation = get_index(W, w, get_translation=True)
    w_intr = total_translation / index
    w_loc = w - w_intr
    return (w_intr, w_loc)


def get_detailed_spg_operation(W, w, coord_sys=None):
    """
    get detailed space group operation information
    such as intrinsic part of translation operation

    Args:
        W (3x3 numpy array): rotation part (3 x 3) of space group operation
        w (numpy array): translation part (3) of space group operation
        coord_sys (str) (optional): If you set coordinate system such as
          'monoclinic', 'W_detail' key is added in the output dict.

    Returns:
        dict: description

    Raises:
        ValueError: could not detect index of the operation

    Examples:
        description

        >>> print_test ("test", "message")
          test message

    Note:
        description
    """
    w_sep = get_separated_translation_part(W, w)
    spg_operation = {
        'W': W,
        'w': w,
        'w_intr': w_sep[0],
        'w_loc': w_sep[1],
        'W_index': get_index(W, w)
    }
    if coord_sys is not None:
        spg_operation['W_detail'] = \
            point_group_operatons.get_operation_detail(W, coord_sys)

    return spg_operation
