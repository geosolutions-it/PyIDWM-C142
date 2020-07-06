# -*- coding: utf-8 -*-
from unittest import TestCase
from pyidwm.Config import Config
from pyidwm.Value import Value, DistanceValue, CoordinateValue, AngleValue
from pyidwm.Units import Angle, Distance


class ValueTest(TestCase):

    def test_value(self):
        value = Value(1.0)
        self.assertEqual(value.getValue(), 1.0)
        self.assertIsNone(value.getUnit())

    def test_value_with_unit(self):
        value = Value(1.0, Distance.KILOMETERS)
        self.assertEqual(value.getValue(), 1.0)
        self.assertEqual(value.getUnit(), Distance.KILOMETERS)

    def test_distance_value(self):
        config = Config()
        config.distance_mode = "meters"
        value = DistanceValue(12.3)
        self.assertEqual(value.getValue(), 12.3)
        self.assertEqual(value.getUnit(), Distance.METERS)

    def test_distance_value_with_unit(self):
        value = DistanceValue(12.3, Distance.KILOMETERS)
        self.assertEqual(value.getValue(), 12.3)
        self.assertEqual(value.getUnit(), Distance.KILOMETERS)

    def test_coordinate_value(self):
        config = Config()
        config.angle_mode = "radians"
        value = CoordinateValue(0.1234)
        self.assertEqual(value.getValue(), 0.1234)
        self.assertEqual(value.getUnit(), Angle.RADIANS)

    def test_coordinate_value_with_unit(self):
        value = CoordinateValue(12.3, Angle.DEGREES)
        self.assertEqual(value.getValue(), 12.3)
        self.assertEqual(value.getUnit(), Angle.DEGREES)

    def test_angle_value(self):
        config = Config()
        config.angle_mode = "radians"
        value = AngleValue(0.1234)
        self.assertEqual(value.getValue(), 0.1234)
        self.assertEqual(value.getUnit(), Angle.RADIANS)

    def test_angle_value_with_unit(self):
        value = AngleValue(12.3, Angle.DEGREES)
        self.assertEqual(value.getValue(), 12.3)
        self.assertEqual(value.getUnit(), Angle.DEGREES)
