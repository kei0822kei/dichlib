#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file provides various kind of calculations about point group oprations.
"""
import numpy as np

def get_all_pog_operations(coord_sys):
    """
    get all point group operations specified coordinate system

        Parameters
        ----------

        Returns
        -------
        dict
            all point group operations

        Notes
        -----
        reference: ITA p.14 Table 1.2.2.1 and 1.2.2.2

        Raises
        ------
        unexpected coodinate system is specifed
    """
    def __add_dict(symbol,
                   geometric_element,
                   direction,
                   transformed_coord,
                   matrix):
        pog_operations[symbol] = {
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
                geometric_element = None,
                direction = None,
                transformed_coord = 'xyz',
                matrix = np.array([[1, 0, 0],
                                   [0, 1, 0],
                                   [0, 0, 1]])
            )
        __add_dict(
                symbol = '3+',
                geometric_element = 'xxx',
                direction = np.array([1,1,1]),
                transformed_coord = 'zxy',
                matrix = np.array([[0, 0, 1],
                                   [1, 0, 0],
                                   [0, 1, 0]])
            )

    return pog_operations
