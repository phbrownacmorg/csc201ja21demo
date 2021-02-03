# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
import lab17solution

class TestLab17(unittest.TestCase):
    def test_nothing(self) -> None:
        self.assertTrue(True)

    # Test strings for equality
    def testClassifyZero(self) -> None:
        self.assertEqual(lab17solution.classify(0), 'freshman')
        
    def testClassify1(self) -> None:
        self.assertEqual(lab17solution.classify(1), 'freshman')

    def testClassify23(self) -> None:
        self.assertEqual(lab17solution.classify(23), 'freshman')

    def testClassify2395(self) -> None:
        self.assertEqual(lab17solution.classify(23.95), 'freshman')

    def testClassify24(self) -> None:
        self.assertEqual(lab17solution.classify(24), 'sophomore')

    def testClassify55(self) -> None:
        self.assertEqual(lab17solution.classify(55), 'sophomore')

    def testClassify56(self) -> None:
        self.assertEqual(lab17solution.classify(56), 'junior')

    def testClassify86(self) -> None:
        self.assertEqual(lab17solution.classify(86), 'junior')

    def testClassify87(self) -> None:
        self.assertEqual(lab17solution.classify(87), 'senior')

    def testClassify120(self) -> None:
        self.assertEqual(lab17solution.classify(120), 'senior')

    # Test for an exception getting raised
    def testClassifyNeg0p01(self) -> None:
        with self.assertRaises(ValueError) as cm:
            lab17solution.classify(-0.01)
        exc:ValueError = cm.exception
        self.assertEqual(str(exc), "Hours must be non-negative.  -0.01 is negative.")

    # Test for output to the console (print)
    def test

if __name__ == '__main__':
    unittest.main()