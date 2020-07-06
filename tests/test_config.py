# -*- coding: utf-8 -*-
from unittest import TestCase
from pyidwm.Config import Config
from pyidwm.Units import Angle, Distance


class ConfigTest(TestCase):

    def test_constructor(self):
        config = Config()
        self.assertIsInstance(config, Config)

    def test_config_is_singleton(self):
        config1 = Config()
        config1.geopackage = "path"
        self.assertEqual(config1.geopackage, "path")
        config2 = Config()
        self.assertEqual(config2.geopackage, "path")

    def test_layers(self):
        config = Config()
        self.assertTrue("country" in config.layers)

    def test_angle_mode(self):
        config = Config()
        self.assertEqual(config.angle_mode, Angle.DEGREES)

    def test_angle_mode_setter(self):
        config = Config()
        config.angle_mode = Angle.RADIANS
        self.assertEqual(config.angle_mode, Angle.RADIANS)

    def test_distance_mode(self):
        config = Config()
        self.assertEqual(config.distance_mode, Distance.KILOMETERS)

    def test_distance_mode_setter(self):
        config = Config()
        config.distance_mode = Distance.METERS
        self.assertEqual(config.distance_mode, Distance.METERS)

    def test_from_file_01(self):
        config = Config.FROM_FILE(__file__ + "/../data/config01.json")
        self.assertIsInstance(config, Config)
        self.assertEqual(config.geopackage, "mygeopackage.gpkg")
        self.assertEqual(config.angle_mode, Angle.RADIANS)
        self.assertEqual(config.distance_mode, Distance.METERS)
        self.assertEqual(config.layers["country"]["table"], "table_countries")
        self.assertEqual(config.layers["country"]["field_name"], "code")

    def test_from_file_02(self):
        config = Config.FROM_FILE(__file__ + "/../data/config02.json")
        self.assertIsInstance(config, Config)
        self.assertIsNone(config.geopackage)
        self.assertEqual(config.angle_mode, Angle.RADIANS)
        self.assertEqual(config.distance_mode, Distance.METERS)
        self.assertEqual(config.layers["country"]["table"], "table_countries")
        self.assertEqual(config.layers["country"]["field_name"], "code")

    def test_from_file_03(self):
        config = Config.FROM_FILE(__file__ + "/../data/config03.json")
        self.assertIsInstance(config, Config)
        self.assertEqual(config.geopackage, "mygeopackage.gpkg")
        self.assertEqual(config.angle_mode, Angle.DEGREES)
        self.assertEqual(config.distance_mode, Distance.METERS)
        self.assertEqual(config.layers["country"]["table"], "table_countries")
        self.assertEqual(config.layers["country"]["field_name"], "code")

    def test_from_file_04(self):
        config = Config.FROM_FILE(__file__ + "/../data/config04.json")
        self.assertIsInstance(config, Config)
        self.assertEqual(config.geopackage, "mygeopackage.gpkg")
        self.assertEqual(config.angle_mode, Angle.RADIANS)
        self.assertEqual(config.distance_mode, Distance.KILOMETERS)
        self.assertEqual(config.layers["country"]["table"], "table_countries")
        self.assertEqual(config.layers["country"]["field_name"], "code")

    def test_from_file_05(self):
        config = Config.FROM_FILE(__file__ + "/../data/config05.json")
        self.assertIsInstance(config, Config)
        self.assertEqual(config.geopackage, "mygeopackage.gpkg")
        self.assertEqual(config.angle_mode, Angle.RADIANS)
        self.assertEqual(config.distance_mode, Distance.METERS)
        self.assertEqual(config.layers["country"]["table"], "RRCountriesPoly")
        self.assertEqual(config.layers["country"]["field_name"], "CTRY")

    def test_from_not_existing_file(self):
        with self.assertRaises(Exception) as context:
            config = Config.FROM_FILE(__file__ + "/../data/not_existing.json")
        self.assertTrue('No such file or directory' in str(context.exception))
