from itertools import combinations
import pandas as pd


def f_343(number_list, element):
    """
    Find all unique combinations of 3 numbers from a list that add up to a certain element.

    If the number_list is empty, or there is no combination that adds up to the element,
    an empty dataframe is returned.
    

    Parameters:
    number_list (list): The list of numbers.
    element (int): The number to which the combination of 3 numbers should add up.

    Returns:
    Pandas DataFrame: A pandas Dataframe with the column 'Combinations',
         where each row contains a tuple containing a unique combination of 3 numbers that add up to the element.

    Requirements:
    - itertools
    - pandas:

    Example:
    >>> result = f_343([1, 2, 3, 4, 5], 6)
    >>> print(result)    
      Combinations
    0    (1, 2, 3)

    >>> result = f_343([-1, 1, 0, -2, 2, 3], 0)
    >>> print(result) 
      Combinations
    0  (-1, -2, 3)
    1   (-1, 1, 0)
    2   (0, -2, 2)

    >>> result = f_343([], 0)
    >>> print(result)
    Empty DataFrame
    Columns: [Combinations]
    Index: []
    """
    combinations_list = list(combinations(number_list, 3))
    valid_combinations = [comb for comb in combinations_list if sum(comb) == element]
    return pd.DataFrame({'Combinations': list(set(valid_combinations))})

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_343([1, 2, 3, 4, 5, 6], 6)
        expected = pd.DataFrame(
            {'Combinations': {0: (1, 2, 3)}}
        )
        pd.testing.assert_frame_equal(result, expected)
    def test_case_2(self):
        result = f_343(list(range(1, 51)) + [50], 50)
        expected = pd.DataFrame(
                {'Combinations': {0: (1, 12, 37),
                1: (1, 13, 36),
                2: (12, 16, 22),
                3: (3, 22, 25),
                4: (2, 14, 34),
                5: (3, 23, 24),
                6: (5, 12, 33),
                7: (5, 13, 32),
                8: (9, 10, 31),
                9: (1, 11, 38),
                10: (3, 20, 27),
                11: (3, 21, 26),
                12: (6, 19, 25),
                13: (5, 11, 34),
                14: (9, 16, 25),
                15: (2, 5, 43),
                16: (7, 20, 23),
                17: (1, 2, 47),
                18: (7, 21, 22),
                19: (6, 10, 34),
                20: (6, 17, 27),
                21: (6, 18, 26),
                22: (11, 13, 26),
                23: (2, 3, 45),
                24: (2, 4, 44),
                25: (7, 19, 24),
                26: (6, 8, 36),
                27: (10, 18, 22),
                28: (4, 13, 33),
                29: (6, 16, 28),
                30: (4, 21, 25),
                31: (3, 10, 37),
                32: (11, 19, 20),
                33: (10, 16, 24),
                34: (1, 22, 27),
                35: (4, 11, 35),
                36: (4, 12, 34),
                37: (7, 10, 33),
                38: (12, 18, 20),
                39: (4, 19, 27),
                40: (3, 8, 39),
                41: (3, 9, 38),
                42: (6, 7, 37),
                43: (1, 21, 28),
                44: (4, 10, 36),
                45: (5, 14, 31),
                46: (7, 8, 35),
                47: (7, 9, 34),
                48: (15, 16, 19),
                49: (3, 7, 40),
                50: (2, 22, 26),
                51: (9, 18, 23),
                52: (2, 23, 25),
                53: (5, 21, 24),
                54: (9, 19, 22),
                55: (1, 19, 30),
                56: (8, 15, 27),
                57: (1, 20, 29),
                58: (8, 16, 26),
                59: (4, 9, 37),
                60: (5, 19, 26),
                61: (9, 17, 24),
                62: (8, 13, 29),
                63: (2, 13, 35),
                64: (8, 14, 28),
                65: (1, 10, 39),
                66: (4, 7, 39),
                67: (12, 14, 24),
                68: (8, 12, 30),
                69: (2, 12, 36),
                70: (10, 19, 21),
                71: (1, 8, 41),
                72: (1, 9, 40),
                73: (4, 22, 24),
                74: (2, 10, 38),
                75: (3, 19, 28),
                76: (2, 11, 37),
                77: (5, 9, 36),
                78: (10, 17, 23),
                79: (2, 18, 30),
                80: (1, 7, 42),
                81: (4, 20, 26),
                82: (14, 17, 19),
                83: (3, 17, 30),
                84: (3, 18, 29),
                85: (5, 7, 38),
                86: (4, 18, 28),
                87: (7, 17, 26),
                88: (13, 18, 19),
                89: (3, 15, 32),
                90: (14, 16, 20),
                91: (3, 16, 31),
                92: (6, 14, 30),
                93: (5, 6, 39),
                94: (5, 22, 23),
                95: (11, 17, 22),
                96: (7, 15, 28),
                97: (7, 16, 27),
                98: (6, 12, 32),
                99: (6, 13, 31),
                100: (5, 20, 25),
                101: (3, 6, 41),
                102: (11, 15, 24),
                103: (11, 16, 23),
                104: (10, 13, 27),
                105: (4, 8, 38),
                106: (12, 15, 23),
                107: (4, 16, 30),
                108: (3, 5, 42),
                109: (2, 20, 28),
                110: (2, 21, 27),
                111: (1, 17, 32),
                112: (4, 6, 40),
                113: (1, 18, 31),
                114: (12, 13, 25),
                115: (4, 14, 32),
                116: (3, 4, 43),
                117: (3, 11, 36),
                118: (5, 10, 35),
                119: (2, 19, 29),
                120: (9, 15, 26),
                121: (5, 18, 27),
                122: (1, 15, 34),
                123: (1, 16, 33),
                124: (5, 8, 37),
                125: (9, 13, 28),
                126: (5, 16, 29),
                127: (9, 14, 27),
                128: (8, 10, 32),
                129: (8, 11, 31),
                130: (7, 18, 25),
                131: (6, 15, 29),
                132: (9, 11, 30),
                133: (9, 12, 29),
                134: (11, 18, 21),
                135: (2, 8, 40),
                136: (8, 9, 33),
                137: (2, 9, 39),
                138: (10, 15, 25),
                139: (1, 5, 44),
                140: (1, 6, 43),
                141: (6, 21, 23),
                142: (13, 17, 20),
                143: (14, 15, 21),
                144: (2, 6, 42),
                145: (2, 7, 41),
                146: (10, 14, 26),
                147: (1, 3, 46),
                148: (1, 4, 45),
                149: (13, 15, 22),
                150: (4, 17, 29),
                151: (6, 20, 24),
                152: (13, 16, 21),
                153: (3, 13, 34),
                154: (3, 14, 33),
                155: (10, 12, 28),
                156: (4, 15, 31),
                157: (7, 13, 30),
                158: (7, 14, 29),
                159: (13, 14, 23),
                160: (3, 12, 35),
                161: (6, 11, 33),
                162: (11, 14, 25),
                163: (1, 24, 25),
                164: (8, 20, 22),
                165: (7, 12, 31),
                166: (10, 11, 29),
                167: (6, 9, 35),
                168: (5, 17, 28),
                169: (11, 12, 27),
                170: (1, 23, 26),
                171: (8, 19, 23),
                172: (7, 11, 32),
                173: (15, 17, 18),
                174: (4, 5, 41),
                175: (5, 15, 30),
                176: (9, 20, 21),
                177: (8, 17, 25),
                178: (2, 17, 31),
                179: (8, 18, 24),
                180: (1, 14, 35),
                181: (12, 17, 21),
                182: (2, 15, 33),
                183: (2, 16, 32)}}
                  )
        pd.testing.assert_frame_equal(result, expected)
    def test_case_4(self):
        random_list = [i for i in range(1, 51)] + [50]
        result = f_343(random_list, 50)
        expected = pd.DataFrame(
{'Combinations': {0: (1, 12, 37),
  1: (1, 13, 36),
  2: (12, 16, 22),
  3: (3, 22, 25),
  4: (2, 14, 34),
  5: (3, 23, 24),
  6: (5, 12, 33),
  7: (5, 13, 32),
  8: (9, 10, 31),
  9: (1, 11, 38),
  10: (3, 20, 27),
  11: (3, 21, 26),
  12: (6, 19, 25),
  13: (5, 11, 34),
  14: (9, 16, 25),
  15: (2, 5, 43),
  16: (7, 20, 23),
  17: (1, 2, 47),
  18: (7, 21, 22),
  19: (6, 10, 34),
  20: (6, 17, 27),
  21: (6, 18, 26),
  22: (11, 13, 26),
  23: (2, 3, 45),
  24: (2, 4, 44),
  25: (7, 19, 24),
  26: (6, 8, 36),
  27: (10, 18, 22),
  28: (4, 13, 33),
  29: (6, 16, 28),
  30: (4, 21, 25),
  31: (3, 10, 37),
  32: (11, 19, 20),
  33: (10, 16, 24),
  34: (1, 22, 27),
  35: (4, 11, 35),
  36: (4, 12, 34),
  37: (7, 10, 33),
  38: (12, 18, 20),
  39: (4, 19, 27),
  40: (3, 8, 39),
  41: (3, 9, 38),
  42: (6, 7, 37),
  43: (1, 21, 28),
  44: (4, 10, 36),
  45: (5, 14, 31),
  46: (7, 8, 35),
  47: (7, 9, 34),
  48: (15, 16, 19),
  49: (3, 7, 40),
  50: (2, 22, 26),
  51: (9, 18, 23),
  52: (2, 23, 25),
  53: (5, 21, 24),
  54: (9, 19, 22),
  55: (1, 19, 30),
  56: (8, 15, 27),
  57: (1, 20, 29),
  58: (8, 16, 26),
  59: (4, 9, 37),
  60: (5, 19, 26),
  61: (9, 17, 24),
  62: (8, 13, 29),
  63: (2, 13, 35),
  64: (8, 14, 28),
  65: (1, 10, 39),
  66: (4, 7, 39),
  67: (12, 14, 24),
  68: (8, 12, 30),
  69: (2, 12, 36),
  70: (10, 19, 21),
  71: (1, 8, 41),
  72: (1, 9, 40),
  73: (4, 22, 24),
  74: (2, 10, 38),
  75: (3, 19, 28),
  76: (2, 11, 37),
  77: (5, 9, 36),
  78: (10, 17, 23),
  79: (2, 18, 30),
  80: (1, 7, 42),
  81: (4, 20, 26),
  82: (14, 17, 19),
  83: (3, 17, 30),
  84: (3, 18, 29),
  85: (5, 7, 38),
  86: (4, 18, 28),
  87: (7, 17, 26),
  88: (13, 18, 19),
  89: (3, 15, 32),
  90: (14, 16, 20),
  91: (3, 16, 31),
  92: (6, 14, 30),
  93: (5, 6, 39),
  94: (5, 22, 23),
  95: (11, 17, 22),
  96: (7, 15, 28),
  97: (7, 16, 27),
  98: (6, 12, 32),
  99: (6, 13, 31),
  100: (5, 20, 25),
  101: (3, 6, 41),
  102: (11, 15, 24),
  103: (11, 16, 23),
  104: (10, 13, 27),
  105: (4, 8, 38),
  106: (12, 15, 23),
  107: (4, 16, 30),
  108: (3, 5, 42),
  109: (2, 20, 28),
  110: (2, 21, 27),
  111: (1, 17, 32),
  112: (4, 6, 40),
  113: (1, 18, 31),
  114: (12, 13, 25),
  115: (4, 14, 32),
  116: (3, 4, 43),
  117: (3, 11, 36),
  118: (5, 10, 35),
  119: (2, 19, 29),
  120: (9, 15, 26),
  121: (5, 18, 27),
  122: (1, 15, 34),
  123: (1, 16, 33),
  124: (5, 8, 37),
  125: (9, 13, 28),
  126: (5, 16, 29),
  127: (9, 14, 27),
  128: (8, 10, 32),
  129: (8, 11, 31),
  130: (7, 18, 25),
  131: (6, 15, 29),
  132: (9, 11, 30),
  133: (9, 12, 29),
  134: (11, 18, 21),
  135: (2, 8, 40),
  136: (8, 9, 33),
  137: (2, 9, 39),
  138: (10, 15, 25),
  139: (1, 5, 44),
  140: (1, 6, 43),
  141: (6, 21, 23),
  142: (13, 17, 20),
  143: (14, 15, 21),
  144: (2, 6, 42),
  145: (2, 7, 41),
  146: (10, 14, 26),
  147: (1, 3, 46),
  148: (1, 4, 45),
  149: (13, 15, 22),
  150: (4, 17, 29),
  151: (6, 20, 24),
  152: (13, 16, 21),
  153: (3, 13, 34),
  154: (3, 14, 33),
  155: (10, 12, 28),
  156: (4, 15, 31),
  157: (7, 13, 30),
  158: (7, 14, 29),
  159: (13, 14, 23),
  160: (3, 12, 35),
  161: (6, 11, 33),
  162: (11, 14, 25),
  163: (1, 24, 25),
  164: (8, 20, 22),
  165: (7, 12, 31),
  166: (10, 11, 29),
  167: (6, 9, 35),
  168: (5, 17, 28),
  169: (11, 12, 27),
  170: (1, 23, 26),
  171: (8, 19, 23),
  172: (7, 11, 32),
  173: (15, 17, 18),
  174: (4, 5, 41),
  175: (5, 15, 30),
  176: (9, 20, 21),
  177: (8, 17, 25),
  178: (2, 17, 31),
  179: (8, 18, 24),
  180: (1, 14, 35),
  181: (12, 17, 21),
  182: (2, 15, 33),
  183: (2, 16, 32)}}
        )
        self.assertEqual(result.size, expected.size)
        for comb in result['Combinations']:
            self.assertEqual(comb[0]+comb[1]+comb[2], 50)
    def test_edge_case_2(self):
        # Test with a list of length less than 3
        result = f_343([1, 2, 3], 3)
        self.assertTrue(result.empty)
    def test_edge_case_3(self):
        # Test with negative numbers in the list
        result = f_343([-1, -2, 1, 2, 3, 0], 0)
        expected = pd.DataFrame(
            {'Combinations': {0: (-1, -2, 3), 1: (-1, 1, 0), 2: (-2, 2, 0)}}       
        )
        self.assertEqual(result.size, expected.size)
        for comb in result['Combinations']:
            self.assertEqual(comb[0]+comb[1]+comb[2], 0)
    def test_edge_case_4(self):
        # Test with repeated numbers in the list
        result = f_343([1, 1, 1, 1, 1, 3], 3)
        expected = pd.DataFrame(
            {'Combinations': {0: (1, 1, 1)}}
        )
        self.assertEqual(result.size, expected.size)
        for comb in result['Combinations']:
            self.assertEqual(comb[0]+comb[1]+comb[2], 3)
    def test_edge_case_5(self):
        # Test with both positive and negative numbers with no valid combinations
        result = f_343([-5, -4, -3, 5, 6, 7, 0], 0)
        expected = pd.DataFrame(
            {'Combinations': {0: (-4, -3, 7), 1: (-5, 5, 0)}}
        )
        self.assertEqual(result.size, expected.size)
        for comb in result['Combinations']:
            self.assertEqual(comb[0]+comb[1]+comb[2], 0)
