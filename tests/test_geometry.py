# -*- coding: utf-8 -*-
from osgeo import ogr
from unittest import TestCase
from pyidwm.Config import Config
from pyidwm.helper.Geometry import *
from pyidwm.Units import *
from pyidwm.Value import *


class GeometryTest(TestCase):

    def test_get_segments_count_n_minus_1(self):
        self.assertEqual(Geometry.get_segments_count(10), 9)

    def test_get_segments_count_1(self):
        self.assertEqual(Geometry.get_segments_count(2), 1)

    def test_get_segments_count_0(self):
        self.assertEqual(Geometry.get_segments_count(0), 0)
        self.assertEqual(Geometry.get_segments_count(1), 0)

    def test_create_buffer(self):
        lon_value = CoordinateValue(12.3, Angle.DEGREES)
        lat_value = CoordinateValue(45.6, Angle.DEGREES)
        radius_value = DistanceValue(18.2, Distance.KILOMETERS)
        circle = Geometry.create_buffer(lon_value, lat_value, radius_value)
        self.assertEqual(str(circle), "POLYGON ((12.3 45.7636765322772 0,12.4657597312244 45.7156170926263 0,"
                                      "12.5339354636961 45.5997612653316 0,12.4650773011197 45.4841441707049 0,"
                                      "12.3 45.4363234677228 0,12.1349226988803 45.4841441707049 0,"
                                      "12.0660645363039 45.5997612653316 0,12.1342402687756 45.7156170926263 0,"
                                      "12.3 45.7636765322772 0))")

    def test_create_great_circular_arc(self):
        projection = Projection.get_aeqd_proj(12.3, 45.6, Angle.DEGREES)
        line = Geometry.create_great_circular_arc(projection, 1000, 1000, 3)
        self.assertIsInstance(line, ogr.Geometry)
        self.assertEqual(str(line), "LINESTRING (12.3 45.6 0,"
                                    "12.3064273317806 45.6044964278275 0,"
                                    "12.3128556939183 45.6089924951745 0)")

    def test_create_great_circular_arc_from_2_points(self):
        s_lon_value = CoordinateValue(12.1, Angle.DEGREES)
        s_lat_value = CoordinateValue(45.6, Angle.DEGREES)
        e_lon_value = CoordinateValue(15.3, Angle.DEGREES)
        e_lat_value = CoordinateValue(45.9, Angle.DEGREES)
        line = Geometry.create_great_circular_arc_from_2_points(s_lon_value, s_lat_value, e_lon_value, e_lat_value, 5)
        self.assertIsInstance(line, ogr.Geometry)
        self.assertEqual(str(line), "LINESTRING (12.1 45.6 0,"
                                    "12.8967002866441 45.6833606270848 0,"
                                    "13.6956989586903 45.7611675931092 0,"
                                    "14.4968489821408 45.8333902604146 0,"
                                    "15.3 45.9 0)")

    def test_create_great_circular_arc_from_point_azimuth_distance(self):
        s_lon_value = CoordinateValue(12.1, Angle.DEGREES)
        s_lat_value = CoordinateValue(45.6, Angle.DEGREES)
        azimuth = 45.0
        distance_value = DistanceValue(100.0, Distance.KILOMETERS)
        line = Geometry.create_great_circular_arc_from_point_azimuth_distance(
            s_lon_value, s_lat_value, azimuth, distance_value, 5)
        self.assertIsInstance(line, ogr.Geometry)
        self.assertEqual(str(line), "LINESTRING (12.1 45.6 0,"
                                    "12.3278679043781 45.7587530281451 0,"
                                    "12.5570342682142 45.9170505123658 0,"
                                    "12.7875099444211 46.0748873137703 0,"
                                    "13.0193058218881 46.2322582356215 0)")

    def test_create_great_circular_arc_from_point_azimuth_distance_meters(self):
        s_lon_value = CoordinateValue(12.1, Angle.DEGREES)
        s_lat_value = CoordinateValue(45.6, Angle.DEGREES)
        azimuth = 45.0
        distance_value = DistanceValue(100000.0, Distance.METERS)
        line = Geometry.create_great_circular_arc_from_point_azimuth_distance(
            s_lon_value, s_lat_value, azimuth, distance_value, 5)
        self.assertIsInstance(line, ogr.Geometry)
        self.assertEqual(str(line), "LINESTRING (12.1 45.6 0,"
                                    "12.3278679043781 45.7587530281451 0,"
                                    "12.5570342682142 45.9170505123658 0,"
                                    "12.7875099444211 46.0748873137703 0,"
                                    "13.0193058218881 46.2322582356215 0)")

    def test_create_great_circular_arc_from_point_radians_azimuth_distance(self):
        s_lon_value = CoordinateValue(0.211184839491314, Angle.RADIANS)
        s_lat_value = CoordinateValue(0.795870138909414, Angle.RADIANS)
        azimuth = 45.0
        distance_value = DistanceValue(100.0, Distance.KILOMETERS)
        line = Geometry.create_great_circular_arc_from_point_azimuth_distance(
            s_lon_value, s_lat_value, azimuth, distance_value, 5)
        self.assertIsInstance(line, ogr.Geometry)
        self.assertEqual(str(line), "LINESTRING (12.1 45.6 0,"
                                    "12.3278679043781 45.7587530281451 0,"
                                    "12.5570342682142 45.9170505123658 0,"
                                    "12.7875099444211 46.0748873137703 0,"
                                    "13.0193058218881 46.2322582356215 0)")

    def test_get_progressive_distances(self):
        distance = 100
        distances = Geometry.get_progressive_distances(distance, 5)
        self.assertEqual(5, len(distances))
        self.assertEqual(20, distances[0])
        self.assertEqual(40, distances[1])
        self.assertEqual(60, distances[2])
        self.assertEqual(80, distances[3])
        self.assertEqual(100, distances[4])
