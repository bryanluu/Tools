from linalg import Vector, CVector, Vector2D
import unittest
import numpy as np
import math

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
        self.assertTrue(a == list(range(5)))

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

    def test_abs(self):
        u = Vector([3, 4])
        self.assertEqual(abs(u), 5)
        self.assertEqual(abs(-u), 5)



class TestCVectorMethods(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(TypeError):
            v = CVector(3)
        with self.assertRaises(ValueError):
            v = CVector([1, 2, '3'])
        with self.assertRaises(ValueError):
            v = CVector([[1, 2], [3, 4]])
        v = CVector([complex(x, x**2) for x in range(5)])
        self.assertTrue(all(v.data == [complex(x, x**2) for x in range(5)]))

    def test_CC(self):
        u = CVector(range(5))*1j
        self.assertEqual(u.CC(), -u)

    def test_dot(self):
        u = CVector(range(3))*1j
        v = CVector(range(3))*1j
        self.assertTrue(u.dot(v) == 5)


class TestVector2DMethods(unittest.TestCase):

    def setUp(self):
        # Vectors in each quadrant
        # Q1 is top right: x>0, y>0, and goes counter clockwise
        self.vectorQ1 = Vector2D(3, 4)
        self.vectorQ2 = Vector2D(-3, 4)
        self.vectorQ3 = Vector2D(-1, -1)
        self.vectorQ4 = Vector2D(6, -8)
        self.vectors = [
            self.vectorQ1, self.vectorQ2, self.vectorQ3, self.vectorQ4]

    def test_init(self):
        with self.assertRaises(TypeError):
            v = Vector2D(1,2,3)
        with self.assertRaises(TypeError):
            v = Vector2D([1,2,3])
        with self.assertRaises(ValueError):
            v = Vector2D(3, 'a')
        v = Vector2D(3, 4)
        self.assertTrue(v == [3, 4])

    def testAdditionToZero(self):
        for vector in self.vectors:
            actual = vector + Vector2D.zero()
            expected = vector
            self.assertEqual(actual, expected)

    def testAddition(self):
        actual = self.vectorQ1 + self.vectorQ2
        expected = Vector2D(0, 8)
        self.assertEqual(actual, expected)

        actual = self.vectorQ1 + 3
        expected = Vector2D(6, 7)
        self.assertEqual(actual, expected)

    def testAdditionToSelf(self):
        actual = Vector2D.zero()
        actual += self.vectorQ1
        expected = Vector2D(3, 4)
        self.assertEqual(actual, expected)

        actual = Vector2D(3, 4)
        actual += 3
        expected = Vector2D(6, 7)
        self.assertEqual(actual, expected)

    def testSubtraction(self):
        actual = self.vectorQ1 - self.vectorQ2
        expected = Vector2D(6, 0)
        self.assertEqual(actual, expected)

        actual = self.vectorQ1 - 3
        expected = Vector2D(0, 1)
        self.assertEqual(actual, expected)

    def testSubtractionToSelf(self):
        actual = Vector2D.zero()
        actual -= self.vectorQ1
        expected = Vector2D(-3, -4)
        self.assertEqual(actual, expected)

        actual = Vector2D(3, 4)
        actual -= 3
        expected = Vector2D(0, 1)
        self.assertEqual(actual, expected)

    def testScalarMultiplication(self):
        actual = self.vectorQ1 * 2
        expected = Vector2D(6, 8)
        self.assertEqual(actual, expected)

        actual = 2 * self.vectorQ1
        self.assertEqual(actual, expected)

    def testScalarDivision(self):
        actual = self.vectorQ1 / 2
        expected = Vector2D(1.5, 2)
        self.assertEqual(actual, expected)

    def testDotProduct(self):
        actual = self.vectorQ1.dot(self.vectorQ2)
        expected = 7
        self.assertEqual(actual, expected)

    def testCopy(self):
        actual = self.vectorQ1.copy()
        actual += 3
        expected = Vector2D(6, 7)
        self.assertEqual(actual, expected)
        self.assertNotEqual(actual, self.vectorQ1)

    def testAngles(self):
        north = Vector2D(0, 1)
        south = Vector2D(0, -1)
        west = Vector2D(-1, 0)
        east = Vector2D(1, 0)
        northeast = Vector2D(1, 1)
        northwest = Vector2D(-1, 1)
        southeast = Vector2D(1, -1)
        southwest = Vector2D(-1, -1)

        specialTriangle = Vector2D.create_from_angle(math.pi/6, 2)

        self.assertEqual(north.angle(), math.pi/2)
        self.assertEqual(south.angle(), -math.pi/2)
        self.assertEqual(west.angle(), math.pi)
        self.assertEqual(east.angle(), 0)

        self.assertAlmostEqual(northeast.angle(), math.pi/4, delta=0.01)
        self.assertAlmostEqual(northwest.angle(), 3*math.pi/4, delta=0.01)
        self.assertAlmostEqual(southeast.angle(), -math.pi/4, delta=0.01)
        self.assertAlmostEqual(southwest.angle(), -3*math.pi/4, delta=0.01)

        self.assertAlmostEqual(specialTriangle.angle(), math.pi/6, delta=0.01)

    def testAngleBetween(self):
        north = Vector2D(0, 1)
        south = Vector2D(0, -1)
        west = Vector2D(-1, 0)
        east = Vector2D(1, 0)
        northeast = Vector2D(1, 1)
        northwest = Vector2D(-1, 1)
        southeast = Vector2D(1, -1)
        southwest = Vector2D(-1, -1)

        self.assertAlmostEqual(
            Vector2D.angle_between(north, south), math.pi)
        self.assertAlmostEqual(
            Vector2D.angle_between(east, west), math.pi)
        self.assertAlmostEqual(
            Vector2D.angle_between(north, east), -math.pi/2)
        self.assertAlmostEqual(
            Vector2D.angle_between(north, west), math.pi/2)
        self.assertAlmostEqual(
            Vector2D.angle_between(southeast, south), -math.pi/4)
        self.assertAlmostEqual(
            Vector2D.angle_between(southeast, northeast), math.pi/2)
        self.assertAlmostEqual(
            Vector2D.angle_between(southeast, northwest), math.pi, places=5)
        self.assertAlmostEqual(
            Vector2D.angle_between(southeast, west), -3*math.pi/4)
        self.assertAlmostEqual(
            Vector2D.angle_between(southwest, north), -3*math.pi/4)
        self.assertAlmostEqual(
            Vector2D.angle_between(southwest, southeast), math.pi/2)
        self.assertAlmostEqual(
            Vector2D.angle_between(southwest, west), -math.pi/4)
        self.assertAlmostEqual(
            Vector2D.angle_between(southwest, southwest), 0, 5)

    def testCreateFromAngle(self):
        specialTriangle30 = Vector2D.create_from_angle(math.pi/6, 2)
        specialTriangle60 = Vector2D.create_from_angle(math.pi/3, 2)
        specialTriangle45 = Vector2D.create_from_angle(
            math.pi/4, math.sqrt(2))

        self.assertAlmostEqual(specialTriangle30.X(), math.sqrt(3))
        self.assertAlmostEqual(specialTriangle30.Y(), 1)

        self.assertAlmostEqual(specialTriangle60.X(), 1)
        self.assertAlmostEqual(specialTriangle60.Y(), math.sqrt(3))

        self.assertAlmostEqual(specialTriangle45.X(), 1)
        self.assertAlmostEqual(specialTriangle45.Y(), 1)

    # Also checks for immutability
    def tearDown(self):
        self.assertTrue(self.vectorQ1 == Vector2D(3, 4))
        self.assertTrue(self.vectorQ2 == Vector2D(-3, 4))
        self.assertTrue(self.vectorQ3 == Vector2D(-1, -1))
        self.assertTrue(self.vectorQ4 == Vector2D(6, -8))
        self.assertTrue(self.vectorQ1 == [3, 4])
        self.assertTrue(self.vectorQ2 == [-3, 4])
        self.assertTrue(self.vectorQ3 == [-1, -1])
        self.assertTrue(self.vectorQ4 == [6, -8])


if __name__ == '__main__':
    unittest.main()
