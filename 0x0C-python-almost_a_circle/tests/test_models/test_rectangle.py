import unittest
from models.rectangle import Rectangle

class testRectangleMethods(unittest.TestCase):
    
    def test_all(self):
        r1 = Rectangle(10, 2, 20, 30)
        #test id
        self.assertEqual(r1.id, 1)

        # Check getter for height works
        self.assertEqual(r1.height, 2)

        # check setter for height works
        r1.height = 5
        self.assertEqual(r1.height, 5)

        # Check getter for width works
        self.assertEqual(r1.width, 10)

        # check setter for width works
        r1.width = 12
        self.assertEqual(r1.width, 12)

        # Check getter for x works
        self.assertEqual(r1.x, 20)

        # check setter for x works
        r1.x = 25
        self.assertEqual(r1.x, 25)

        # Check getter for y works
        self.assertEqual(r1.y, 30)

        # check setter for y works
        r1.y = 35
        self.assertEqual(r1.y, 35)

    def test_height(self):
        r3 = Rectangle(10, 2)
        self.assertEqual(r3.id, 2)

        # Check getter works
        self.assertEqual(r3.height, 2)

        # check setter works
        r3.height = 5
        self.assertEqual(r3.height, 5)

        # check an exception is raised when trying to access
        # a private attribute
        with self.assertRaises(AttributeError):
            print(r3.__height)

        # check an exception is raised when height not an int
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r3.height = 'hi'

        # check an exception is raised when height is less than 0 or 0
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r3.height = 0

    def test_width(self):
        r2 = Rectangle(10, 2, id=12)
        self.assertEqual(r2.id, 12)

        # Check getter works
        self.assertEqual(r2.width, 10)

        # check setter works
        r2.width = 5
        self.assertEqual(r2.width, 5)

        # check an exception is raised when trying to access
        # a private attribute
        with self.assertRaises(AttributeError):
            print(r2.__width)

        # check an exception is raised when width not an int
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2.width = 'hi'

        # check an exception is raised when width is less than 0 or 0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r2.width = 0

    def test_x(self):
        # Check getter works
        r4 = Rectangle(10, 2)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r4.x, 0)

        # check setter works
        r4.x = 5
        self.assertEqual(r4.x, 5)

        # check an exception is raised when trying to access
        # a private attribute
        with self.assertRaises(AttributeError):
            print(r4.__x)

        # check an exception is raised when x not an int
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r4.x = 'hi'

        # check an exception is raised when x is less than 0
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r4.x = -1

    def test_y(self):
        r5 = Rectangle(10, 2)
        self.assertEqual(r5.id, 4)

        # Check getter works
        self.assertEqual(r5.y, 0)

        # check setter works
        r5.y = 5
        self.assertEqual(r5.y, 5)

        # check an exception is raised when trying to access
        # a private attribute
        with self.assertRaises(AttributeError):
            print(r5.__y)

        # check an exception is raised when y not an int
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r5.y = 'hi'

        # check an exception is raised when y is less than 0
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r5.y = -1
