
#Importing the classes and Functions from different packages.

import sys

sys.path.append("/Users/sharath.bc/Downloads/PythonPractice1-master/Python/Python-6/pack1")

import module1

module1.display()

sys.path.append("/Users/sharath.bc/Downloads/PythonPractice1-master/Python/Python-6/pack2")

import module2

module2.run()

#To import class then the best way is as below.

from module1 import Bike

b=Bike()

b.gear(10)

from module2 import Car

c=Car()

c.headLight(3)
