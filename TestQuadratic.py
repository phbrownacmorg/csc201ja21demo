# Empty unit-testing class
# Peter Brown, 26 Jan 2017

from typing import Tuple
import unittest
from quadratic_fns import findRoots

class TestQuadratic(unittest.TestCase):
    def test_nothing(self) -> None:
        self.assertTrue(True)

    # Test floating-point numbers
    def testSimple(self) -> None:
        roots:Tuple[float, float] = findRoots(2, 5, 2)
        self.assertAlmostEqual(roots[0], -0.5)
        self.assertAlmostEqual(roots[1], -2.0)

    def testNotSoSimple(self) -> None:
        roots:Tuple[float, float] = findRoots(5, 6, 1)
        self.assertAlmostEqual(roots[0], -0.2)
        self.assertAlmostEqual(roots[1], -1.0)
        
    # Test exception
    def testNegDeterminant(self) -> None:
        with self.assertRaises(ValueError) as cm:
            findRoots(2,3,2)
        exc:ValueError = cm.exception
        # Actually testing a Boolean expression
        self.assertTrue((str(exc)).startswith('math domain error'))
            
if __name__ == '__main__':
    unittest.main()