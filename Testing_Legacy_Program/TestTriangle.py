import unittest

from Triangle import classifyTriangle

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

