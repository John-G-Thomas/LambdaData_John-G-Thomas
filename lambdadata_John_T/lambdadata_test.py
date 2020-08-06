#!/usr/bin/env/ python
"""Tests for lambdata modules."""

import unittest
from random import randint
from .file import SocialMediaUser


def increment(number):
    """Increases a given number by 1."""
    return number + 1


COLORS = ('Blue', 'Orange', 'Red', 'Green', 'Violet', 'Cyan')


# unittest supports a type of tests called unit tests
# A unit is the smallest cohesive piece of code we can test
# (usually something like a function or method)
# Other types of tests (you won't write now, just to be aware):
# - Intgration: testing multiple pices working together
# - End to end: testing a full "flow"/use case
# There are also manual/non-code tests that are common
# - User acceptance testing: show it5 to a user, got feedback
# - Manual running and chekcing


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

    def test_increment_random(self):
        """Test increment with randomly generated input."""
        x1 = randint(1, 10000000)
        y1 = increment(x1)
        self.assertEqual(y1, x1 + 1)

    def test_colors(self):
        """Testing presence/absence of expected colors."""
        self.assertIn('Orange', COLORS)
        self.assertNotIn('Aqumarine', COLORS)
        self.assertEqual(len(COLORS), 6)


class SocalMeidaUserTests(unittest.TestCase):
    """Test the instatiation and use of SocialMediaUser"""

    def test_name(self):
        """Test that the name field is assigned correctly."""
        user1 = SocialMediaUser('Jane')
        user2 = SocialMediaUser('Joe')
        self.assertEqual(user1.name, 'Jane')
        self.assertEqual(user2.name, 'Joe')

    def test_default_upvotes(self):
        """Test that the default upvotes of a new user is 0."""
        user1 = SocialMediaUser('Jane')
        self.assertEqual(user1.upvotes, 0)

    def test_unpopular(self):
        """Test that a user with <=100 upvotes is not popular."""
        user1 = SocialMediaUser('Joe')
        for _ in range(randint(1, 100)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), False)

    def test_popular(self):
        """Test that a user with >100 upvotes is popular"""
        user1 = SocialMediaUser('Jane')
        for _ in range(randint(101, 10000)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), True)


if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()
