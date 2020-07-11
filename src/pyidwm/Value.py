from .Config import Config
from .Units import Distance


class Value:

    def __init__(self, value, unit=None):
        self.__value = value
        self.__unit = unit

    def getValue(self):
        return self.__value

    def getUnit(self):
        return self.__unit
# ---------------------------------------------------------------------------------------------


class DistanceValue(Value):

    def __init__(self, value, unit=None):
        if unit is None:
            unit = Config().distance_mode
        Value.__init__(self, value, unit)

    def __sub__(self, other):
        value = self.getValue()
        if self.getUnit() == other.getUnit():
            value -= other.getValue()
        else:
            value -= Distance.CONVERT(other.getValue(), other.getUnit, self.getUnit())
        return DistanceValue(value, self.getUnit())
# ---------------------------------------------------------------------------------------------


class CoordinateValue(Value):

    def __init__(self, value, unit=None):
        if unit is None:
            unit = Config().angle_mode
        Value.__init__(self, value, unit)
# ---------------------------------------------------------------------------------------------


class AngleValue(Value):

    def __init__(self, value, unit=None):
        if unit is None:
            unit = Config().angle_mode
        Value.__init__(self, value, unit)
