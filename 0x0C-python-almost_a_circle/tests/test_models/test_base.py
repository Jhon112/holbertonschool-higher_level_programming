import unittest
from models.base import Base

class testBaseMethods(unittest.TestCase):
    """Class to test different methods from base class"""

    def test_base(self):
        b1 = Base()
        b2 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 3)
