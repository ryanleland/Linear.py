#!/usr/bin/env python

__version__ = '0.0.3'

from math import pi, sqrt, acos, degrees


class Vector(object):

    def __init__(self, *coordinates):
        self.coordinates = coordinates
        self.index = 0

    @property
    def x(self):
        return self.coordinates[0]

    @property
    def y(self):
        return self.coordinates[1]

    @property
    def z(self):
        return self.coordinates[2]

    @property
    def magnitude(self):
        return abs(sqrt(sum(c ** 2 for c in self)))

    def normalize(self):
        return self / self.magnitude

    def dot(self, other):
        return sum(a * b for a, b in zip(self, other))

    def cross(self, other):
        x = self.y * other.z - other.y * self.z
        y = -(self.x * other.z - other.x * self.z)
        z = self.x * other.y - other.x * self.y
        return Vector(x, y, z)

    def angle_in_radians(self, other):
        return acos(self.dot(other) / (self.magnitude * other.magnitude))

    def angle(self, other):
        return degrees(self.angle_in_radians(other))

    def is_orthogonal(self, other, tolerance=1e-10):
        return abs(self.dot(other)) < tolerance

    def is_parallel(self, other):
        return (self.is_zero()
            or other.is_zero()
            or self.angle_in_radians(other) == 0
            or self.angle_in_radians(other) == pi)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude < tolerance

    def __len__(self):
        return len(self.coordinates)

    def __iter__(self):
        return iter(self.coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        for a, b in zip(self, other):
            if a != b:
                return False

        return True

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
