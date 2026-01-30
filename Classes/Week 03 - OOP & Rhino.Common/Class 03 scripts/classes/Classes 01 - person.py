
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
        
    def sayHi(self):
        print("Hi! my name is " + str(self.name) + ". I'm " + str(self.age) + " year's old")

john = Person("John", 36)

print(john.name)
john.sayHi()

