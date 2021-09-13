# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 09:00:26 2021

@author: acolak
"""

class Settings(object):
    FILE_NAME = "input.json"
    STOCK_CONSTRAINT =  True
    OUTPUT_FILE = "output.txt"
    
    
    def __str__(self):
        return  "\n\tINPUT FILE_NAME : " + str(self.FILE_NAME) + \
                "\n\tSTOCK_CONSTRAINT : " + str(self.STOCK_CONSTRAINT) + \
                "\n\tOUTPUT_FILE : " + str(self.OUTPUT_FILE)