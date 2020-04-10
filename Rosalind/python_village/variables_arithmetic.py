#Austin Schenk
#Rosalind python village
#problem 2

from math import sqrt
####Variables & some Arithmetic####

####notes####
#you must indicate floating point or python will round down to the 
#nearest whole number. float(#)
# == is equality 

####problem####

""" Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b. """

####solution####
# a^2 + b^2 = c^2
# c = abs(sqrt(a^2 + b^2))

def hypo(a,b):
  c = abs(sqrt(a**2 + b**2))
  return(c)

#print(hypo(3, 5)) # 5.83...???
#print(sqrt((3**2) + (5**2)))
#print(3**2)
#print(5**2)
#this function works but the question is asking for the square. Reading the 
#question does help. 


def hypo(a,b):
  c = a**2 + b**2
  return(c)

print(hypo(3, 5)) # 34, bingo!

#sample given: 984, 964

print(hypo(984, 964))

#answer: 1897552, correct. 