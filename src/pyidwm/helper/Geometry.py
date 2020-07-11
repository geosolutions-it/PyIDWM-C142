# -*- coding: utf-8 -*-
#https://arthur-e.github.io/Wicket/sandbox-gmaps3.html
import math
import pyproj
from osgeo import ogr
from pyproj import Proj
from ..Singleton import Singleton
from ..Config import Config
from ..Units import Angle, Distance, SpatialOperator
from ..Value import AngleValue, DistanceValue
from .Projection import Projection, WGS84_PROJECTION


class Geometry:

    @staticmethod
    def get_segments_count(num_vertices):
        """
        Return the number of segments from the total number of required vertices.
        Even it performs a check about the minumum number of segments (0)
        :param num_vertices:
        :return:
        """
        num_segments = num_vertices - 1
        if num_segments < 0:
            num_segments = 0
        return num_segments

    @staticmethod
    def create_buffer(lonValue, latValue, radiusValue, num_vertices=8):
        """
        Create a circle (approximate by a polygon) from center and radius in WGS84
        :param lonValue: {CoordinateValue} longitude of the center of the circle
        :param latValue: {CoordinateValue} latitude of the center of the circle
        :param radius: {DistanceValue} radius of the circle
        :param num_vertices: number of vertices to approximate the circle with a polygon
        :return:
        """
        radius = Distance.CONVERT(radiusValue.getValue(), radiusValue.getUnit(), Distance.METERS)
        lon = Angle.CONVERT(lonValue.getValue(), lonValue.getUnit(), Angle.DEGREES)
        lat = Angle.CONVERT(latValue.getValue(), latValue.getUnit(), Angle.DEGREES)
        aeqd_projection = Projection.get_aeqd_proj(lon, lat, Angle.DEGREES)
        line = ogr.Geometry(ogr.wkbLinearRing)
        step_radians = 2 * math.pi / num_vertices
        array_x, array_y = [], []
        for i in range(num_vertices):
            angle_radians = i * step_radians
            x = radius * math.sin(angle_radians)
            y = radius * math.cos(angle_radians)
            array_x.append(x)
            array_y.append(y)
        points = pyproj.transform(aeqd_projection, WGS84_PROJECTION, array_x[:], array_y[:])
        for i in range(len(points[0])):
            new_lat, new_lon = points[0][i], points[1][i]
            line.AddPoint(new_lon, new_lat)
        new_lat, new_lon = points[0][0], points[1][0]
        line.AddPoint(new_lon, new_lat)
        polygon = ogr.Geometry(ogr.wkbPolygon)
        polygon.AddGeometry(line)
        return polygon

    @staticmethod
    def create_great_circular_arc(projection, e_x, e_y, num_points=20):
        """
        Create the great circular arc (WGS84) using the provided aeqd projection (from the starting point) and the ending point
        :param projection: aeqd projection starting from the first point (lon,lat) => (0,0)
        :param e_x: x coordinate of the final point in the aeqd projection
        :param e_y: y coordinate of the final point in the aeqd projection
        :param num_points: number of vertices for the output linestring (default is 20)
        :return:
        """
        segments_count = Geometry.get_segments_count(num_points)
        dx = e_x / segments_count
        dy = e_y / segments_count
        line = ogr.Geometry(ogr.wkbLineString)
        array_x, array_y = [], []
        for i in range(segments_count + 1):
            x, y = i * dx, i * dy
            array_x.append(x)
            array_y.append(y)
        points = pyproj.transform(projection, WGS84_PROJECTION, array_x[:], array_y[:])
        for i in range(len(points[0])):
            new_lat, new_lon = points[0][i], points[1][i]
            line.AddPoint(new_lon, new_lat)
        return line

    @staticmethod
    def create_great_circular_arc_from_2_points(s_lon_value, s_lat_value, e_lon_value, e_lat_value, num_points=20):
        """
        Create the great circular arc (WGS84) from 2 points
        :param s_lon_value: longitude of the starting point
        :param s_lat_value: latitude of the starting point
        :param e_lon_value: longitude of the ending point
        :param e_lat_value: latitude of the ending point
        :param num_points: number of vertices for the output linestring (default is 20)
        :return:
        """
        s_lon = Angle.CONVERT(s_lon_value.getValue(), s_lon_value.getUnit(), Angle.DEGREES)
        s_lat = Angle.CONVERT(s_lat_value.getValue(), s_lat_value.getUnit(), Angle.DEGREES)
        e_lon = Angle.CONVERT(e_lon_value.getValue(), e_lon_value.getUnit(), Angle.DEGREES)
        e_lat = Angle.CONVERT(e_lat_value.getValue(), e_lat_value.getUnit(), Angle.DEGREES)
        aeqd_projection = Projection.get_aeqd_proj(s_lon, s_lat, Angle.DEGREES)
        x2, y2 = aeqd_projection(e_lon, e_lat)
        return Geometry.create_great_circular_arc(aeqd_projection, x2, y2, num_points)

    @staticmethod
    def create_great_circular_arc_from_point_azimuth_distance(
            s_lon_value, s_lat_value, azimuth, distance_value, num_points=20):
        """
        Create the great circular arc (WGS84) from the starting point, the azimuthal direction (in degrees)
        and the final distance
        :param s_lon_value: longitude of the starting point
        :param s_lat_value: latitude of the starting point
        :param azimuth: direction of the path in degrees
        (0 is toward north, 90 is toward east, 180 is toward south, 270 is toward west)
        :param distance_value: maximum distance to reach
        :param num_points: number of vertices for the output linestring (default is 20)
        :return:
        """
        s_lon = Angle.CONVERT(s_lon_value.getValue(), s_lon_value.getUnit(), Angle.DEGREES)
        s_lat = Angle.CONVERT(s_lat_value.getValue(), s_lat_value.getUnit(), Angle.DEGREES)
        aeqd_projection = Projection.get_aeqd_proj(s_lon, s_lat, Angle.DEGREES)
        radians = Angle.CONVERT(azimuth, Angle.DEGREES, Angle.RADIANS)
        distance = Distance.CONVERT(distance_value.getValue(), distance_value.getUnit(), Distance.METERS)
        x2 = distance * math.sin(radians)
        y2 = distance * math.cos(radians)
        return Geometry.create_great_circular_arc(aeqd_projection, x2, y2, num_points)

    @staticmethod
    def get_progressive_distances(distance, intervals=10):
        """
        return a list of distances in progression from a minimum step (distance/intervals) to the provided max distance
        :param distance: maximum distance (in meters)
        :param intervals: number of the intervals (default 10)
        :return:
        """
        step = distance / intervals
        distances = []
        for i in range(intervals - 1):
            distances.append((i + 1) * step)
        distances.append(distance)
        return distances

    @staticmethod
    def get_distance(projection, lon_value, lat_value, unit=Distance.METERS):
        """
        Return the distance of a given point from the origin of the given projection
        :param projection: custom aeqd projection
        :param lon_value: longitude value of the point
        :param lat_value: latitude value of the point
        :param unit: unit of measure for the distance
        :return:
        """
        lon = Angle.CONVERT(lon_value.getValue(), lon_value.getUnit(), Angle.DEGREES)
        lat = Angle.CONVERT(lat_value.getValue(), lat_value.getUnit(), Angle.DEGREES)
        x, y = projection(lon, lat)
        distance = Distance.CONVERT(math.sqrt(x*x + y*y), Distance.METERS, unit)
        return DistanceValue(distance, unit)

    @staticmethod
    def explodeToArray(geometry):
        """
        Explode a geometry or a multi geometry to an array of single geometries
        :param geometry: geometry to explode
        :return:
        """
        array = []
        geom_count = geometry.GetGeometryCount()
        if geom_count == 0:
            array.append(geometry)
        else:
            for i in range(geom_count):
                part = geometry.GetGeometryRef(i)
                array.append(part)
        return array
