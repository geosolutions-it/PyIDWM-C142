# -*- coding: utf-8 -*-
from unittest import TestCase
from pyidwm.Units import Angle, Distance, SpatialOperator


class UnitsTest(TestCase):

    def test_angle_from_string_degrees_upper(self):
        self.assertEqual(Angle.FROM_STRING("DEGREES"), Angle.DEGREES)

    def test_angle_from_string_degrees_lower(self):
        self.assertEqual(Angle.FROM_STRING("degrees"), Angle.DEGREES)

    def test_angle_from_string_radians_upper(self):
        self.assertEqual(Angle.FROM_STRING("RADIANS"), Angle.RADIANS)

    def test_angle_from_string_radians_lower(self):
        self.assertEqual(Angle.FROM_STRING("radians"), Angle.RADIANS)

    def test_angle_from_string_invalid(self):
        self.assertIsNone(Angle.FROM_STRING("invalid"))

    def test_angle_convert_radians_degrees(self):
        self.assertAlmostEqual(Angle.CONVERT(0, Angle.DEGREES, Angle.RADIANS), 0.0, 3)
        self.assertAlmostEqual(Angle.CONVERT(90, Angle.DEGREES, Angle.RADIANS), 1.570796, 3)
        self.assertAlmostEqual(Angle.CONVERT(180, Angle.DEGREES, Angle.RADIANS), 3.141592, 3)
        self.assertAlmostEqual(Angle.CONVERT(270, Angle.DEGREES, Angle.RADIANS), 4.712388, 3)
        self.assertAlmostEqual(Angle.CONVERT(360, Angle.DEGREES, Angle.RADIANS), 6.283185, 3)

    def test_angle_convert_degrees_radians(self):
        self.assertAlmostEqual(Angle.CONVERT(0.000000, Angle.RADIANS, Angle.DEGREES), 0, 3)
        self.assertAlmostEqual(Angle.CONVERT(1.570796, Angle.RADIANS, Angle.DEGREES), 90, 3)
        self.assertAlmostEqual(Angle.CONVERT(3.141592, Angle.RADIANS, Angle.DEGREES), 180, 3)
        self.assertAlmostEqual(Angle.CONVERT(4.712388, Angle.RADIANS, Angle.DEGREES), 270, 3)
        self.assertAlmostEqual(Angle.CONVERT(6.283185, Angle.RADIANS, Angle.DEGREES), 360, 3)

    def test_angle_convert_same_units(self):
        self.assertAlmostEqual(Angle.CONVERT(20.000000, Angle.RADIANS, Angle.RADIANS), 20.000000, 3)

    def test_angle_convert_with_invalid_unit(self):
        self.assertIsNone(Angle.CONVERT(20.000000, Angle.RADIANS, Angle.FROM_STRING("invalid")))

    def test_distance_from_string_meters_upper(self):
        self.assertEqual(Distance.FROM_STRING("meters"), Distance.METERS)

    def test_distance_from_string_meters_lower(self):
        self.assertEqual(Distance.FROM_STRING("meters"), Distance.METERS)

    def test_distance_from_string_kilometers_upper(self):
        self.assertEqual(Distance.FROM_STRING("KILOMETERS"), Distance.KILOMETERS)

    def test_distance_from_string_kilometers_lower(self):
        self.assertEqual(Distance.FROM_STRING("kilometers"), Distance.KILOMETERS)

    def test_distance_from_string_invalid(self):
        self.assertIsNone(Distance.FROM_STRING("invalid"))

    def test_distance_convert_meters_kilometers(self):
        self.assertAlmostEqual(Distance.CONVERT(1000, Distance.METERS, Distance.KILOMETERS), 1, 3)

    def test_distance_convert_kilometers_meters(self):
        self.assertAlmostEqual(Distance.CONVERT(1, Distance.KILOMETERS, Distance.METERS), 1000, 3)

    def test_distance_convert_same_units(self):
        self.assertAlmostEqual(Distance.CONVERT(1000, Distance.METERS, Distance.METERS), 1000, 3)

    def test_distance_convert_with_invalid_unit(self):
        self.assertIsNone(Distance.CONVERT(20.000000, Distance.METERS, Distance.FROM_STRING("invalid")))

    def test_spatial_operator_from_string_intersects_upper(self):
        self.assertEqual(SpatialOperator.FROM_STRING("INTERSECTS"), SpatialOperator.INTERSECTS)

    def test_spatial_operator_from_string_intersects_lower(self):
        self.assertEqual(SpatialOperator.FROM_STRING("intersects"), SpatialOperator.INTERSECTS)

    def test_spatial_operator_from_string_within_upper(self):
        self.assertEqual(SpatialOperator.FROM_STRING("WITHIN"), SpatialOperator.WITHIN)

    def test_spatial_operator_from_string_within_lower(self):
        self.assertEqual(SpatialOperator.FROM_STRING("within"), SpatialOperator.WITHIN)

    def test_spatial_operator_from_string_invalid(self):
        self.assertIsNone(SpatialOperator.FROM_STRING("invalid"))
