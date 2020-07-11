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

    def test_add_2_distance_value_with_same_units(self):
        value1 = DistanceValue(5.0, Distance.METERS)
        value2 = DistanceValue(8.0, Distance.METERS)
        value = value1 + value2
        self.assertEqual(value.getValue(), 13.0)
        self.assertEqual(value.getUnit(), Distance.METERS)

    def test_add_2_distance_value_with_different_units_01(self):
        value1 = DistanceValue(5.0, Distance.METERS)
        value2 = DistanceValue(0.3, Distance.KILOMETERS)
        value = value1 + value2
        self.assertEqual(value.getValue(), 305.0)
        self.assertEqual(value.getUnit(), Distance.METERS)

    def test_add_2_distance_value_with_different_units_02(self):
        value1 = DistanceValue(0.3, Distance.KILOMETERS)
        value2 = DistanceValue(5.0, Distance.METERS)
        value = value1 + value2
        self.assertEqual(value.getValue(), 0.305)
        self.assertEqual(value.getUnit(), Distance.KILOMETERS)

    def test_sub_2_distance_value_with_same_units_01(self):
        value1 = DistanceValue(8.0, Distance.METERS)
        value2 = DistanceValue(3.0, Distance.METERS)
        value = value1 - value2
        self.assertEqual(value.getValue(), 5.0)
        self.assertEqual(value.getUnit(), Distance.METERS)

    def test_sub_2_distance_value_with_same_units_02(self):
        value1 = DistanceValue(3.0, Distance.METERS)
        value2 = DistanceValue(8.0, Distance.METERS)
        value = value1 - value2
        self.assertEqual(value.getValue(), -5.0)
        self.assertEqual(value.getUnit(), Distance.METERS)

    def test_sub_2_distance_value_with_different_units_01(self):
        value1 = DistanceValue(1.0, Distance.KILOMETERS)
        value2 = DistanceValue(300.0, Distance.METERS)
        value = value1 - value2
        self.assertEqual(value.getValue(), 0.7)
        self.assertEqual(value.getUnit(), Distance.KILOMETERS)

    def test_sub_2_distance_value_with_different_units_02(self):
        value1 = DistanceValue(300.0, Distance.METERS)
        value2 = DistanceValue(1.0, Distance.KILOMETERS)
        value = value1 - value2
        self.assertEqual(value.getValue(), -700.0)
        self.assertEqual(value.getUnit(), Distance.METERS)
