from .Config import Config
from .Units import Distance


class Value:
    """
    It is a Base Class representing a value with his unit of measure
    """
    def __init__(self, value, unit=None):
        """
        Constructor
        :param value: number of the measure
        :param unit: unit of the measure
        """
        self.__value = value
        self.__unit = unit

    def getValue(self):
        """
        Return the value of the measure
        :return:
        """
        return self.__value

    def getUnit(self):
        """
        Return the unit of the measure
        :return:
        """
        return self.__unit
# ---------------------------------------------------------------------------------------------


class DistanceValue(Value):
    """
    Class representing a value with unit for a distance
    """
    def __init__(self, value, unit=None):
        """
        Constructor
        :param value: value of the distance
        :param unit: unit of the distance [METERS, KILOMETERS]
        """
        if unit is None:
            unit = Config().distance_mode
        Value.__init__(self, value, unit)

    def __add__(self, other):
        """
        Override of the ADD (+) operator
        :param other: instance of the other object to add
        :return:
        """
        value = self.getValue()
        if self.getUnit() == other.getUnit():
            value += other.getValue()
        else:
            value += Distance.CONVERT(other.getValue(), other.getUnit(), self.getUnit())
        return DistanceValue(value, self.getUnit())

    def __sub__(self, other):
        """
        Override of the SUB (-) operator
        :param other: instance of the other object to subtract
        :return:
        """
        value = self.getValue()
        if self.getUnit() == other.getUnit():
            value -= other.getValue()
        else:
            value -= Distance.CONVERT(other.getValue(), other.getUnit(), self.getUnit())
        return DistanceValue(value, self.getUnit())
# ---------------------------------------------------------------------------------------------


class CoordinateValue(Value):
    """
    Class representing a value with unit for a coordinate
    """
    def __init__(self, value, unit=None):
        """
        Constructor
        :param value: value of the geographic coordinate
        :param unit: unit of the angle [DEGREES, RADIANS]
        """
        if unit is None:
            unit = Config().angle_mode
        Value.__init__(self, value, unit)
# ---------------------------------------------------------------------------------------------


class AngleValue(Value):
    """
    Class representing a value with unit for an angle
    """
    def __init__(self, value, unit=None):
        """
        Constructor
        :param value: value of the angle
        :param unit: unit of the angle [DEGREES, RADIANS]
        """
        if unit is None:
            unit = Config().angle_mode
        Value.__init__(self, value, unit)
