import random
import pandas as pd
import numpy as np

def f_664(n,
          domain="samplewebsite.com",
          categories=['Sports', 'Technology', 'Health', 'Science', 'Business'],
          random_seed=None):
    """
    Generate 'n' random articles with titles, URLs, IDs, categories, and views, and return them as a DataFrame.
    Views are generated by sampling from a poisson distribution with lambda=1000.
    

    Parameters:
    n (int): The number of articles to generate.
    domain (str): The domain name for article URLs. Default is "samplewebsite.com".
    categories (list): List of categories for the articles. Default values are ['Sports', 'Technology', 'Health', 'Science', 'Business'].
    random_seeed(int): Seed for rng. Used for generating views and choosing categories.

    Returns:
    DataFrame: A pandas DataFrame with columns: 'title', 'title_url', 'id', 'category', 'views'.

    Requirements:
    - random
    - pandas
    - numpy

    Example:
    >>> df = f_664(5, random_seed=1)
    >>> print(df)
           title                    title_url  id    category  views
    0  Article 0  samplewebsite.com/Article_0   0  Technology    992
    1  Article 1  samplewebsite.com/Article_1   1    Business    962
    2  Article 2  samplewebsite.com/Article_2   2      Sports    968
    3  Article 3  samplewebsite.com/Article_3   3      Health    991
    4  Article 4  samplewebsite.com/Article_4   4      Sports    993

    >>> df = f_664(3, categories=['A', 'B'], domain='test.de', random_seed=12)
    >>> print(df)
           title          title_url  id category  views
    0  Article 0  test.de/Article_0   0        B    963
    1  Article 1  test.de/Article_1   1        B    977
    2  Article 2  test.de/Article_2   2        B   1048

    """
    random.seed(random_seed)
    np.random.seed(random_seed)

    data = []
    for _ in range(n):
        title = f"Article {_}"
        title_url = f"{domain}/Article_{_}"
        id = _
        category = random.choice(categories)
        views = np.random.poisson(1000)
        data.append({'title': title, 'title_url': title_url, 'id': id, 'category': category, 'views': views})

    df = pd.DataFrame(data)
    return df

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def test_rng(self):
        'test rng reproducability'
        df1 = f_664(300, random_seed=42)
        df2 = f_664(300, random_seed=42)

        self.assertTrue(pd.testing.assert_frame_equal(df1, df2) is None)
    
    def test_case_1(self):
        'default params'
        df = f_664(400, random_seed=10)
        self.assertEqual(len(df), 400)
        self.assertTrue(df['title_url'].str.startswith("samplewebsite.com/Article_").all())
        self.assertEqual(len(df['id'].unique()), 400)
        self.assertTrue(df['category'].isin(['Sports', 'Technology', 'Health', 'Science', 'Business']).all())
        self.assertTrue(df['views'].dtype, int)

    def test_case_2(self):
        'custom params'
        df = f_664(330, domain="testdomain.com", categories=['A', 'B', 'C'])
        self.assertEqual(len(df), 330)
        self.assertTrue(df['title_url'].str.startswith("testdomain.com/Article_").all())
        self.assertEqual(len(df['id'].unique()), 330)
        self.assertTrue(df['category'].isin(['A', 'B', 'C']).all())
        self.assertTrue(df['views'].dtype, int)

    def test_case_3(self):
        '0 articles'
        df = f_664(0)
        self.assertEqual(len(df), 0)

    def test_case_4(self):
        df = f_664(1000, random_seed=1)
        self.assertEqual(len(df), 1000)
        self.assertEqual(len(df['id'].unique()), 1000)
        self.assertTrue(df['views'].dtype, int)

    def test_case_5(self):
        df = f_664(7, domain="anotherdomain.com", random_seed=3)
        self.assertEqual(len(df), 7)
        self.assertTrue(df['title_url'].str.startswith("anotherdomain.com/Article_").all())
        self.assertEqual(len(df['id'].unique()), 7)
        self.assertTrue(df['category'].isin(['Sports', 'Technology', 'Health', 'Science', 'Business']).all())
        self.assertTrue(df['views'].dtype, int)

if __name__ == "__main__":
    run_tests()