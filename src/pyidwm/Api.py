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

    def geoplc(self, lon_value, lat_value):
        """
        Determine the county code for a given point
        :param lon_value: longitude of the given point
        :param lat_value: latitude of the given point
        :return:
        """
        lon = Angle.CONVERT(lon_value.getValue(), lon_value.getUnit(), Angle.DEGREES)
        lat = Angle.CONVERT(lat_value.getValue(), lat_value.getUnit(), Angle.DEGREES)
        layer = self.__store.get_layer(self.__config.layers["country"]["table"])
        point = ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(lon, lat)
        layer.SetSpatialFilter(point)
        name = None
        for feature in layer:
            name = feature.GetField(self.__config.layers["country"]["field_name"])
            break
        return name

    #def geoalc():
    #    pass