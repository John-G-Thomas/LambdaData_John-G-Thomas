
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '{}. {}'.format((self.r, self.i)),

# class BasicClass:
# def __init__


# class AnothorClass:
# def __init__


# myobject = BasicClass()
# myobject
