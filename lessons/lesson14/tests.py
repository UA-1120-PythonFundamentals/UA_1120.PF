import unittest
from point import Point


class PointTest(unittest.TestCase):
    def test_create_deloult(self):
        point = Point()
        self.assertEqual(point.x, 0, "x")
        self.assertEqual(
            point.y,
            0,
        )

    def test_create_deloult1(self):
        point = Point(1)
        self.assertEqual(point.x, 1, "x")
        self.assertEqual(
            point.y,
            0,
        )

    def test_create_deloult2(self):
        point = Point(-1, 5)
        self.assertEqual(point.x, -1, "x")
        self.assertEqual(point.y, -5, "y")

    def test_add(self):
        point1 = Point(-1, 5)
        point2 = Point(-1, 5)
        point3 = point1 + point2

        self.assertEqual(point3.x, -2, "x")
        self.assertEqual(point3.y, 10, "y")


if __name__ == "__main__":
    unittest.main()
