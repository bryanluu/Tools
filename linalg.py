import numpy as np
from numbers import Number


'''
Implements an N-dimensional column vector of real numbers.
'''
class Vector:
    def __init__(self, data):
        try:
            iter(data)
        except TypeError as te:
            raise TypeError('Invalid iterable data')

        if all(isinstance(x, Number) for x in data):
            arr = np.array(data)
        else:
            raise ValueError('Invalid numeric data')

        if arr.ndim != 1:
            raise ValueError('Too many array dimensions')

        self.data = arr

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        return self.data.__getitem__(key)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return all(self.data == other.data)
        elif isinstance(other, list):
            if len(other) != len(self.data):
                return False
            return all(x == y for (x, y) in zip(self.data, other))
        else:
            return False

    '''
    Returns addition of vector with a scalar or vector of same length
    '''
    def __add__(self, other):
        if isinstance(other, Vector):
            if self.data.ndim != other.data.ndim:
                raise ValueError('Incompatible vector dimensions')
            return Vector(self.data + other.data)
        elif isinstance(other, Number):
            return Vector(self.data + other)
        else:
            try:
                return Vector(x + y for (x, y) in zip(self.data, other))
            except TypeError as te:
                raise TypeError("Other must be a scalar "
                                "or iterable of same length")

    '''
    Returns addition of vector with a scalar or vector of same length
    '''
    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.data.ndim != other.data.ndim:
                raise ValueError('Incompatible vector dimensions')
            return Vector(self.data - other.data)
        elif isinstance(other, Number):
            return Vector(self.data - other)
        else:
            try:
                return Vector(x - y for (x, y) in zip(self.data, other))
            except TypeError as te:
                raise TypeError("Other must be a scalar "
                                "or iterable of same length")

    def __neg__(self):
        return Vector(-self.data)

    '''
    Returns scalar or elementwise multiplication of vector
    '''
    def __mul__(self, other):
        if isinstance(other, Number):
            return Vector(other * self.data)
        elif isinstance(other, Vector):
            if self.data.ndim != other.data.ndim:
                raise TypeError('Incompatible vector dimensions')
            return Vector(self.data * other.data)
        else:
            try:
                return Vector(x * y for (x, y) in zip(self.data, other))
            except TypeError as te:
                raise TypeError("Other must be a scalar "
                                "or iterable of same length")

    '''
    Returns scalar or elementwise division of vector
    '''
    def __div__(self, other):
        if isinstance(other, Number):
            return Vector(self.data/other)
        if isinstance(other, Vector):
            if self.data.ndim != other.data.ndim:
                raise TypeError('Incompatible vector dimensions')
            return Vector(self.data/other.data)

    def __rmul__(self, other):
        if isinstance(other, Number):
            return Vector(other * self.data)
        else:
            try:
                return Vector(x*y for (x,y) in zip(self.data, other))
            except TypeError as te:
                raise TypeError("Other must be a scalar or iterable of same length")

    '''
    Returns vector dot product
    '''
    def dot(self, other):
        if isinstance(other, Vector):
            if self.data.ndim != other.data.ndim:
                raise ValueError("Vectors must be same length")
            return sum(x * y for (x, y) in zip(self.data, other.data))
        else:
            try:
                if len(other) != self.data.ndim:
                    raise ValueError("Incompatible lengths: expected "
                                    "{self.data.ndim} got {len(other)}")
                return sum(x * y for (x, y) in zip(self.data, other))
            except TypeError as te:
                raise TypeError("Other must be iterable of same length")

    '''
    Returns a deep copy of the vector
    '''
    def copy(self):
        return Vector(self.data.copy())

    @staticmethod
    def zeros(n):
        return Vector(np.zeros(n))

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.data += other.data
            return self
        elif isinstance(other, Number):
            self.data += other
            return self
        else:
            raise TypeError("Other must be a scalar or Vector")

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.data -= other.data
            return self
        elif isinstance(other, Number):
            self.data -= other
            return self
        else:
            raise TypeError("Other must be a scalar or Vector")

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)


