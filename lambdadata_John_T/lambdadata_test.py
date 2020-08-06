#!/usr/bin/env/ python
"""Tests for lambdata modules."""

import unittest
from random import randint
# unittest supports a type of tests called unit tests
# A unit is the smallest cohesive piece of code we can test
# (usually something like a function or method)

# OTher types of tests (you won't write now, just to be aware):
# - Intgratio: testing multiple pices working together
# - End to end: testing a full "flow"/use case
# There are also manual/non-code tests that are common
# - User acceptance testing: show it5 to a user, got feedback
# - Manual running and chekcing

from lambdadata_John_T import increment, COLORS
from lambdadata_John_T.file import SocialMediaUser


class ExampleUnitTests(unittest.TestCase):
    """Making sure our examples behave as expected."""

    def test_increment(self):
        """Testing that increment adds one to a number."""
        x1 = 5
        y1 = increment(x1)
        x2 = -106
        y2 = increment(x2)
        # Now we make sure the output is as expected with assertions
        self.assertEqual(y1, 6)
        self.assertEqual(y2, -105)


if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()
