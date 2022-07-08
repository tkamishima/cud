#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Color palettes recommended in `the Color Universal Design, version 4
(in Japanese) <https://jfly.uni-koeln.de/colorset/)`_.
"""

# =============================================================================
# Imports
# =============================================================================

# =============================================================================
# Metadata variables
# =============================================================================

# =============================================================================
# Public symbols
# =============================================================================

__all__ = ['named_colors', 'plot']

# =============================================================================
# Constants
# =============================================================================

"""
The dictionary whose keys and values are color names and their corresponding
hex-style values.

>>> import cud4
>>> import matplotlib.pyplot as plt

>>> mycol = cud4.named_colors
>>> plt.bar(mycol.keys(), 1, color=mycol.values())
>>> plt.xticks(rotation=-90)
>>> plt.show()
"""
named_colors = {
    'white' : '#FFFFFF',
    'light gray' : '#C8C8CB',
    'gray' : '#84919E',
    'black' : '#000000',
    'red' : '#FF4B00',
    'yellow' : '#FFF100',
    'green' : '#03AF7A',
    'blue' : '#005AFF',
    'skyblue' : '#4DC4FF',
    'pink' : '#FF8082',
    'orange' : '#F6AA00',
    'purple' : '#990099',
    'brown' : '#804000',
    'light pink' : '#FFCABF',
    'cream' : '#FFFF80',
    'light yellowgreen' : '#D8F255',
    'light skyblue' : '#BFE4FF',
    'beige' : '#FFCA80',
    'light green' : '#77D9A8',
    'light purple' : '#C9ACE6',
}

"""
Selected six colors useful for plotting.

>>> import cud4
>>> import matplotlib.pyplot as plt
>>> import numpy as np

>>> x = np.linspace(0.0, np.pi * 6, 1000)
>>> y = np.sin(x)
>>> for i in range(6):
>>>     plt.plot(x, y + i, color=cud4.plot[i])
>>> plt.show()
"""
plot = (
    named_colors['red'],
    named_colors['blue'],
    named_colors['green'],
    named_colors['orange'],
    named_colors['skyblue'],
    named_colors['yellow'],
)

