import unittest
from UpdatedTriangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    
    def test_right_triangle_a(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 should be Right')
    
    def test_right_triangle_b(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 should be Right')
    
    def test_equilateral_triangle(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')
    
    def test_invalid_input_non_integer(self):
        self.assertEqual(classifyTriangle(3, 4, 'five'), 'InvalidInput', '3,4,five should be InvalidInput')

    def test_invalid_input_negative_side(self):
        self.assertEqual(classifyTriangle(3, -4, 5), 'InvalidInput', '3,-4,5 should be InvalidInput')
    
    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 should not be a triangle')
    def test_scalene_triangle(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3,4,6 should be Scalene')
    def test_isosceles_triangle(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isosceles', '3,3,5 should be Isosceles')
    
    def test_invalid_input_zero_or_negative(self):
        self.assertEqual(classifyTriangle(0, 3, 4), 'InvalidInput', '0,3,4 should be InvalidInput')

if __name__ == '__main__':
    unittest.main()

