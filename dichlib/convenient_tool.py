#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file provides various convenient mathematical tools.
"""

def check_equal(x, y, accuracy=3):
    """
    check whether x and y is equal or not

    Args:
        x (float): x value
        y (float): y value
        accuracy (int): threshold of whether two values are the same of not
            In the case of 'accuracy=3', check the third decimal place.

    Returns:
        bool: If True, x and y are the same.

    Raises:
        ValueError: description

    Examples:
        description

        >>> print_test ("test", "message")
          test message

    Note:
        description
    """
    if round(x, accuracy) == round(y, accuracy):
        flag = True
    else:
        flag = False
    return flag


def float2frac(var, accuracy=3, denominator=10):
    """
    transform float to fractional (str object)

    Args:
        var (float): input value
        accuracy (int): threshold of whether two values are the same of not
            In the case of 'accuracy=3', check the third decimal place.
        denominator (int): if 'denominator=10',
            check from 1/2 to 12/13

    Returns:
        dict: description

    Raises:
        ValueError("could not find fractional representation of input 'var')

    Examples:
        description

        >>> float2frac(-1.333333, 3)
          '-4/3'

    Note:
        description
    """
    def _decimal_part2frac(deci_part, accuracy, denominator):
        flag = 1
        for i in range(2, denominator+1):
            for j in (range(1, i)):
                if check_equal(deci_part, j/i):
                    flag = 0
                    pair = (j, i)
                    break
                else:
                    continue
            if flag == 0:
                break
            else:
                continue
        if flag == 1:
            raise ValueError("could not find fractional representation of %s"
                    % deci_part)
        else:
            return pair

    if var < 0:
        sign = '-'
    else:
        sign = ''
    int_part = int(abs(var))
    deci_part = abs(var) - int_part

    if check_equal(deci_part, 0.):
        if int_part == 0:
            return str(int_part)
        else:
            return sign+str(int_part)
    else:
        pair = _decimal_part2frac(deci_part, accuracy, denominator)
        return sign+str(int_part*pair[1]+pair[0])+'/'+str(pair[1])
