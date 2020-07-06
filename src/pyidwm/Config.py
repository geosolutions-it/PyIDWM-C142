# -*- coding: utf-8 -*-
import json
from .Singleton import Singleton
from .Units import Angle, Distance


@Singleton
class Config(object):
    """
    This class manage the base configuration for the IDWM library and it implements the singleton pattern
    """
    def __init__(self):
        """
        Constructor of the class
        """
        self.__geopackage = None
        self.__angle_mode = None
        self.__distance_mode = None
        self.__layers = None
        self.reset()

    def reset(self):
        """
        Reste the configuration parameters to the default values
        :return:
        """
        self.__geopackage = None
        self.__angle_mode = Angle.DEGREES
        self.__distance_mode = Distance.KILOMETERS
        self.__layers = {
            "country": {
                "table": "RRCountriesPoly",
                "field_name": "CTRY"
            }
        }

    @property
    def geopackage(self):
        """
        Return the path to the IDWM geopackage
        :return:
        """
        return self.__geopackage

    @geopackage.setter
    def geopackage(self, gpkg):
        """
        Set the path to the IDWM geopackage
        :param gpkg: path to the IDWM geopackage
        :return:
        """
        self.__geopackage = gpkg

    @property
    def layers(self):
        """
        Return a dictionary with information of the used layers from the geopackage
        :return:
        """
        return self.__layers

    @property
    def angle_mode(self):
        """
        Return the angle mode for the library
        :return:
        """
        return self.__angle_mode

    @angle_mode.setter
    def angle_mode(self, mode):
        """
        Set the angle mode (degrees/radians) for the library
        :param mode: angle mode for the library (Angle.DEGREES, Angle.RADIANS)
        :return:
        """
        if isinstance(mode, str):
            self.__angle_mode = Angle.FROM_STRING(mode)
        else:
            self.__angle_mode = mode

    @property
    def distance_mode(self):
        """
        Return the distance mode for the library
        :return:
        """
        return self.__distance_mode

    @distance_mode.setter
    def distance_mode(self, mode):
        """
        Set the distance mode (meters/kilometers) for the library
        :param mode: angle mode for the library (Distance.METERS, Distance.KILOMETERS)
        :return:
        """
        if isinstance(mode, str):
            self.__distance_mode = Distance.FROM_STRING(mode)
        else:
            self.__distance_mode = mode

    @staticmethod
    def FROM_FILE(path):
        """
        Read a JSON configuration file, with the following structure:
        {
            "geopackage": <full path to the geopackage>,
            "angle_mode": "degrees" or "radians",
            "distance_mode": "meters" or "kilometers",
            "layers": {
                "country": {
                    "table": <table name containing the polygons of the countries>,
                    "field_name": <field name containing the country code>
                }
            }
        }
        :param path: path of the json file
        :return:
        """
        config = Config()
        config.reset()
        with open(path, 'r') as f:
            data = json.load(f)
        if "geopackage" in data:
            config.geopackage = data["geopackage"]
        if "angle_mode" in data:
            config.angle_mode = data["angle_mode"]
        if "distance_mode" in data:
            config.distance_mode = data["distance_mode"]
        if "layers" in data:
            config.__layers = data["layers"]
        return config
