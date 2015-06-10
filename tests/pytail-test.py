import unittest
import pytail

class pytailTest(unittest.TestCase):
    def test_get_count(self):
        self.assertEqual(-3, pytail.get_count("+3"))
        self.assertEqual(3, pytail.get_count("3"))
        self.assertEqual(0, pytail.get_count("+0"))
        self.assertEqual(0, pytail.get_count("0"))





if __name__ == '__main__':
    unittest.main()


