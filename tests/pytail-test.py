import unittest
from .. import pytail


class pytailTest(unittest.TestCase):
    def test_get_count(self):
        self.assertEqual(-3, pytail.get_count("+3"))
        self.assertEqual(3, pytail.get_count("3"))
        self.assertEqual(0, pytail.get_count("+0"))
        self.assertEqual(0, pytail.get_count("0"))

    def test_is_verbose(self):
        #test verbose
        parse = pytail.config_args()
        args = parse.parse_args("-v".split())
        self.assertTrue(pytail.is_verbose(args))

        #quiet
        args = parse.parse_args("-q".split())
        self.assertFalse(pytail.is_verbose(args))

        #quiet and files is > 1
        args = parse.parse_args("-q foo bar".split())
        self.assertFalse(pytail.is_verbose(args))

        #no quiet and files is > 1
        args = parse.parse_args("foo bar".split())
        self.assertTrue(pytail.is_verbose(args))

        #quiet and verbose (mutually exclusive)
        with self.assertRaises(SystemExit) as qv:
            args = parse.parse_args("-q -v".split())

        self.assertEqual(qv.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
