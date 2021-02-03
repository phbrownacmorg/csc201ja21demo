# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
import idmaker_files

class TestIDMaker(unittest.TestCase):
    def test_nothing(self) -> None:
        self.assertTrue(True)

    # Comparing strings: use assertEqual
    def testSimple(self) -> None:
        self.assertEqual(idmaker_files.id_from_line('Brown\tPeter\tH.'), 'phbrown001\tBrown\tPeter\tH.')

    def testNoMiddleName(self) -> None:
        self.assertEqual(idmaker_files.id_from_line('Brown\tPeter'), 'pbrown001\tBrown\tPeter')

    def testSpaceInName(self) -> None:
        self.assertEqual(idmaker_files.id_from_line('von Braun\tPeter\tH.'), 'phvonbraun001\tvon Braun\tPeter\tH.')

    def testJr(self) -> None:
        self.assertEqual(idmaker_files.id_from_line('Brown, Jr.\tPeter\tH.'), 'phbrown001\tBrown, Jr.\tPeter\tH.')

    def testII(self) -> None:
        self.assertEqual(idmaker_files.id_from_line('Brown II\tPeter\tH.'), 'phbrown001\tBrown II\tPeter\tH.')
    
    def testApostrophe(self) -> None:
        self.assertEqual(idmaker_files.id_from_line("O'Brown\tPeter\tH."), "phobrown001\tO'Brown\tPeter\tH.")
        
if __name__ == '__main__':
    unittest.main()