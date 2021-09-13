# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 09:00:26 2021

@author: 200461
"""

class Settings(object):
    FILE_NAME = "input.json"
    STOCK_CONSTRAINT =  False
    CARBOY_SERVICE_CONSTRAINT = False
    
    
    def __str__(self):
        return  "\n\tINPUT FILE_NAME : " + str(self.FILE_NAME) + \
         "\n\tSTOCK_CONSTRAINT : " + str(self.STOCK_CONSTRAINT) + \
         "\n\tCARBOY_SERVICE_CONSTRAINT : " + str(self.CARBOY_SERVICE_CONSTRAINT) + "\n\n"