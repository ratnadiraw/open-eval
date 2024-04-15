import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def f_313(length):
    """
    Create a normal distribution with a given length, plot its histogram alongside the 
    probability density function, and return the distribution and the plot.
    
    Parameters:
    - length (int): The length of the distribution to be generated.
    
    Returns:
    - tuple: A tuple containing:
        1. numpy array with the normal distribution.
        2. matplotlib Axes object representing the plot.
    
    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot
    
    Constants:
    - MU (mean): 0
    - SIGMA (standard deviation): 1
    
    Example:
    >>> distribution, ax = f_312(1000)
    >>> print(type(distribution))
    <class 'numpy.ndarray'>
    >>> print(type(ax))
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """

    MU = 0
    SIGMA = 1
    
    distribution = np.random.normal(MU, SIGMA, length)
    fig, ax = plt.subplots()
    ax.hist(distribution, 30, density=True, label='Histogram')
    ax.plot(np.sort(distribution), norm.pdf(np.sort(distribution), MU, SIGMA), 
            linewidth=2, color='r', label='PDF')
    ax.legend()
    
    return distribution, ax

import unittest
import numpy as np
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        distribution, ax = f_313(1000)
        self.assertIsInstance(distribution, np.ndarray, "Expected distribution to be a numpy array")
        self.assertIsInstance(ax, plt.Axes, "Expected ax to be a matplotlib Axes object")
    
    def test_case_2(self):
        length = 500
        distribution, _ = f_313(length)
        self.assertEqual(len(distribution), length, f"Expected distribution length to be {length}")
    
    def test_case_3(self):
        distribution, _ = f_313(1000)
        mean = distribution.mean()
        std_dev = distribution.std()
        self.assertAlmostEqual(mean, 0, delta=0.1, msg=f"Expected mean to be close to 0, got {mean}")
        self.assertAlmostEqual(std_dev, 1, delta=0.1, msg=f"Expected std_dev to be close to 1, got {std_dev}")
    
    def test_case_4(self):
        distribution, ax = f_313(1000)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 1, "Expected one line representing PDF in the plot")
        bars = [rect for rect in ax.get_children() if isinstance(rect, plt.Rectangle)]
        self.assertGreater(len(bars), 1, "Expected multiple bars representing histogram in the plot")
    
    def test_case_5(self):
        distribution, _ = f_313(2000)
        self.assertEqual(distribution.shape, (2000,), "Expected shape of distribution to match input length")
if __name__ == "__main__":
    run_tests()