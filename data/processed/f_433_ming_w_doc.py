import base64
import pandas as pd


def f_127(df):
    """
    Encodes a Pandas DataFrame as a Base64 string. The DataFrame is first converted to CSV format,
    then encoded to bytes, and finally encoded to a Base64 string.

    Parameters:
        df (DataFrame): The pandas DataFrame to be encoded.

    Returns:
        str: The Base64 encoded string of the DataFrame's CSV representation.

    Requirements:
        - base64
        - pandas

    Example:
        >>> df = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        >>> encoded_df = f_127(df)
        >>> isinstance(encoded_df, str)
        True
        >>> len(encoded_df) > 0  # The actual encoded string will vary
        True
    """
    df = pd.DataFrame(df)
    csv = df.to_csv(index=False)
    csv_bytes = csv.encode('utf-8')
    base64_bytes = base64.b64encode(csv_bytes)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string

import unittest
from io import StringIO
class TestCases(unittest.TestCase):
    def test_encode_basic_dataframe(self):
        df = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        encoded_df = f_127(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
    def test_encode_with_different_columns(self):
        df = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        encoded_df = f_127(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
    def test_encode_empty_dataframe(self):
        df = {'X': [], 'Y': []}
        encoded_df = f_127(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv, check_dtype=False, check_index_type=False)
    def test_encode_with_specific_values(self):
        df = {'ID': [101, 102, 103], 'Score': [85, 90, 88]}
        encoded_df = f_127(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
    def test_encode_with_string_values(self):
        df = {'City': ['NY', 'LA'], 'Population': [8000000, 4000000]}
        encoded_df = f_127(df)
        decoded_csv = pd.read_csv(StringIO(base64.b64decode(encoded_df.encode('utf-8')).decode('utf-8')))
        pd.testing.assert_frame_equal(pd.DataFrame(df), decoded_csv)
