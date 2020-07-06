from .Config import Config


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
