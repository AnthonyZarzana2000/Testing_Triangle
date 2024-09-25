# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # # require that the input values be >= 0 and <= 200
    # if a > 200 or b > 200 or c > 200:
    #     return 'InvalidInput'
        
    # if a <= 0 or b <= b or c <= 0:
    #     return 'InvalidInput'
    
    # # verify that all 3 inputs are integers  
    # # Python's "isinstance(object,type) returns True if the object is of the specified type
    # if not (isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
    #     return 'InvalidInput';

    #######################################################################################
    # I went ahead and fixed the InvalidInput checks becaszue they were not working properley.
    # Below is the new lodgic to test if the input values are valid or not.
    #######################################################################################

    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle

    # Input validation
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        print("Invalid input: One or more sides are out of bounds.")
        return 'InvalidInput'
    
    # Verify that all 3 inputs are integers 
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        print("Invalid input: One or more sides are not integers.")
        return 'InvalidInput'
    
    # Triangle inequality theorem
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Not a triangle: The sum of two sides is not greater than the third.")
        return 'NotATriangle'
      
    #if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)): this is wrong
    if not (a + b > c and a + c > b and b + c > a): 
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    #if a == b and b == a:
    if a == b and b == c:
        return 'Equilateral'
    #elif ((a * 2) + (b * 2)) == (c * 2): this is wrong
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    #elif (a != b) and  (b != c) and (a != b): this is wrong
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'