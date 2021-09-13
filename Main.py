# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 20:46:52 2021

@author: 200461
"""
from DeliveryManager import DeliveryManager
from BruteForce import BruteForce


def main():
    mgr = DeliveryManager()
    bruteForce = BruteForce(mgr)
    bruteForce.createBruteRoutes()
    minroute = bruteForce.findMinRoute()
    mgr.printRoute(minroute)
    
if __name__ == "__main__":
    main()