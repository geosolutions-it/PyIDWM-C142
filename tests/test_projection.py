# -*- coding: utf-8 -*-
from unittest import TestCase
from pyidwm.Config import Config
from pyidwm.helper.Projection import *
from pyidwm.Units import *


class ProjectionTest(TestCase):

    def test_get_aeqd_wkt_proj(self):
        Config().angle_mode = Angle.DEGREES
        wkt = Projection.get_aeqd_wkt_proj(12.1, 44.2)
        self.assertEqual(wkt, "+proj=aeqd +lat_0=44.20000000 +lon_0=12.10000000 +x_0=0 +y_0=0 "
                              "+a=6371000 +b=6371000 +units=m +no_defs")

    def test_get_aeqd_wkt_proj_degrees(self):
        wkt = Projection.get_aeqd_wkt_proj(12.1, 44.2, Angle.DEGREES)
        self.assertEqual(wkt, "+proj=aeqd +lat_0=44.20000000 +lon_0=12.10000000 +x_0=0 +y_0=0 "
                              "+a=6371000 +b=6371000 +units=m +no_defs")

    def test_get_aeqd_wkt_proj_radians(self):
        wkt = Projection.get_aeqd_wkt_proj(0.211184839491314, 0.771435529381494, Angle.RADIANS)
        self.assertEqual(wkt,
                         "+proj=aeqd +lat_0=44.20000000 +lon_0=12.10000000 +x_0=0 +y_0=0 "
                         "+a=6371000 +b=6371000 +units=m +no_defs")

    def test_get_aeqd_proj(self):
        Config().angle_mode = Angle.DEGREES
        prj = Projection.get_aeqd_proj(12.1, 44.2)
        self.assertIsInstance(prj, Proj)
        self.assertEqual(prj.crs.srs, "+proj=aeqd +lat_0=44.20000000 +lon_0=12.10000000 +x_0=0 +y_0=0 "
                              "+a=6371000 +b=6371000 +units=m +no_defs +type=crs")

    def test_get_aeqd_wkt_proj_degrees(self):
        prj = Projection.get_aeqd_proj(12.1, 44.2, Angle.DEGREES)
        self.assertIsInstance(prj, Proj)
        self.assertEqual(prj.crs.srs, "+proj=aeqd +lat_0=44.20000000 +lon_0=12.10000000 +x_0=0 +y_0=0 "
                              "+a=6371000 +b=6371000 +units=m +no_defs +type=crs")

    def test_get_aeqd_wkt_proj_radians(self):
        prj = Projection.get_aeqd_proj(0.211184839491314, 0.771435529381494, Angle.RADIANS)
        self.assertIsInstance(prj, Proj)
        self.assertEqual(prj.crs.srs, "+proj=aeqd +lat_0=44.20000000 +lon_0=12.10000000 +x_0=0 +y_0=0 "
                              "+a=6371000 +b=6371000 +units=m +no_defs +type=crs")