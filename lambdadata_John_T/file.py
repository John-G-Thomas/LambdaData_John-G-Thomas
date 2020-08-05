import math
import pandas as pd


class MyDataFrame(pd.DataFrame):
    def _constructor_expanddim(self):
        pass

    def num_cells(self):
        return self.shape[0] * self.shape[1]


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name):
        self.name = name
        self.upvotes = 0

    def receive_upvote(self):
        self.upvotes += 1

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """General representation of animals."""

    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = weight
        self.diet_type = diet_type

    def run(self):
        return 'Vroom!'


def eat(food):
    return food + ' is delicious, yum!'


def say_great():
    return "It's GREEAAAAT!"


class Tiger(Animal):
    """Representation of tigers, a subclass of Animal."""

    def __nit__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = num_stripes

    # Example of overriding
    def run(self):
        return 'Scamperwoosh!'


def example1():
    # This is a long comment. This should be wrapped to fit within 72
    # characters.
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        'long': 'Long code lines should be wrapped within 79 characters.',
        'other': [math.pi, 100, 200, 300, 9876543210,
                  'This is a long string that goes on'],
        'more': {'inner': 'This whole logical line should be wrapped.',
                 some_tuple: [1, 20, 300, 40000, 500000000,
                              60000000000000000]}}
    return some_tuple, some_variable


def example2():
    return {'has_key() is deprecated': True}.has_key({'f': 2}.has_key(''))
