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
