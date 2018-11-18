from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

import math


class MarkerPublisher:
    def __init__(self):
        pass

    @staticmethod
    def make_point(color, phi, marker_id, header):
        m = Marker()
        m.header = header
        m.id = marker_id
        m.action = Marker.ADD
        m.type = Marker.CYLINDER
        m.scale.x = phi
        m.scale.y = phi
        m.scale.z = 0.1
        m.color = color
        return m

    @staticmethod
    def circle_points(r, dt):
        points = list()
        theta = 0
        while theta < 2 * math.pi:
            p = Point()
            p.x = r * math.cos(theta)
            p.y = r * math.sin(theta)
            p.z = 0
            points.append(p)
            theta += dt
        return points

    @staticmethod
    def make_circle(color, phi, thickness, marker_id, header):
        m = Marker()
        m.header = header
        m.id = marker_id
        m.action = Marker.ADD
        m.type = Marker.LINE_STRIP
        m.scale.x = thickness
        m.points = MarkerPublisher.circle_points(phi / 2.0, math.pi / 180)
        m.color = color
        [m.colors.append(m.color) for i in range(len(m.points))]
        return m

    @staticmethod
    def make_marker(color, phi, header):
        ma = MarkerArray()
        ma.markers.append(MarkerPublisher.make_point(color, phi * 0.3, 0, header))
        ma.markers.append(MarkerPublisher.make_circle(color, phi, phi * 0.2, 1, header))
        return ma
