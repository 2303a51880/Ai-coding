"""Vector mathematics module for multi-dimensional geometric operations.

This module provides a Vector class and utility functions for performing
mathematical operations on vectors in arbitrary dimensions. It supports
vector arithmetic (addition, subtraction), scaling, dot product computation,
magnitude calculation, normalization, and distance measurements between vectors.

Dependencies:
    - math: For mathematical operations (sqrt)
    - random: For generating random vectors

Key Components:
    Vector: A class representing a multi-dimensional vector with support for
            arithmetic operations, dot products, magnitude, and normalization.
    random_vector: Function to generate random vectors in a specified dimension
                   with optional bounds.
    distance: Function to calculate the Euclidean distance between two vectors.

Example Usage:
    >>> v1 = Vector(3, 4)
    >>> v2 = Vector(1, 2)
    >>> result = v1 + v2
    >>> print(result)
    Vector(4.0, 6.0)
    >>> mag = v1.magnitude()
    >>> print(mag)
    5.0
    >>> dist = distance(v1, v2)
    >>> print(dist)
    2.23606797749979
    >>> rand_vec = random_vector(3, low=0, high=1)
    >>> print(rand_vec.normalize())
    Vector(...)
"""

import math
import random

class Vector:
    def __init__(self, *coords):
        self._c = tuple(float(x) for x in coords)

    def __add__(self, other):
        return Vector(*(a + b for a, b in zip(self._c, other._c)))

    def __sub__(self, other):
        return Vector(*(a - b for a, b in zip(self._c, other._c)))

    def scale(self, k):
        return Vector(*(k * x for x in self._c))

    def dot(self, other):
        return sum(a * b for a, b in zip(self._c, other._c))

    def magnitude(self):
        return math.sqrt(self.dot(self))

    def normalize(self):
        m = self.magnitude()
        return self.scale(1 / m) if m else self

    def __repr__(self):
        return f"Vector{self._c}"

def random_vector(dim, low=-1.0, high=1.0):
    return Vector(*(random.uniform(low, high) for _ in range(dim)))

def distance(a, b):
    return (a - b).magnitude()
