'''
Created on Sep 13, 2014

@author: Gus
'''

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        
    def getBasicInformation(self):
        return "Name: "+ self.name +", Author: "+ self.author
    
    def calculateYearsFromRelease(self, year):
        return (2014 - year)
