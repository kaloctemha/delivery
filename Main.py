# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 20:46:52 2021

@author: acolak
"""
from DeliveryManager import DeliveryManager
from BruteForce import BruteForce
from Settings import Settings

def main():
    print(Settings())
    mgr = DeliveryManager()
    bruteForce = BruteForce(mgr)
    bruteForce.createBruteRoutes()
    minroute = bruteForce.findMinRoute()
    mgr.printRoute(minroute)
    mgr.writeToFile(minroute)
        
        
if __name__ == "__main__":
    main()