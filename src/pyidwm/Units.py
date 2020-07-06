# -*- coding: utf-8 -*-
import math
from enum import Enum
# ---------------------------------------------------------------------------------


class Angle(Enum):
    """
    Enum for angle units
    """
    RADIANS = 0
    DEGREES = 1

    @staticmethod
    def CONVERT(angle, from_unit=RADIANS, to_unit=DEGREES):
        """
        Convert the value of given angle in a specific unit to another unit
        :param angle: value of the angle
        :param from_unit: original unit
        :param to_unit: destination unit
        :return:
        """
        if from_unit == to_unit:
            return angle
        elif from_unit == Angle.RADIANS and to_unit == Angle.DEGREES:
            return 180.0*angle/math.pi
        elif from_unit == Angle.DEGREES and to_unit == Angle.RADIANS:
            return math.pi*angle/180.0
        return None

    @staticmethod
    def FROM_STRING(value):
        """
        Return a value in the enum from a given string
        :param value: string representing the angle unit
        :return:
        """
        if value.upper() == "RADIANS":
            return Angle.RADIANS
        elif value.upper() == "DEGREES":
            return Angle.DEGREES
        return None
# ---------------------------------------------------------------------------------


class Distance(Enum):
    """
    Enum for distance units
    """
    METERS = 0
    KILOMETERS = 1

    @staticmethod
    def CONVERT(distance, from_unit=KILOMETERS, to_unit=METERS):
        """
        Convert the value of given distance in a specific unit to another unit
        :param distance: value of the distance
        :param from_unit: original unit
        :param to_unit: destination unit
        :return:
        """
        if from_unit == to_unit:
            return distance
        elif from_unit == Distance.KILOMETERS and to_unit == Distance.METERS:
            return 1000.0*distance
        elif from_unit == Distance.METERS and to_unit == Distance.KILOMETERS:
            return distance/1000.0
        return None

    @staticmethod
    def FROM_STRING(value):
        """
        Return a value in the enum from a given string
        :param value: string representing the distance unit
        :return:
        """
        if value.upper() == "METERS":
            return Distance.METERS
        elif value.upper() == "KILOMETERS":
            return Distance.KILOMETERS
        return None
# ---------------------------------------------------------------------------------


class SpatialOperator(Enum):
    """
    Enumerator for supported spatial operators
    """
    INTERSECTS = 0
    WITHIN = 1

    @staticmethod
    def FROM_STRING(value):
        """
        Return a value in the enum from a given string
        :param value: string representing the spatial operator
        :return:
        """
        if value.upper() == "INTERSECTS":
            return SpatialOperator.INTERSECTS
        elif value.upper() == "WITHIN":
            return SpatialOperator.WITHIN
        return None
# ---------------------------------------------------------------------------------

