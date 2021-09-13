# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 14:15:38 2021

@author: 200461
"""
from Route import Route
from Permutation import Permutation
import numpy as np


class BruteForce(object):

    def __init__(self, mgr):
        self.routeList = list()
        self.clusters = None
        self.permObj = Permutation()
        self.processor = None
        self.mgr = mgr

    def createBruteRoutes(self):
        self.clusters = self.__createClusters()
        for cluster in self.clusters:
            v1 = cluster[0]
            v2 = cluster[1]
            v3 = cluster[2]
            v1Perms = self.permObj.getPermutation(v1, [])
            for v1Route in v1Perms:
                v2Perms = self.permObj.getPermutation(v2, v1Route)
                for v2Route in v2Perms:
                    v3Perms = self.permObj.getPermutation(
                        v3, (v1Route + v2Route))
                    for v3Route in v3Perms:
                        route = Route()
                        route.routes[1] = v1Route
                        route.routes[2] = v2Route
                        route.routes[3] = v3Route
                        self.routeList.append(route)

    def findMinRoute(self):
        for route in self.routeList:
            self.__calc_route_cost(route)
        minroute = self.__find_min_route()
        return minroute

    def __calc_route_cost(self, route):
        job_objects = self.mgr.job_objects
        vehicle_objects = self.mgr.vehicle_objects
        matrix = self.mgr.matrix
        for vehicle in vehicle_objects.values():
            vehicle_location = vehicle.location
            vehicle_id = vehicle.vehicle_id
            vehicle_jobs = route.routes[vehicle_id]
            for job_id in vehicle_jobs:
                job = job_objects[job_id]
                target_location = job.location_index
                service = job.service
                cost = matrix[vehicle_location, target_location]
                route.addCost(cost)
                vehicle_location = target_location

    def __find_min_route(self):
        mincost = -1
        minroute = None
        for route in self.routeList:
            if mincost < 0 or route.cost < mincost:
                mincost = route.cost
                minroute = route

        return minroute

    def __createClusters(self):
        """
         Creates the reference data with all possible number of jobs
         could be assigned to each vehicle
         I.E: [4, 1, 2] ==>  4,1 and 2 jobs will be assigned to Vehicle-1, Vehicle-2 and Vehicle-3 respectively

         TODO: refactor this to execute dynamically with number of jobs and vehicles
        """
        tmp = list()
        for i in reversed(range(8)):
            for j in range(0, 8-i):
                k = 7 - (i+j)
                tmp.append([i, j, k])
        return tmp

        # [7, 0, 0] [3, 2, 2] [1, 3, 3]
        # [6, 0, 1] [3, 3, 1] [1, 4, 2]
        # [6, 1, 0] [3, 4, 0] [1, 5, 1]
        # [5, 0, 2] [2, 0, 5] [1, 6, 0]
        # [5, 1, 1] [2, 1, 4] [0, 0, 7]
        # [5, 2, 0] [2, 2, 3] [0, 1, 6]
        # [4, 0, 3] [2, 3, 2] [0, 2, 5]
        # [4, 1, 2] [2, 4, 1] [0, 3, 4]
        # [4, 2, 1] [2, 5, 0] [0, 4, 3]
        # [4, 3, 0] [1, 0, 6] [0, 5, 2]
        # [3, 0, 4] [1, 1, 5] [0, 6, 1]
        # [3, 1, 3] [1, 2, 4] [0, 7, 0]
