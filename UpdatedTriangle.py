def classifyTriangle(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    

    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

 
    if a + b <= c or b + c <= a or a + c <= b:
        return 'NotATriangle'

  
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        return 'Right'


    if a == b == c:
        return 'Equilateral'


    if a == b or b == c or a == c:
        return 'Isosceles'


    return 'Scalene'

