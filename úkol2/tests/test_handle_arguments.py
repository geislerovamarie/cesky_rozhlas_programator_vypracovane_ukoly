from src.handle_arguments import *
from argparse import Namespace
import unittest


class TestClass(unittest.TestCase):
    def test_none_output_file(self):
        expected = {"source_file": "../úkol2/obecnа_osoba.xml", "output_file": "../úkol2/obecnа_osoba", "otype": "csv"}
        args = Namespace(source_file='../úkol2/obecnа_osoba.xml', output_file=None, otype="csv")
        result = check_args(args)
        self.assertDictEqual(expected, result)

    def test_type_undefined_extension_in_output_file(self):
        expected = {"source_file": "../úkol2/obecnа_osoba.xml", "output_file": "osoba.json", "otype": "json"}
        args = Namespace(source_file='../úkol2/obecnа_osoba.xml', output_file='osoba.json', otype=None)
        result = check_args(args)
        self.assertDictEqual(expected, result)


if __name__ == '__main__':
    unittest.main()