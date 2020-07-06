# -*- coding: utf-8 -*-
from unittest import TestCase
from pyidwm.Config import Config
from pyidwm.Api import Api
from pyidwm.Units import Angle, Distance, SpatialOperator
from pyidwm.Value import AngleValue


class ApiTest(TestCase):

    def geoplc(self, lon, lat, angle_mode=None):
        config = Config()
        config.angle_mode = Angle.DEGREES
        config.geopackage = __file__ + "/../data/idwm.gpkg"
        api = Api()
        return api.geoplc(AngleValue(lon, angle_mode), AngleValue(lat, angle_mode))

    def test_geoplc_water(self):
        result = self.geoplc(11.735, 39.844)
        self.assertIsNone(result)

    def test_geoplc_degrees_water(self):
        result = self.geoplc(11.735, 39.844, Angle.DEGREES)
        self.assertIsNone(result)

    def test_geoplc_radians_water(self):
        result = self.geoplc(0.204814388, 0.695408987, Angle.RADIANS)
        self.assertIsNone(result)

    def test_geoplc_italy(self):
        result = self.geoplc(12.525, 42.721)
        self.assertEqual(result, "I")

    def test_geoplc_degrees_italy(self):
        result = self.geoplc(12.525, 42.721, Angle.DEGREES)
        self.assertEqual(result, "I")

    def test_geoplc_radians_italy(self):
        result = self.geoplc(0.218602489, 0.74562211, Angle.RADIANS)
        self.assertEqual(result, "I")

    def test_geoplc_switzerland(self):
        result = self.geoplc(7.87, 46.87)
        self.assertEqual(result, "SUI")

    def test_geoplc_degrees_switzerland(self):
        result = self.geoplc(7.87, 46.87, Angle.DEGREES)
        self.assertEqual(result, "SUI")

    def test_geoplc_radians_switzerland(self):
        result = self.geoplc(0.137357412131954,	0.818035820409742, Angle.RADIANS)
        self.assertEqual(result, "SUI")

    def test_geoplc_sanmarino(self):
        result = self.geoplc(12.459, 43.943)
        self.assertEqual(result, "SMR")

    def test_geoplc_degrees_sanmarino(self):
        result = self.geoplc(12.459, 43.943, Angle.DEGREES)
        self.assertEqual(result, "SMR")

    def test_geoplc_radians_sanmarino(self):
        result = self.geoplc(0.217450571505973, 0.766950033203868, Angle.RADIANS)
        self.assertEqual(result, "SMR")

    def test_geoplc_greece(self):
        result = self.geoplc(26.063, 38.397)
        self.assertEqual(result, "GRC")

    def test_geoplc_degrees_greece(self):
        result = self.geoplc(26.063, 38.397, Angle.DEGREES)
        self.assertEqual(result, "GRC")

    def test_geoplc_radians_greece(self):
        result = self.geoplc(0.454885162947282, 0.670154072888263, Angle.RADIANS)
        self.assertEqual(result, "GRC")


