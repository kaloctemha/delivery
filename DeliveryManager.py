# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:00:42 2021

@author: 200461
"""
from Settings import Settings
from Job import Job
from Vehicle import Vehicle
import json
import numpy as np


class DeliveryManager(object):

    def __init__(self):
        self.job_objects = dict()
        self.vehicle_objects = dict()
        self.matrix = list()
        self.build()

    def build(self):
        """
        A method for calculating the distance between the job(customer location) being processed
        and the current location of the fleet
        """
        with open(Settings.FILE_NAME) as input_file:
            data = json.load(input_file)
            self.__construct_jobs(data["jobs"])
            self.__construct_vehicles(data["vehicles"])
            self.matrix = data["matrix"]
            self.matrix = np.array(self.matrix)

    def __construct_jobs(self, jobs):
        """
         Map jobs extracted from input file to our cutsom Job objects
        """
        for j in jobs:
            jID = j['id']
            jIndex = j['location_index']
            jDelivery = j['delivery'][0]
            jService = j['service']
            job = Job(jID, jIndex, jDelivery, jService)
            self.job_objects[jID] = job

    def __construct_vehicles(self, vehicles):
        """
         Map vehicles extracted from input file to our cutsom Vehicle objects
        """
        for v in vehicles:
            vID = v['id']
            vIndex = v['start_index']
            vCapacity = v['capacity'][0]
            vehicle = Vehicle(vID, vIndex, vCapacity)
            self.vehicle_objects[vID] = vehicle

    def printRoute(self, route):
        output = dict()
        outputRoutes = dict()
        output["total_delivery_duration"] = route.cost
        output["routes"] = outputRoutes
        for v in self.vehicle_objects.values():
            vehicleRoute = route.routes[v.vehicle_id]
            delivery_duration = self.__get_vehicle_cost(v.location,vehicleRoute)
            outputRoutes[str(v.vehicle_id)] = dict({"jobs": list(vehicleRoute),
                                               "delivery_duration": delivery_duration})
        print(output)

    def __get_vehicle_cost(self, vehicle_location, jobs):
        vehicleCost = 0
        for jobID in jobs:
            job = self.job_objects[jobID]
            target_location = job.location_index
            vehicleCost += self.matrix[vehicle_location, target_location]
            vehicle_location = target_location
        return vehicleCost
