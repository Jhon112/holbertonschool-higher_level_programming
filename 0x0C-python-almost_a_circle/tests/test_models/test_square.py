import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquareMethods(unittest.TestCase):
    
    def test_square(self):
        s1 = Square(5)

        # Check id
        self.assertEqual(s1.id, 10)

        # check width and height are the same
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

        # check area method works as intended        
        self.assertEqual(s1.area(), 25)

        # check an error is raised when trying to
        # intialize with a non integer val 
        
        with self.assertRaises(TypeError, msg="height must be an integer"):
            s1.height = 'hi'

        with self.assertRaises(TypeError, msg="height must be an integer"):
            s2 = Square("hello")
