# -*- coding: utf-8 -*-
from unittest import TestCase
from pyidwm.Config import Config
from pyidwm.Api import Api
from pyidwm.Units import Angle, Distance, SpatialOperator
from pyidwm.Value import AngleValue, DistanceValue


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

    def geoalc(self, lon, lat, max_dist_value, azimuth, angle_mode=None, iwc=0, max_cros=100, arc_approximation=20):
        config = Config()
        config.angle_mode = Angle.DEGREES
        config.geopackage = __file__ + "/../data/idwm.gpkg"
        api = Api()
        return api.geoalc(
            AngleValue(lon, angle_mode),
            AngleValue(lat, angle_mode),
            max_dist_value,
            azimuth,
            iwc, max_cros, arc_approximation)

    def test_geoalc_completely_in_sea(self):
        result = self.geoalc(11.07079, 41.19145, DistanceValue(100, Distance.KILOMETERS), 45.0, Angle.DEGREES)
        self.assertEqual(len(result), 1)
        self.assertIsNone(result[0]["name"])
        self.assertAlmostEqual(result[0]["total_distance"].getValue(), 100.0, 2)
        self.assertAlmostEqual(result[0]["partial_distance"].getValue(), 100.0, 2)
        self.assertAlmostEqual(result[0]["point"][0].getValue(), 11.92414, 4)
        self.assertAlmostEqual(result[0]["point"][1].getValue(), 41.82423, 4)

    def test_geoalc_sea_italy(self):
        result = self.geoalc(11.07079, 41.19145, DistanceValue(200, Distance.KILOMETERS), 45.0, Angle.DEGREES)
        self.assertEqual(len(result), 2)
        self.assertIsNone(result[0]["name"])
        self.assertAlmostEqual(result[0]["total_distance"].getValue(), 118.41438, 2)
        self.assertAlmostEqual(result[0]["partial_distance"].getValue(), 118.41438, 2)
        self.assertAlmostEqual(result[0]["point"][0].getValue(), 12.08312, 4)
        self.assertAlmostEqual(result[0]["point"][1].getValue(), 41.94005, 4)
        self.assertEqual(result[1]["name"], "I")
        self.assertAlmostEqual(result[1]["total_distance"].getValue(), 200.000, 2)
        self.assertAlmostEqual(result[1]["partial_distance"].getValue(), 81.58561, 2)
        self.assertAlmostEqual(result[1]["point"][0].getValue(), 12.79444, 4)
        self.assertAlmostEqual(result[1]["point"][1].getValue(), 42.45057, 4)

    def test_geoalc_sea_sardinia_italy(self):
        result = self.geoalc(7.28857, 39.08092, DistanceValue(600, Distance.KILOMETERS), 45.0, Angle.DEGREES)
        self.assertEqual(len(result), 4)
        self.assertIsNone(result[0]["name"])
        self.assertAlmostEqual(result[0]["total_distance"].getValue(), 133.851, 2)
        self.assertAlmostEqual(result[0]["partial_distance"].getValue(), 133.851, 2)
        self.assertAlmostEqual(result[0]["point"][0].getValue(), 8.39861, 4)
        self.assertAlmostEqual(result[0]["point"][1].getValue(), 39.92678, 4)
        self.assertEqual(result[1]["name"], "I")
        self.assertAlmostEqual(result[1]["total_distance"].getValue(), 283.599, 2)
        self.assertAlmostEqual(result[1]["partial_distance"].getValue(), 149.748, 2)
        self.assertAlmostEqual(result[1]["point"][0].getValue(), 9.67303, 4)
        self.assertAlmostEqual(result[1]["point"][1].getValue(), 40.86040, 4)
        self.assertIsNone(result[2]["name"])
        self.assertAlmostEqual(result[2]["total_distance"].getValue(), 510.894, 2)
        self.assertAlmostEqual(result[2]["partial_distance"].getValue(), 227.295, 2)
        self.assertAlmostEqual(result[2]["point"][0].getValue(), 11.67727, 4)
        self.assertAlmostEqual(result[2]["point"][1].getValue(), 42.24944, 4)
        self.assertEqual(result[3]["name"], "I")
        self.assertAlmostEqual(result[3]["total_distance"].getValue(), 599.99999, 2)
        self.assertAlmostEqual(result[3]["partial_distance"].getValue(), 89.105, 2)
        self.assertAlmostEqual(result[3]["point"][0].getValue(), 12.48684, 4)
        self.assertAlmostEqual(result[3]["point"][1].getValue(), 42.78433, 4)

    def test_geoalc_sea_sardinia_italy_maxcross_2(self):
        result = self.geoalc(7.28857, 39.08092, DistanceValue(600, Distance.KILOMETERS), 45.0, Angle.DEGREES, 1, 2)
        self.assertEqual(len(result), 2)
        self.assertIsNone(result[0]["name"])
        self.assertAlmostEqual(result[0]["total_distance"].getValue(), 133.851, 2)
        self.assertAlmostEqual(result[0]["partial_distance"].getValue(), 133.851, 2)
        self.assertAlmostEqual(result[0]["point"][0].getValue(), 8.39861, 4)
        self.assertAlmostEqual(result[0]["point"][1].getValue(), 39.92678, 4)
        self.assertEqual(result[1]["name"], "+++")
        self.assertAlmostEqual(result[1]["total_distance"].getValue(), 283.599, 2)
        self.assertAlmostEqual(result[1]["partial_distance"].getValue(), 149.748, 2)
        self.assertAlmostEqual(result[1]["point"][0].getValue(), 9.67303, 4)
        self.assertAlmostEqual(result[1]["point"][1].getValue(), 40.86040, 4)

    def test_geoalc_sea_sardinia_italy_official(self):
        result = self.geoalc(7.0, 39.0, DistanceValue(700, Distance.KILOMETERS), 45.0, Angle.DEGREES, 1, 100, 100)
        self.assertEqual(len(result), 4)
        self.assertIsNone(result[0]["name"])
        self.assertAlmostEqual(result[0]["total_distance"].getValue(), 177.755, 2)
        self.assertAlmostEqual(result[0]["partial_distance"].getValue(), 177.755, 2)
        self.assertAlmostEqual(result[0]["point"][0].getValue(), 8.47820, 4)
        self.assertAlmostEqual(result[0]["point"][1].getValue(), 40.12112, 4)
        self.assertEqual(result[1]["name"], "+++")
        self.assertAlmostEqual(result[1]["total_distance"].getValue(), 304.842, 2)
        self.assertAlmostEqual(result[1]["partial_distance"].getValue(), 127.087, 2)
        self.assertAlmostEqual(result[1]["point"][0].getValue(), 9.56501, 4)
        self.assertAlmostEqual(result[1]["point"][1].getValue(), 40.91085, 4)
        self.assertIsNone(result[2]["name"])
        self.assertAlmostEqual(result[2]["total_distance"].getValue(), 534.517, 2)
        self.assertAlmostEqual(result[2]["partial_distance"].getValue(), 229.674, 2)
        self.assertAlmostEqual(result[2]["point"][0].getValue(), 11.59601, 4)
        self.assertAlmostEqual(result[2]["point"][1].getValue(), 42.31119, 4)
        self.assertEqual(result[3]["name"], "+++")
        self.assertAlmostEqual(result[3]["total_distance"].getValue(), 699.999, 2)
        self.assertAlmostEqual(result[3]["partial_distance"].getValue(), 165.48228, 2)
        self.assertAlmostEqual(result[3]["point"][0].getValue(), 13.11550, 4)
        self.assertAlmostEqual(result[3]["point"][1].getValue(), 43.29714, 4)
