# -*- coding: utf-8 -*-
from osgeo import ogr
from .Config import Config
from .helper.Store import Store
from .helper.Geometry import Geometry
from .helper.Projection import Projection
from .Units import Angle, Distance, SpatialOperator
from .Value import AngleValue, DistanceValue
from .Singleton import Singleton


@Singleton.decorator
class Api:
    """
    Class facade to access in friendly way to the IDWM functionalities
    """
    def __init__(self):
        self.__config = Config()
        self.__store = Store()

    def geoplc(self, lon_value, lat_value):
        """
        Return the county code for a given point or None if it is on the sea
        :param lon_value: longitude value of the given point
        :param lat_value: latitude value of the given point
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

    def geoalc(self, lon_value, lat_value, max_dist_value, azimuth, iwc=0, max_cros=100, arc_approximation=20):
        """
        calculate the path (geographical map) from a given point on a given azimuth through each country or water
        within a specified distance.
        :param lon_value: longitude value of the starting point
        :param lat_value: latitude value of the starting point
        :param max_dist_value: maximum distance
        :param azimuth: azimuth (in degrees clockwise from North) (0-359)
        :param iwc: determines how the routine shall return results:
                    if IWC=1 : The user is only interested of the land/sea path and doesn't need to know if the
                    land path is over different countries.
                    In the CTYVEK array a land path will be indicated with the code '+++'.
                    if IWC=0 : Full information of the path (countries/sea).
        :param max_cros: MAXCROS influences the dimension of the work space for this subroutine.
                        It should be greater than the expected number of crossings which will depend on the value
                        of IRANGE and the complexity of the map. Experience shows that this value may be up to 110
        :param arc_approximation: number of vertices to approximate the arc with a linestring geometry (default 20)
        :return:
        """
        dist_unit = max_dist_value.getUnit()
        aeqd = Projection.get_aeqd_proj(lon_value.getValue(), lat_value.getValue(), lon_value.getUnit())
        line = Geometry.create_great_circular_arc_from_point_azimuth_distance(
            lon_value, lat_value, azimuth, max_dist_value, arc_approximation)
        layer = self.__store.get_layer(self.__config.layers["country"]["table"])
        field_name = self.__config.layers["country"]["field_name"]
        layer.SetSpatialFilter(line)
        cont = 0
        parts = []
        for feature in layer:
            name = "+++"
            if iwc == 0:
                name = feature.GetField(field_name)
            geom = feature.GetGeometryRef()
            intersection = line.Intersection(geom)

            lines = Geometry.explodeToArray(intersection)
            for i in range(len(lines)):
                first_point = lines[i].GetPoint(0)
                last_point = lines[i].GetPoint(lines[i].GetPointCount() - 1)
                f_lon_value = AngleValue(first_point[0], Angle.DEGREES)
                f_lat_value = AngleValue(first_point[1], Angle.DEGREES)
                l_lon_value = AngleValue(last_point[0], Angle.DEGREES)
                l_lat_value = AngleValue(last_point[1], Angle.DEGREES)
                distance_f = Geometry.get_distance(aeqd, f_lon_value, f_lat_value, dist_unit)
                distance_l = Geometry.get_distance(aeqd, l_lon_value, l_lat_value, dist_unit)
                distance_p = distance_l - distance_f
                parts.append({"name": name, "point": [l_lon_value, l_lat_value],
                              "total_distance": distance_l, "partial_distance": distance_p})
                cont += 1
                if cont == max_cros:
                    break
            line = line.Difference(geom)

        lines = Geometry.explodeToArray(line)
        for i in range(len(lines)):
            first_point = lines[i].GetPoint(0)
            last_point = lines[i].GetPoint(lines[i].GetPointCount()-1)
            f_lon_value = AngleValue(first_point[0], Angle.DEGREES)
            f_lat_value = AngleValue(first_point[1], Angle.DEGREES)
            l_lon_value = AngleValue(last_point[0], Angle.DEGREES)
            l_lat_value = AngleValue(last_point[1], Angle.DEGREES)
            distance_f = Geometry.get_distance(aeqd, f_lon_value, f_lat_value, dist_unit)
            distance_l = Geometry.get_distance(aeqd, l_lon_value, l_lat_value, dist_unit)
            distance_p = distance_l - distance_f
            parts.append({"name": None, "point": [l_lon_value, l_lat_value],
                          "total_distance": distance_l, "partial_distance": distance_p})

        parts.sort(key=lambda x: x["total_distance"].getValue(), reverse=False)
        return parts[0:max_cros]
