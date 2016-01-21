from math import sqrt


class Vector(object):

    def __init__(self, *coordinates):
        self.coordinates = coordinates
        self.index = 0

    def magnitude(self):
        return abs(sqrt(sum(c ** 2 for c in self)))

    def normalize(self):
        return self / self.magnitude()

    def __len__(self):
        return len(self.coordinates)

    def __iter__(self):
        return iter(self.coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __add__(self, other):
        coordinates = (a + b for a, b in zip(self, other))
        return Vector(*coordinates)

    def __sub__(self, other):
        coordinates = (a - b for a, b in zip(self, other))
        return Vector(*coordinates)

    def __mul__(self, other):
        coordinates = (c * other for c in self)
        return Vector(*coordinates)

    def __div__(self, other):
        coordinates = (c / other for c in self)
        return Vector(*coordinates)

    def __str__(self):
        return str(self.coordinates)

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    v1 = Vector(-1, 1)
    print v1.normalize(), v1.mag()
