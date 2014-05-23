from unittest import TestCase
from numpy import *
import matrix


class MatrixTest(TestCase):
    def test_incidenceAngle(self):
        rot = 0
        self.assertEqual(matrix.incidenceAngle(rot), pi/4)
