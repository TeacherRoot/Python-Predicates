import random
import time
import math
import unittest
import pytest

# is x between a and b
def between(x, a, b):
  pass
  return True
  
# is x divisibleBy a ?
def isDivisibleBy(x, a):
  
  return False
  
# is x even?
def isEvenNumber(x):
  return False
  
# is x odd?
def isOddNumber(x):
  return False
  
# this is done
def isInteger(x):
  return False  # no change needed here

# withinRadius is the point (x1,y1) within distance of the point (x2, y2)
def withinRadius(x1, y1, x2, y2, distance):
  # t1.xcor()   t2.xcor()
  # t1.ycor()   t2.ycor()
  return False
  
# do the sides a, b, c make a Pythagorean triangle
# remember the Pythagorean theorem
def isPythagorean(a, b, c):
  return False
  
# is number a prime number
# I suggest using a loop here
def isPrime(number):
  
  return True
  
# is (x, y) a point with in the circle defined by (cx, cy) and radius
# think about the circle equation (x-h)^2 + (y-k) ^2 = r^2
# where h,k is the center and x,y is point 
# 
def pointWithinCircle(x, y, cx, cy, radius):

  return False


# put test cases here
# test between
print( "Is 10 between 8 and 12 " + str(between (10, 8, 12)))  

# test divisible by
print( "Is 10 divible by 2 " + str(isDivisibleBy (10, 2))) 

# test isEvenNumber
print( "is 80 even " + str(isEvenNumber(80))) 


print("withInDistance of 10" +str( withinRadius(3,4, 7,8 ,10)))

assert(between(5, 1, 10) == True)     # x is between a and b
assert(between(11, 1, 10) == False)   # x is greater than b
assert(between(0, 1, 10) == False)    # x is less than a
assert(between(10, 1, 10) == True)    # x is equal to b
assert(between(1, 1, 10) == True) 

