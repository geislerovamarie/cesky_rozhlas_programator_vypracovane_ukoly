from src.clean_data import *
import unittest
import pandas as pd


class TestClass(unittest.TestCase):
    def test_filename_separator_tsv(self):
        sep = process_filename("filename.tsv")
        self.assertEqual(sep, '\t')

    def test_filename_separator_csv(self):
        sep = process_filename("some/file/path/data.csv")
        self.assertEqual(sep, ',')

    def test_count_nonempty_name_rows_for_objectID(self):
        """
        chunk =   ObjectID   Name
                0      zbc    NaN
                1      abc  Item0
                2      abc    NaN
                3      abc    NaN
                4      abc  Item1
                5      bbc  Item2
        """
        chunk = pd.DataFrame({'ObjectID': {0: 'zbc', 1: 'abc', 2: 'abc', 3: 'abc', 4: 'abc', 5: 'bbc'},\
                              'Name': {0: np.nan, 1: 'Item0', 2: np.nan, 3: np.nan, 4: 'Item1', 5: 'Item2'}})
        
        _, group_counts = count_nonempty_rows_in_chunk(chunk)
        formatted_group_counts = group_counts.to_dict()["Name_nonempty"]
        
        expected = {'zbc': 0, 'abc': 2, 'bbc': 1}
        self.assertDictEqual(formatted_group_counts, expected)


if __name__ == '__main__':
    unittest.main()