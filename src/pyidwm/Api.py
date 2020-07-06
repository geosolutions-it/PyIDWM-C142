# -*- coding: utf-8 -*-
from osgeo import ogr
from .Config import Config
from .helper.Store import Store
from .helper.Geometry import Geometry
from .Units import Angle, Distance, SpatialOperator
from .Singleton import Singleton


@Singleton
class Api:
    """
    Class facade to access in friendly way to the IDWM functionalities
    """

    def __init__(self):
        self.__config = Config()
        self.__store = Store()

    def geoplc(self, lon, lat, angle_mode=None):
        """
        Determine the county code for a given point
        :param lon: longitude of the given point
        :param lat: latitude of the given point
        :param angle_mode: angle unit of the coordinate (radians/degrees)
        :return:
        """
        if angle_mode is None:
            angle_mode = self.__config.angle_mode
        layer = self.__store.get_layer(self.__config.layers["country"]["table"])
        point = ogr.Geometry(ogr.wkbPoint)
        lon = Angle.CONVERT(lon, angle_mode, Angle.DEGREES)
        lat = Angle.CONVERT(lat, angle_mode, Angle.DEGREES)
        point.AddPoint(lon, lat)
        layer.SetSpatialFilter(point)
        name = None
        for feature in layer:
            name = feature.GetField(self.__config.layers["country"]["field_name"])
            break
        return name

    #def geoalc():
    #    pass