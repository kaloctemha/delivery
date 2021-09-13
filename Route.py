# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 14:11:25 2021

@author: acolak
"""

class Route(object):
    def __init__(self):
        self.routes = {1: list(), 2: list(), 3: list()}
        self.cost = 0
        self.total_delivery_duration = 0
        self.routes = dict()

    def addCost(self, newCost):
        self.cost += newCost

    def __str__(self):
        out = str(self.routes[1]) + " --> " + \
            str(self.routes[2]) + " --> " + \
            str(self.routes[3]) + "\t=\t" + str(self.cost)
        return out