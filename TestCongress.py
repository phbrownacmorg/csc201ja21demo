# Empty unit-testing class
# Peter Brown, 26 Jan 2017

from congress import eligibleHRep, eligibleSenate
import unittest

class TestNothing(unittest.TestCase):

    def testHRepGenericOK(self) -> None:
        # Checking a Boolean function
        self.assertTrue(eligibleHRep(40, 40))

    def testHRepGenericChild(self) -> None:
        # Checking a Boolean function
        self.assertFalse(eligibleHRep(6, 6))

    def testHRepMinAge(self) -> None:
        self.assertTrue(eligibleHRep(25, 25))

    def testHRepTooYoung(self) -> None:
        self.assertFalse(eligibleHRep(24, 24))

    def testHRepAlien(self) -> None:
        self.assertFalse(eligibleHRep(40, 0))

    def testHRepMinCit(self) -> None:
        self.assertTrue(eligibleHRep(40, 7))

    def testHRepAlmostCit(self) -> None:
        self.assertFalse(eligibleHRep(40, 6))

    def testHRepBarelyBoth(self) -> None:
        self.assertTrue(eligibleHRep(25, 7))

    def testHRepAlmostBoth(self) -> None:
        self.assertFalse(eligibleHRep(24, 6))

    def testSenateGenericOK(self) -> None:
        # Checking a Boolean function
        self.assertTrue(eligibleSenate(40, 40))

    def testSenateGenericChild(self) -> None:
        # Checking a Boolean function
        self.assertFalse(eligibleSenate(6, 6))

    def testSenateMinAge(self) -> None:
        self.assertTrue(eligibleSenate(30, 30))

    def testSenateTooYoung(self) -> None:
        self.assertFalse(eligibleSenate(29, 29))

    def testSenateAlien(self) -> None:
        self.assertFalse(eligibleSenate(40, 0))

    def testSenateMinCit(self) -> None:
        self.assertTrue(eligibleSenate(40, 9))

    def testSenateAlmostCit(self) -> None:
        self.assertFalse(eligibleSenate(40, 8))

    def testSenateBarelyBoth(self) -> None:
        self.assertTrue(eligibleSenate(30, 9))

    def testSenateAlmostBoth(self) -> None:
        self.assertFalse(eligibleSenate(29, 8))

if __name__ == '__main__':
    unittest.main()