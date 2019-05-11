from linalg import Vector
import unittest
import numpy as np

class TestVectorMethods(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(TypeError):
            v = Vector(3)
        with self.assertRaises(ValueError):
            v = Vector([1, 2, '3'])
        with self.assertRaises(ValueError):
            v = Vector([[1, 2], [3, 4]])
        v = Vector([x**2 for x in range(5)])
        self.assertTrue(all(v.data == [x**2 for x in range(5)]))

    def test_iter(self):
        v = Vector(range(5))
        a = [x for x in v]
        self.assertTrue(a == range(5))

    def test_equal(self):
        a = list(range(5))
        v = Vector(a)
        self.assertTrue(v == a)
        a[-1] = 0 # modify a but not v
        self.assertFalse(v == a)

    def test_getitem(self):
        v = Vector(range(5))
        self.assertTrue(v[-1] == 4)
        self.assertTrue(all(v[1:] == [1,2,3,4]))

    def test_add(self):
        a = list(range(5))
        b = list(range(4,-1,-1))
        c = [3,4,5,6,7]
        v = Vector(a)
        u = Vector(b)
        w = u+v
        self.assertTrue(all(x == 4 for x in w))
        self.assertTrue(v+3 == c)

    def test_sub(self):
        a = list(range(5))
        b = list(range(5))
        c = [-1,0,1,2,3]
        v = Vector(a)
        u = Vector(b)
        w = u-v
        self.assertTrue(all(x == 0 for x in w))
        self.assertTrue(v-1 == c)

    def test_iadd(self):
        a = list(range(5))
        b = list(range(4,-1,-1))
        c = [3,4,5,6,7]
        v = Vector(a)
        u = Vector(b)
        w = v.copy()
        v += u
        w += 3
        self.assertTrue(v == [4]*5)
        self.assertTrue(w == c)

    def test_isub(self):
        a = list(range(5))
        c = [-1,0,1,2,3]
        v = Vector(a)
        u = Vector(a)
        w = v.copy()
        v -= u
        w -= 1
        self.assertTrue(v == Vector.zeros(5))
        self.assertTrue(w == c)

    def test_mul(self):
        a = list(range(5))
        b = list(range(5))
        c = [0,1,4,9,16]
        v = Vector(a)
        u = Vector(b)
        w = u*v
        self.assertTrue(w == c)
        self.assertTrue(2*v == [0,2,4,6,8])

    def test_div(self):
        a = list(range(5))
        c = [x/2 for x in range(5)]
        v = Vector(a)
        w = v/2
        self.assertTrue(w == c)
        self.assertTrue(x == 1 for x in (v+1)/(v+1))

    def test_dot(self):
        u = Vector(range(5))
        v = Vector(range(5))
        self.assertTrue(u.dot(v) == sum(x*x for x in range(5)))

    def test_zero(self):
        v = Vector.zeros(5)
        self.assertTrue(all(x == 0 for x in v))

    def test_copy(self):
        v = Vector(range(5))
        u = v.copy()
        w = v
        self.assertFalse(u is v)
        self.assertTrue(w is v)

    def test_neg(self):
        v = Vector(range(5))
        self.assertTrue(-v == -1*v)
        self.assertTrue(--v == v)

if __name__ == '__main__':
    unittest.main()
