
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


class Student(Person):
  def __str__(self):
        #return ("Hi! my name is " + str(self.name) + ". I'm " + str(self.age) + " year's old")
        return f"Hi! my name is {self.name}. I'm a student and I'm {self.age} year's old"

class Teacher(Person):
    def __init__(self, name, age, subject):
        #self.name = name
        #self.age = age
        super().__init__(name, age)
        self.subject = subject
    
    def __str__(self):
        #return ("Hi! my name is " + str(self.name) + ". I'm " + str(self.age) + " year's old")
        return f"Hi! my name is {self.name}. I teach {self.subject} and I'm {self.age} year's old"

people.append(Person("John", 36))
people.append(Teacher("Sally", 25, "Math" ))
people.append(Student("Billy", 15))

people[0].name = "Jonathan"

print(people[0].name)


for p in people:
    print(p)