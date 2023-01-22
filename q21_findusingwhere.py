#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:28:22 2023

@author: franktapira49
"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
print(x)
