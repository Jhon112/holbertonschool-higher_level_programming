import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquareMethods(unittest.TestCase):
    
    def test_square(self):
        s1 = Square(5)

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

        # teset getter
        s1.size = 8
        self.assertEqual(s1.height, 8)
         # test size.setter
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1.size = "hello"
        with self.assertRaises(ValueError, msg="width must be > 0"):
            s1.size = -5
