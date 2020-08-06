import unittest
from random import randint

"""# unittest supports a type of tests called unit tests
# A unit is the smallest cohesive piece of code we can test
# (usually something like a function or method)
# Other types of tests (you won't write now, just to be aware):
# - Integration: testing multiple prices working together
# - End to end: testing a full "flow"/use case
# There are also manual/non-code tests that are common
# - User acceptance testing: show it5 to a user, got feedback
# - Manual running and checking"""


class calculator(unittest.TestCase):
    """Making sure our class behave as expected."""

    def add(self):
        """Testing that increment adds one to a number."""
        x1 = 5
        y1 = increment(x1)
        x2 = -106
        y2 = increment(x2)
        # Now we make sure the output is as expected with assertions
        self.assertEqual(y1, 6)
        self.assertEqual(y2, -105)
    def add(self):

    def test_increment_random(self):
        """Test increment with randomly generated input."""
        x1 = randint(1, 10000000)
        y1 = increment(x1)
        self.assertEqual(y1, x1 + 1)
