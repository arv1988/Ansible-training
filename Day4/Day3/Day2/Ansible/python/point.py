#!/usr/bin/python

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setValues(self,value1,value2):
        self.x = value1
        self.y = value2
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def print1(self):
        print('X = ', self.x)
        print('Y = ', self.y)
        print('***************')

point1 = Point()
point1.setValues(10,20)
point1.print1()

point1 = Point()
point1.setValues(100,200)
point1.print1()