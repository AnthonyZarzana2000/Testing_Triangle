# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    test_results = []  
    
    def run_test(self, test_id, a, b, c, expected_result):
        actual_result = classifyTriangle(a, b, c)
        passed = actual_result == expected_result
        TestTriangles.test_results.append({
            'Test ID': test_id,
            'Input': f'{a}, {b}, {c}',
            'Expected Result': expected_result,
            'Actual Result': actual_result,
            'Pass or Fail': 'Pass' if passed else 'Fail'
        })

#################################################################################################
    # def testRightTriangleA(self): 
    #     self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    # # def testRightTriangleB(self): 
    # #     self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    # def testRightTriangleB(self): 
    #     self.assertEqual(classifyTriangle(5,3,4),'Scalene','5,3,4 is a Scalene triangle')
        
    # def testEquilateralTriangles(self): 
    #     self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
#################################################################################################


    # Above are the original tests that we were using to test the Triangle code
    # Below are the new Tests that I have created to test the program
    # The program prints out a text file that you will notice in the repo that shows the results of the test in
    # the same orderly table layout that was shown in the instructions of the assignment.

    def testRightTriangleA(self):
        self.run_test('1', 3, 4, 5, 'Right')

    def testRightTriangleB(self):
        self.run_test('2', 5, 3, 4, 'Scalene')

    def testEquilateralTriangle(self):
        self.run_test('3', 1, 1, 1, 'Equilateral')

    # Teardown method class I created to print out the table showing the results of the unit test.
    @classmethod
    def tearDownClass(cls):
        with open('test_report.txt', 'w') as f:
            f.write("{:<10} {:<15} {:<20} {:<20} {:<10}\n".format('Test ID', 'Input', 'Expected Result', 'Actual Result', 'Pass or Fail'))
            f.write("-" * 80 + "\n")
            for result in cls.test_results:
                f.write("{:<10} {:<15} {:<20} {:<20} {:<10}\n".format(
                    result['Test ID'], result['Input'], result['Expected Result'], result['Actual Result'], result['Pass or Fail']
                ))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

