
#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino

people = []

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
    def __str__(self):
        #return ("Hi! my name is " + str(self.name) + ". I'm " + str(self.age) + " year's old")
        return f"Hi! my name is {self.name}. I'm {self.age} year's old"

people.append(Person("John", 36))
people.append(Person("Sally", 25))
people.append(Person("Billy", 15))


for p in people:
    print(p)