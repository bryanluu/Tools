import numpy as np
from numbers import Number
import math


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
            raise ValueError(f'Too many array dimensions ({arr.ndim})')

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
    def __truediv__(self, other):
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
            return np.sum(self.data * other.data)
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

    def __abs__(self):
        return np.sqrt(self.dot(self))



'''
Implements an N-dimensional vector of complex numbers.
'''
class CVector(Vector):
    def __init__(self, data):
        try:
            iter(data)
        except TypeError as te:
            raise TypeError('Invalid iterable data')

        if all(isinstance(x, Number) for x in data):
            arr = np.array([complex(x) for x in data])
        else:
            raise ValueError('Invalid numeric data')

        if arr.ndim != 1:
            raise ValueError('Too many array dimensions')

        self.data = arr

    def __add__(self, other):
        return CVector(super().__add__(other).data)

    def __sub__(self, other):
        return CVector(super().__sub__(other).data)

    def __mul__(self, other):
        return CVector(super().__mul__(other).data)

    def __truediv__(self, other):
        return CVector(super().__truediv__(other).data)

    def __neg__(self):
        return CVector(-(self.data))

    def __rmul__(self, other):
        return CVector(other*(self.data))

    '''
    Returns a deep copy of the vector
    '''
    def copy(self):
        return CVector(self.data.copy())

    @staticmethod
    def zeros(n):
        return CVector(np.zeros(n))

    '''
    Returns a complex conjugate version of the vector
    '''
    def CC(self):
        return CVector(np.conj(self.data))

    '''
    Do an inner product in complex vector (Hilbert) space
    '''
    def dot(self, other):
        return Vector.dot(self.CC(), other)


'''
Implements an 2-dimensional vector of real numbers.
'''
class Vector2D(Vector):
    def __init__(self, *args):
        n = len(args)
        if n == 2:
            super().__init__(args)
        elif n == 1:
            if isinstance(args[0], Vector):
                if len(args[0].data) != 2:
                    raise ValueError('Only 2 dimensions are allowed')
            elif len(args[0]) != 2:
                raise TypeError('Only 2 dimensions are allowed')
            super().__init__(args[0])
        else:
            raise TypeError('Only 2 dimensions are allowed')


    def __add__(self, other):
        return Vector2D(super().__add__(other).data)

    def __sub__(self, other):
        return Vector2D(super().__sub__(other).data)

    def __mul__(self, other):
        return Vector2D(super().__mul__(other).data)

    def __truediv__(self, other):
        return Vector2D(super().__truediv__(other).data)

    def __neg__(self):
        return Vector2D(-(self.data))

    def __rmul__(self, other):
        return Vector2D(other*(self.data))

    def X(self):
        return self.data[0]

    def Y(self):
        return self.data[1]

    def XY(self):
        return (self.data[0], self.data[1])

    def angle(self):
        """
        Returns the angle, measured as 0 radians from x-axis, in radians
        """
        x, y = self.XY()

        if x == 0:
            return math.pi/2 if y > 0 else -math.pi/2

        if y == 0:
            return 0 if x > 0 else math.pi

        angle = math.atan2(y, x)

        return angle

    @staticmethod
    def create_from_angle(angle, length):
        """
        Creates a vector according to the angle and length of the vector.

        Angle: an angle in radians, where the angle is measured from 0 on the x-axis,
        and angle goes from -180 (on the bottom) to +180 (on the top).
        Length: must be a scalar number
        """
        # convert to radians
        x = length * math.cos(angle)
        y = length * math.sin(angle)
        return Vector2D([x, y])

    '''
    Returns a deep copy of the vector
    '''
    def copy(self):
        return Vector2D(self.data.copy())

    @staticmethod
    def zero():
        return Vector2D(np.zeros(2))

    @staticmethod
    def angle_between(u, v):
        """
        Finds the angle of v w.r.t to u.

        :param u: Reference vector to measure angle to
        :param v: Vector to measure angle of w.r.t u
        :return: Angle between the two vectors, where 0 means they point in the same direction
        -90 means v points to the west of u, etc. 0 is returned if either is a zero vector.
        """
        if u == Vector2D.zero() or v == Vector2D.zero():
            return 0
        # Use dot product to find angle
        angle = math.acos(Vector2D.dot(u, v) / (abs(u) * abs(v)))

        u_angle = u.angle()
        v_angle = v.angle()

        if u_angle >= 0:
            if v_angle < u_angle:
                return -angle if v_angle > u_angle - math.pi else angle
            else:
                return angle
        else:
            if v_angle > u_angle:
                return angle if v_angle <= u_angle + math.pi else -angle
            else:
                return -angle

