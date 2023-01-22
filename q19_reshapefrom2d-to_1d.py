#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:21:06 2023

@author: franktapira49
"""

import numpy as np
arr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

newarr = arr.reshape(-1)
print(newarr)
print(newarr.shape)
print(arr.shape)

