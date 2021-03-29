import os
import sys
import unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../../src/service"))

from homework_3 import Homework_3

class StringTransformerTest(unittest.TestCase):
    def setUp(self):
        self.transformer = Homework_3()

    def test_default_transformer(self):
        actual_output = self.transformer.transform("datatest")
        print(actual_output)
        expected_output = "default_prefix_datatest_default_suffix"

        self.assertEqual(actual_output, expected_output)
