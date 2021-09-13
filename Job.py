# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:04:01 2021

@author: acolak
"""


class Job(object):
    def __init__(self, id, loc_index, delivery, service):
        self.job_id = id
        self.location_index = loc_index
        self.delivery = delivery
        self.service = service

    def __str__(self):
        return  "\n\tjob_id : " + str(self.job_id) + \
                "\n\tlocation_index :" + str(self.location_index)+\
                "\n\tdelivery: " + str(self.delivery) + \
                "\n\tservice: " + str(self.service) + \
                "\n\tis_completed : " + str(self.is_completed)
