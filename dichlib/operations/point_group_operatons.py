#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file provides various kind of calculations about point group oprations.
"""
import numpy as np


def get_all_pog_operations(coord_sys):
    """
    get all point group operations specified coordinate system

    Args:
        coord_sys (str): Put coordinate system of lattice, which must be
          chosen from 'cubic', 'tetragonal', 'orthorhombic',
          'monoclinic', 'hexagonal', 'triclinic' or 'rhombohedral'.

    Returns:
        dict: all point group operations

    Raises:
        ValueError: unexpected coodinate system is specifed

    Examples:
        description

        >>> print_test ("test", "message")
          test message

    Note:
        description
    """
    def __add_dict(symbol,
                   geometric_element,
                   direction,
                   transformed_coord,
                   matrix):
        pog_operations[symbol+'_'+geometric_element] = {
                'symbol': symbol,
                'geometric_element': geometric_element,
                'direction': direction,
                'transformed_coord': transformed_coord,
                'matrix': matrix
            }

    except_hexagol = ['cubic',
                      'tetragonal',
                      'orthorhombic',
                      'monoclinic',
                      'triclinic',
                      'rhombohedral']

    pog_operations = {}
    if coord_sys in except_hexagol:
        __add_dict(
                symbol = '1',
                geometric_element = '',
                direction = '',
                transformed_coord = 'x,y,z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '3+',
                geometric_element = 'x,x,x',
                direction = np.array([1,1,1]),
                transformed_coord = 'z,x,y',
                matrix = np.array([[ 0,  0,  1],
                                   [ 1,  0,  0],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                symbol = '3-',
                geometric_element = 'x,x,x',
                direction = np.array([1,1,1]),
                transformed_coord = 'y,z,x',
                matrix = np.array([[ 0,  1,  0],
                                   [ 0,  0,  1],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                symbol = '-1',
                geometric_element = '0,0,0',
                direction = '',
                transformed_coord = '-x,-y,-z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '-3+',
                geometric_element = 'x,x,x',
                direction = np.array([1,1,1]),
                transformed_coord = '-z,-x,-y',
                matrix = np.array([[ 0,  0, -1],
                                   [-1,  0,  0],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                symbol = '-3-',
                geometric_element = 'x,x,x',
                direction = np.array([1,1,1]),
                transformed_coord = '-y,-z,-x',
                matrix = np.array([[ 0, -1,  0],
                                   [ 0,  0, -1],
                                   [-1,  0,  0]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-x,-y,z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '3+',
                geometric_element = 'x,-x,-x',
                direction = np.array([1,-1,-1]),
                transformed_coord = '-z,-x,y',
                matrix = np.array([[ 0,  0, -1],
                                   [-1,  0,  0],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                symbol = '3-',
                geometric_element = 'x,-x,-x',
                direction = np.array([1,-1,-1]),
                transformed_coord = '-y,z,-x',
                matrix = np.array([[ 0, -1,  0],
                                   [ 0,  0,  1],
                                   [-1,  0,  0]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = 'x,x,0',
                direction = np.array([1,1,0]),
                transformed_coord = 'y,x,-z',
                matrix = np.array([[ 0,  1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = 'x,-x,0',
                direction = np.array([1,-1,0]),
                transformed_coord = '-y,-x,-z',
                matrix = np.array([[ 0, -1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '4+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-y,x,z',
                matrix = np.array([[ 0, -1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '4-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y,-x,z',
                matrix = np.array([[ 0,  1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,y,0',
                direction = np.array([0,0,1]),
                transformed_coord = 'x,y,-z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '-3+',
                geometric_element = 'x,-x,-x',
                direction = np.array([1,-1,-1]),
                transformed_coord = 'z,x,-y',
                matrix = np.array([[ 0,  0,  1],
                                   [ 1,  0,  0],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                symbol = '-3-',
                geometric_element = 'x,-x,-x',
                direction = np.array([1,-1,-1]),
                transformed_coord = 'y,-z,x',
                matrix = np.array([[ 0,  1,  0],
                                   [ 0,  0, -1],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,-x,z',
                direction = np.array([1,1,0]),
                transformed_coord = '-y,-x,z',
                matrix = np.array([[ 0, -1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,x,z',
                direction = np.array([1,-1,0]),
                transformed_coord = 'y,x,z',
                matrix = np.array([[ 0,  1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '-4+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y,-x,-z',
                matrix = np.array([[ 0,  1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '-4-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-y,x,-z',
                matrix = np.array([[ 0, -1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = '-x,y,-z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '3+',
                geometric_element = '-x,x,-x',
                direction = np.array([-1,1,-1]),
                transformed_coord = 'z,-x,-y',
                matrix = np.array([[ 0,  0,  1],
                                   [-1,  0,  0],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                symbol = '3-',
                geometric_element = '-x,x,-x',
                direction = np.array([-1,1,-1]),
                transformed_coord = '-y,-z,x',
                matrix = np.array([[ 0, -1,  0],
                                   [ 0,  0, -1],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = 'x,0,x',
                direction = np.array([1,0,1]),
                transformed_coord = 'z,-y,x',
                matrix = np.array([[ 0,  0,  1],
                                   [ 0, -1,  0],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = '-x,0,x',
                direction = np.array([-1,0,1]),
                transformed_coord = '-z,-y,-x',
                matrix = np.array([[ 0,  0, -1],
                                   [ 0, -1,  0],
                                   [-1,  0,  0]])
            )
        __add_dict(
                symbol = '4+',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = 'z,y,-x',
                matrix = np.array([[ 0,  0,  1],
                                   [ 0,  1,  0],
                                   [-1,  0,  0]])
            )
        __add_dict(
                symbol = '4-',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = '-z,y,x',
                matrix = np.array([[ 0,  0, -1],
                                   [ 0,  1,  0],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,0,z',
                direction = np.array([0,1,0]),
                transformed_coord = 'x,-y,z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '-3+',
                geometric_element = '-x,x,-x',
                direction = np.array([-1,1,-1]),
                transformed_coord = '-z,x,y',
                matrix = np.array([[ 0,  0, -1],
                                   [ 1,  0,  0],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                symbol = '-3-',
                geometric_element = '-x,x,-x',
                direction = np.array([-1,1,-1]),
                transformed_coord = 'y,z,-x',
                matrix = np.array([[ 0,  1,  0],
                                   [ 0,  0,  1],
                                   [-1,  0,  0]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = '-x,y,x',
                direction = np.array([1,0,1]),
                transformed_coord = '-z,y,-x',
                matrix = np.array([[ 0,  0, -1],
                                   [ 0,  1,  0],
                                   [-1,  0,  0]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,y,x',
                direction = np.array([-1,0,1]),
                transformed_coord = 'z,y,x',
                matrix = np.array([[ 0,  0,  1],
                                   [ 0,  1,  0],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                symbol = '-4+',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = '-z,-y,x',
                matrix = np.array([[ 0,  0, -1],
                                   [ 0, -1,  0],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                symbol = '-4-',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = 'z,-y,-x',
                matrix = np.array([[ 0,  0,  1],
                                   [ 0, -1,  0],
                                   [-1,  0,  0]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = 'x,-y,-z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '3+',
                geometric_element = '-x,-x,x',
                direction = np.array([-1,-1,1]),
                transformed_coord = '-z,x,-y',
                matrix = np.array([[ 0,  0, -1],
                                   [ 1,  0,  0],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                symbol = '3-',
                geometric_element = '-x,-x,x',
                direction = np.array([-1,-1,1]),
                transformed_coord = 'y,-z,-x',
                matrix = np.array([[ 0,  1,  0],
                                   [ 0,  0, -1],
                                   [-1,  0,  0]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = '0,y,y',
                direction = np.array([0,1,1]),
                transformed_coord = '-x,z,y',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  0,  1],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = '0,y,-y',
                direction = np.array([0,1,-1]),
                transformed_coord = '-x,-z,-y',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  0, -1],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                symbol = '4+',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = 'x,-z,y',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  0, -1],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                symbol = '4-',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = 'x,z,-y',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  0,  1],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = '0,y,z',
                direction = np.array([1,0,0]),
                transformed_coord = '-x,y,z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '-3+',
                geometric_element = '-x,-x,x',
                direction = np.array([-1,-1,1]),
                transformed_coord = 'z,-x,y',
                matrix = np.array([[ 0,  0,  1],
                                   [-1,  0,  0],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                symbol = '-3-',
                geometric_element = '-x,-x,x',
                direction = np.array([-1,-1,1]),
                transformed_coord = '-y,z,x',
                matrix = np.array([[ 0, -1,  0],
                                   [ 0,  0,  1],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,y,-y',
                direction = np.array([0,1,1]),
                transformed_coord = 'x,-z,-y',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  0, -1],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,y,y',
                direction = np.array([0,1,-1]),
                transformed_coord = 'x,z,y',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  0,  1],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                symbol = '-4+',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = '-x,z,-y',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  0,  1],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                symbol = '-4-',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = '-x,-z,y',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  0, -1],
                                   [ 0,  1,  0]])
            )

    elif coord_sys == 'hexagonal':
        __add_dict(
                symbol = '1',
                geometric_element = '',
                direction = '',
                transformed_coord = 'x,y,z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-x,-y,z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = 'x,x,0',
                direction = np.array([1,1,0]),
                transformed_coord = 'y,x,-z',
                matrix = np.array([[ 0,  1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = 'x,-x,0',
                direction = np.array([1,-1,0]),
                transformed_coord = '-y,-x,-z',
                matrix = np.array([[ 0, -1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '-1',
                geometric_element = '0,0,0',
                direction = '',
                transformed_coord = '-x,-y,-z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,y,0',
                direction = np.array([0,0,1]),
                transformed_coord = 'x,y,-z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,-x,z',
                direction = np.array([1,1,0]),
                transformed_coord = '-y,-x,z',
                matrix = np.array([[ 0, -1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,x,z',
                direction = np.array([1,-1,0]),
                transformed_coord = 'y,x,z',
                matrix = np.array([[ 0,  1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '3+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-y,x-y,z',
                matrix = np.array([[ 0, -1,  0],
                                   [ 1, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '6+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'x-y,x,z',
                matrix = np.array([[ 1, -1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = 'x-y,-y,-z',
                matrix = np.array([[ 1, -1,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = 'x,2x,0',
                direction = np.array([1,2,0]),
                transformed_coord = 'y-x,y,-z',
                matrix = np.array([[-1,  1,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '-3+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y,y-x,-z',
                matrix = np.array([[ 0,  1,  0],
                                   [-1,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '-6+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y-x,-x,-z',
                matrix = np.array([[-1,  1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x,2x,z',
                direction = np.array([1,0,0]),
                transformed_coord = 'y-x,y,z',
                matrix = np.array([[-1,  1,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = 'x0z',
                direction = np.array([1,2,0]),
                transformed_coord = 'x-y,-y,z',
                matrix = np.array([[ 1, -1,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '3-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y-x,-x,z',
                matrix = np.array([[-1,  1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '6-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y,y-x,z',
                matrix = np.array([[ 0,  1,  0],
                                   [-1,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = '-x,y-x,-z',
                matrix = np.array([[-1,  0,  0],
                                   [-1,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '2',
                geometric_element = '2x,x,0',
                direction = np.array([2,1,0]),
                transformed_coord = 'x,x-y,-z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 1, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '-3-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'x-y,x,-z',
                matrix = np.array([[ 1, -1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = '-6-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-y,x-y,-z',
                matrix = np.array([[ 0, -1,  0],
                                   [ 1, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = '2x,x,z',
                direction = np.array([0,1,0]),
                transformed_coord = 'x,x-y,z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 1, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                symbol = 'm',
                geometric_element = '0,y,z',
                direction = np.array([2,1,0]),
                transformed_coord = '-x,y-x,z',
                matrix = np.array([[-1,  0,  0],
                                   [-1,  1,  0],
                                   [ 0,  0,  1]])
            )

    else:
        raise ValueError("unexpected coodinate system is specifed ")

    return pog_operations
