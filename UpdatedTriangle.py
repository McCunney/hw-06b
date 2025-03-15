def classifyTriangle(a, b, c):
    # Ensure inputs are integers before anything else
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    # Ensure inputs are within valid range (0 < side <= 200)
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Check if the input forms a valid triangle (Triangle inequality theorem)
    if a + b <= c or b + c <= a or a + c <= b:
        return 'NotATriangle'

    # Check for Right triangle using Pythagoras' theorem
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        return 'Right'

    # Check for Equilateral triangle
    if a == b == c:
        return 'Equilateral'

    # Check for Isosceles triangle
    if a == b or b == c or a == c:
        return 'Isosceles'

    # If none of the above, it must be Scalene
    return 'Scalene'

