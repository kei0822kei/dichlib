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
        In this definition, point group operation number (pognum) is
        defined. Each number is determined in order of Table 1.2.2.1 and
        Tabke 1.2.2.2 in International Table Vol.A. Some of the operations
        in hexagonal system correspond with the ones in the operations of the
        other crystal systems.
    """
    def __add_dict(pognum,
                   symbol,
                   geometric_element,
                   direction,
                   transformed_coord,
                   matrix):
        pog_operations[pognum] = {
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
                pognum = '1',
                symbol = '1',
                geometric_element = None,
                direction = None,
                transformed_coord = 'x,y,z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '2',
                symbol = '3+',
                geometric_element = 'x,x,x',
                direction = np.array([1,1,1]),
                transformed_coord = 'z,x,y',
                matrix = np.array([[ 0,  0,  1],
                                   [ 1,  0,  0],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                pognum = '3',
                symbol = '3-',
                geometric_element = 'x,x,x',
                direction = np.array([1,1,1]),
                transformed_coord = 'y,z,x',
                matrix = np.array([[ 0,  1,  0],
                                   [ 0,  0,  1],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                pognum = '4',
                symbol = '-1',
                geometric_element = '0,0,0',
                direction = None,
                transformed_coord = '-x,-y,-z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '5',
                symbol = '-3+',
                geometric_element = 'x,x,x',
                direction = np.array([1,1,1]),
                transformed_coord = '-z,-x,-y',
                matrix = np.array([[ 0,  0, -1],
                                   [-1,  0,  0],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                pognum = '6',
                symbol = '-3-',
                geometric_element = 'x,x,x',
                direction = np.array([1,1,1]),
                transformed_coord = '-y,-z,-x',
                matrix = np.array([[ 0, -1,  0],
                                   [ 0,  0, -1],
                                   [-1,  0,  0]])
            )
        __add_dict(
                pognum = '7',
                symbol = '2',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-x,-y,z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '8',
                symbol = '3+',
                geometric_element = 'x,-x,-x',
                direction = np.array([1,-1,-1]),
                transformed_coord = '-z,-x,y',
                matrix = np.array([[ 0,  0, -1],
                                   [-1,  0,  0],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                pognum = '9',
                symbol = '3-',
                geometric_element = 'x,-x,-x',
                direction = np.array([1,-1,-1]),
                transformed_coord = '-y,z,-x',
                matrix = np.array([[ 0, -1,  0],
                                   [ 0,  0,  1],
                                   [-1,  0,  0]])
            )
        __add_dict(
                pognum = '10',
                symbol = '2',
                geometric_element = 'x,x,0',
                direction = np.array([1,1,0]),
                transformed_coord = 'y,x,-z',
                matrix = np.array([[ 0,  1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '11',
                symbol = '2',
                geometric_element = 'x,-x,0',
                direction = np.array([1,-1,0]),
                transformed_coord = '-y,-x,-z',
                matrix = np.array([[ 0, -1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '12',
                symbol = '4+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-y,x,z',
                matrix = np.array([[ 0, -1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '13',
                symbol = '4-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y,-x,z',
                matrix = np.array([[ 0,  1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '14',
                symbol = 'm',
                geometric_element = 'x,y,0',
                direction = np.array([0,0,1]),
                transformed_coord = 'x,y,-z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '15',
                symbol = '-3+',
                geometric_element = 'x,-x,-x',
                direction = np.array([1,-1,-1]),
                transformed_coord = 'z,x,-y',
                matrix = np.array([[ 0,  0,  1],
                                   [ 1,  0,  0],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                pognum = '16',
                symbol = '-3-',
                geometric_element = 'x,-x,-x',
                direction = np.array([1,-1,-1]),
                transformed_coord = 'y,-z,x',
                matrix = np.array([[ 0,  1,  0],
                                   [ 0,  0, -1],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                pognum = '17',
                symbol = 'm',
                geometric_element = 'x,-x,z',
                direction = np.array([1,1,0]),
                transformed_coord = '-y,-x,z',
                matrix = np.array([[ 0, -1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '18',
                symbol = 'm',
                geometric_element = 'x,x,z',
                direction = np.array([1,-1,0]),
                transformed_coord = 'y,x,z',
                matrix = np.array([[ 0,  1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '19',
                symbol = '-4+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y,-x,-z',
                matrix = np.array([[ 0,  1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '20',
                symbol = '-4-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-y,x,-z',
                matrix = np.array([[ 0, -1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '21',
                symbol = '2',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = '-x,y,-z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '22',
                symbol = '3+',
                geometric_element = '-x,x,-x',
                direction = np.array([-1,1,-1]),
                transformed_coord = 'z,-x,-y',
                matrix = np.array([[ 0,  0,  1],
                                   [-1,  0,  0],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                pognum = '23',
                symbol = '3-',
                geometric_element = '-x,x,-x',
                direction = np.array([-1,1,-1]),
                transformed_coord = '-y,-z,x',
                matrix = np.array([[ 0, -1,  0],
                                   [ 0,  0, -1],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                pognum = '24',
                symbol = '2',
                geometric_element = 'x,0,x',
                direction = np.array([1,0,1]),
                transformed_coord = 'z,-y,x',
                matrix = np.array([[ 0,  0,  1],
                                   [ 0, -1,  0],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                pognum = '25',
                symbol = '2',
                geometric_element = '-x,0,x',
                direction = np.array([-1,0,1]),
                transformed_coord = '-z,-y,-x',
                matrix = np.array([[ 0,  0, -1],
                                   [ 0, -1,  0],
                                   [-1,  0,  0]])
            )
        __add_dict(
                pognum = '26',
                symbol = '4+',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = 'z,y,-x',
                matrix = np.array([[ 0,  0,  1],
                                   [ 0,  1,  0],
                                   [-1,  0,  0]])
            )
        __add_dict(
                pognum = '27',
                symbol = '4-',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = '-z,y,x',
                matrix = np.array([[ 0,  0, -1],
                                   [ 0,  1,  0],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                pognum = '28',
                symbol = 'm',
                geometric_element = 'x,0,z',
                direction = np.array([0,1,0]),
                transformed_coord = 'x,-y,z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '29',
                symbol = '-3+',
                geometric_element = '-x,x,-x',
                direction = np.array([-1,1,-1]),
                transformed_coord = '-z,x,y',
                matrix = np.array([[ 0,  0, -1],
                                   [ 1,  0,  0],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                pognum = '30',
                symbol = '-3-',
                geometric_element = '-x,x,-x',
                direction = np.array([-1,1,-1]),
                transformed_coord = 'y,z,-x',
                matrix = np.array([[ 0,  1,  0],
                                   [ 0,  0,  1],
                                   [-1,  0,  0]])
            )
        __add_dict(
                pognum = '31',
                symbol = 'm',
                geometric_element = '-x,y,x',
                direction = np.array([1,0,1]),
                transformed_coord = '-z,y,-x',
                matrix = np.array([[ 0,  0, -1],
                                   [ 0,  1,  0],
                                   [-1,  0,  0]])
            )
        __add_dict(
                pognum = '32',
                symbol = 'm',
                geometric_element = 'x,y,x',
                direction = np.array([-1,0,1]),
                transformed_coord = 'z,y,x',
                matrix = np.array([[ 0,  0,  1],
                                   [ 0,  1,  0],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                pognum = '33',
                symbol = '-4+',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = '-z,-y,x',
                matrix = np.array([[ 0,  0, -1],
                                   [ 0, -1,  0],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                pognum = '34',
                symbol = '-4-',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = 'z,-y,-x',
                matrix = np.array([[ 0,  0,  1],
                                   [ 0, -1,  0],
                                   [-1,  0,  0]])
            )
        __add_dict(
                pognum = '35',
                symbol = '2',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = 'x,-y,-z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '36',
                symbol = '3+',
                geometric_element = '-x,-x,x',
                direction = np.array([-1,-1,1]),
                transformed_coord = '-z,x,-y',
                matrix = np.array([[ 0,  0, -1],
                                   [ 1,  0,  0],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                pognum = '37',
                symbol = '3-',
                geometric_element = '-x,-x,x',
                direction = np.array([-1,-1,1]),
                transformed_coord = 'y,-z,-x',
                matrix = np.array([[ 0,  1,  0],
                                   [ 0,  0, -1],
                                   [-1,  0,  0]])
            )
        __add_dict(
                pognum = '38',
                symbol = '2',
                geometric_element = '0,y,y',
                direction = np.array([0,1,1]),
                transformed_coord = '-x,z,y',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  0,  1],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                pognum = '39',
                symbol = '2',
                geometric_element = '0,y,-y',
                direction = np.array([0,1,-1]),
                transformed_coord = '-x,-z,-y',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  0, -1],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                pognum = '40',
                symbol = '4+',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = 'x,-z,y',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  0, -1],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                pognum = '41',
                symbol = '4-',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = 'x,z,-y',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  0,  1],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                pognum = '42',
                symbol = 'm',
                geometric_element = '0,y,z',
                direction = np.array([1,0,0]),
                transformed_coord = '-x,y,z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '43',
                symbol = '-3+',
                geometric_element = '-x,-x,x',
                direction = np.array([-1,-1,1]),
                transformed_coord = 'z,-x,y',
                matrix = np.array([[ 0,  0,  1],
                                   [-1,  0,  0],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                pognum = '44',
                symbol = '-3-',
                geometric_element = '-x,-x,x',
                direction = np.array([-1,-1,1]),
                transformed_coord = '-y,z,x',
                matrix = np.array([[ 0, -1,  0],
                                   [ 0,  0,  1],
                                   [ 1,  0,  0]])
            )
        __add_dict(
                pognum = '45',
                symbol = 'm',
                geometric_element = 'x,y,-y',
                direction = np.array([0,1,1]),
                transformed_coord = 'x,-z,-y',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  0, -1],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                pognum = '46',
                symbol = 'm',
                geometric_element = 'x,y,y',
                direction = np.array([0,1,-1]),
                transformed_coord = 'x,z,y',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  0,  1],
                                   [ 0,  1,  0]])
            )
        __add_dict(
                pognum = '47',
                symbol = '-4+',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = '-x,z,-y',
                matrix = np.array([[-1,  0,  0],
                                   [ 0,  0,  1],
                                   [ 0, -1,  0]])
            )
        __add_dict(
                pognum = '48',
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
                pognum = '1',
                symbol = '1',
                geometric_element = None,
                direction = None,
                transformed_coord = 'x,y,z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '7',
                symbol = '2',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-x,-y,z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '10',
                symbol = '2',
                geometric_element = 'x,x,0',
                direction = np.array([1,1,0]),
                transformed_coord = 'y,x,-z',
                matrix = np.array([[ 0,  1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '11',
                symbol = '2',
                geometric_element = 'x,-x,0',
                direction = np.array([1,-1,0]),
                transformed_coord = '-y,-x,-z',
                matrix = np.array([[ 0, -1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '4',
                symbol = '-1',
                geometric_element = '0,0,0',
                direction = None,
                transformed_coord = '-x,-y,-z',
                matrix = np.array([[-1,  0,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '14',
                symbol = 'm',
                geometric_element = 'x,y,0',
                direction = np.array([0,0,1]),
                transformed_coord = 'x,y,-z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '17',
                symbol = 'm',
                geometric_element = 'x,-x,z',
                direction = np.array([1,1,0]),
                transformed_coord = '-y,-x,z',
                matrix = np.array([[ 0, -1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '18',
                symbol = 'm',
                geometric_element = 'x,x,z',
                direction = np.array([1,-1,0]),
                transformed_coord = 'y,x,z',
                matrix = np.array([[ 0,  1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '49',
                symbol = '3+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-y,x-y,z',
                matrix = np.array([[ 0, -1,  0],
                                   [ 1, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '50',
                symbol = '6+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'x-y,x,z',
                matrix = np.array([[ 1, -1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '51',
                symbol = '2',
                geometric_element = 'x,0,0',
                direction = np.array([1,0,0]),
                transformed_coord = 'x-y,-y,-z',
                matrix = np.array([[ 1, -1,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '52',
                symbol = '2',
                geometric_element = 'x,2x,0',
                direction = np.array([1,2,0]),
                transformed_coord = 'y-x,y,-z',
                matrix = np.array([[-1,  1,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '53',
                symbol = '-3+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y,y-x,-z',
                matrix = np.array([[ 0,  1,  0],
                                   [-1,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '54',
                symbol = '-6+',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y-x,-x,-z',
                matrix = np.array([[-1,  1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '55',
                symbol = 'm',
                geometric_element = 'x,2x,z',
                direction = np.array([1,0,0]),
                transformed_coord = 'y-x,y,z',
                matrix = np.array([[-1,  1,  0],
                                   [ 0,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '56',
                symbol = 'm',
                geometric_element = 'x0z',
                direction = np.array([1,2,0]),
                transformed_coord = 'x-y,-y,z',
                matrix = np.array([[ 1, -1,  0],
                                   [ 0, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '57',
                symbol = '3-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y-x,-x,z',
                matrix = np.array([[-1,  1,  0],
                                   [-1,  0,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '58',
                symbol = '6-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'y,y-x,z',
                matrix = np.array([[ 0,  1,  0],
                                   [-1,  1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '59',
                symbol = '2',
                geometric_element = '0,y,0',
                direction = np.array([0,1,0]),
                transformed_coord = '-x,y-x,-z',
                matrix = np.array([[-1,  0,  0],
                                   [-1,  1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '60',
                symbol = '2',
                geometric_element = '2x,x,0',
                direction = np.array([2,1,0]),
                transformed_coord = 'x,x-y,-z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 1, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '61',
                symbol = '-3-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = 'x-y,x,-z',
                matrix = np.array([[ 1, -1,  0],
                                   [ 1,  0,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '62',
                symbol = '-6-',
                geometric_element = '0,0,z',
                direction = np.array([0,0,1]),
                transformed_coord = '-y,x-y,-z',
                matrix = np.array([[ 0, -1,  0],
                                   [ 1, -1,  0],
                                   [ 0,  0, -1]])
            )
        __add_dict(
                pognum = '63',
                symbol = 'm',
                geometric_element = '2x,x,z',
                direction = np.array([0,1,0]),
                transformed_coord = 'x,x-y,z',
                matrix = np.array([[ 1,  0,  0],
                                   [ 1, -1,  0],
                                   [ 0,  0,  1]])
            )
        __add_dict(
                pognum = '64',
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
