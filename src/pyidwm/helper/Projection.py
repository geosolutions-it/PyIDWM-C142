# -*- coding: utf-8 -*-
from pyproj import Proj
from ..Config import Config
from ..Units import *

WGS84_PROJECTION = Proj("epsg:4326")


class Projection:

    @staticmethod
    def get_aeqd_wkt_proj(lon, lat, angle_mode=None):
        """
        What we will need for real great circles in a GIS is something that preserves distances and angles.
        We use an azimuthal equidistant projection which needs to be defined for a custom starting point.
        :param lon: longitude of the starting point
        :param lat: latitude of the starting point
        :param angle_mode: units of the angles (degrees/radians)
        :return:
        """
        if angle_mode is None:
            angle_mode = Config().angle_mode
        lon = Angle.CONVERT(lon, angle_mode, Angle.DEGREES)
        lat = Angle.CONVERT(lat, angle_mode, Angle.DEGREES)
        projection_def = "+proj=aeqd +lat_0=%4.8f +lon_0=%4.8f +x_0=0 +y_0=0 +a=6371000 +b=6371000 +units=m +no_defs" \
                         % (lat, lon)
        return projection_def

    @staticmethod
    def get_aeqd_proj(lon, lat, angle_mode=None):
        """
        What we will need for real great circles in a GIS is something that preserves distances and angles.
        We use an azimuthal equidistant projection which needs to be defined for a custom starting point.
        :param lon: longitude of the starting point
        :param lat: latitude of the starting point
        :param angle_mode: units of the angles (degrees/radians)
        :return:
        """
        projection = Proj(Projection.get_aeqd_wkt_proj(lon, lat, angle_mode))
        return projection
