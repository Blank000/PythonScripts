import sys
import unittest
from scripts.run import *

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test_sum(self):
        inputs = ["SCRIPT_NAME", 1, 2, 3]
        assert validate_and_return_sum(inputs) == 6

        inputs = ["SCRIPT_NAME", 2, 13, 1]
        assert validate_and_return_sum(inputs) == 3

        inputs = ["SCRIPT_NAME", 2, 1, 14]
        assert validate_and_return_sum(inputs) == 3

        inputs = ["SCRIPT_NAME", 2, 1, 15]
        assert validate_and_return_sum(inputs) == 18

        inputs = ["SCRIPT_NAME", 1, 2]
        assert validate_and_return_sum(inputs) == "Exactly 3 numbers are required"

        inputs = ["SCRIPT_NAME", 1, 2, "a"]
        assert validate_and_return_sum(inputs) == "All inputs must be numeric"

if __name__ == '__main__':
    unittest.main()