# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:03:48 2021

@author: 200461
"""
from Settings import Settings


class Vehicle(object):

    def __init__(self, vehicle_id, start_index, capacity):
        self.vehicle_id = vehicle_id
        self.starting_index = start_index
        self.location = start_index
        self.capacity = capacity
        self.stock = capacity
        self.delivery_duration = 0
        self.costs = list()

    def __str__(self):
        return "\njobs : " + str(self.jobs) + \
            "\n\tvehicle_id : " + str(self.vehicle_id) + \
            "\n\tstarting_index : " + str(self.starting_index) + \
            "\n\tcapacity : " + str(self.capacity) + \
            "\n\tlocation : " + str(self.location) + \
            "\n\tstock : " + str(self.stock) + \
            "\n\tdelivery_duration : " + str(self.delivery_duration)

    def addCost(self, cost):
        self.costs.append(cost)

    def getVehicleCost(self):
        return sum(self.costs)
