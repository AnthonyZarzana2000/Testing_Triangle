

def classifyTriangle(a,b,c):

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
    #if a == b and b == a: this is wrong
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
