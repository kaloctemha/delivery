# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:31:22 2021

@author: 200461
"""
from itertools import permutations
import numpy as np


class Permutation(object):

    def __init__(self):
        pass

    def getPermutation(self, r, otherThan):
        L = range(1, 8)
        L = [x for x in L if x not in otherThan]
        perm = permutations(L, r)
        return list(perm)