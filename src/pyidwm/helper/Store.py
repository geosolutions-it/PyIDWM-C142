# -*- coding: utf-8 -*-
from osgeo import ogr
from ..Singleton import Singleton
from ..Config import Config
from ..Units import Angle, Distance, SpatialOperator


@Singleton
class Store:

    def __init__(self):
        self.__driver = None
        self.__data_source = None
        self.__config = Config()

    def get_driver(self):
        """
        Return the GeoPackage Driver
        :return:
        """
        if self.__driver is None:
            self.__driver = ogr.GetDriverByName('GPKG')
        return self.__driver

    def get_data_source(self):
        """
        Return the data source of the geopackage
        :return:
        """
        if self.__data_source is None:
            driver = self.get_driver()
            self.__data_source = self.get_driver().Open(self.__config.geopackage, 0)
        return self.__data_source

    def get_layer(self, name):
        """
        Return the layer reference from his name
        :param name: name of the layer of interest
        :return:
        """
        source = self.get_data_source()
        return source.GetLayerByName(name)

    #def get_features_in(self, polygon, layer_name, spatial_operator=SpatialOperator.INTERSECTS):
    #    """
    #    Return a list o features of the specified layer in (spatial) relation with the provided polygon
    #    :param polygon: filter mask
    #    :param layer_name: name of the layer of interest
    #    :param spatial_operator: spatial operator of interest (intersects/within)
    #    :return:
    #    """
    #    layer = self.get_layer(layer_name)
    #    layer.SetSpatialFilter(polygon)
    #    features = []
    #    for feature in layer:
    #        features.append(feature)
    #    return features
