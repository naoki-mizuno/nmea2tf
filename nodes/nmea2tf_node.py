#!/usr/bin/env python2

import rospy
import tf
from nmea_msgs.msg import Sentence
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA

import nmea2tf


rospy.init_node('nmea2tf_node')

nmea_topic = rospy.get_param('~nmea_topic', 'nmea_sentence')
gps_origin_frame = rospy.get_param('~gps_origin_frame', 'gps_origin')
gps_antenna_frame = rospy.get_param('~gps_antenna_frame', 'gps_antenna')
gps_required_quality = rospy.get_param('~gps_required_quality', ['2', '4', '5'])
gps_src_epsg = rospy.get_param('~gps_src_epsg', 4326)
gps_tgt_epsg = rospy.get_param('~gps_tgt_epsg', 32653)
visualize = rospy.get_param('~visualize', False)
marker_phi = rospy.get_param('~marker_phi', 1)
color_arr = rospy.get_param('~marker_color', [0.5059, 0.9569, 0.5216, 1.0])
color = ColorRGBA()
color.r = color_arr[0]
color.g = color_arr[1]
color.b = color_arr[2]
color.a = color_arr[3]

converter = nmea2tf.Converter(gps_src_epsg, gps_tgt_epsg)
tf_b = tf.TransformBroadcaster()
if visualize:
    marker_pub = rospy.Publisher('gps_position', MarkerArray, queue_size=1)


def nmea_cb(msg):
    msg_id, obj = nmea2tf.Parser.parse(msg.sentence)
    if msg_id != 'GPGGA':
        return

    # Data quality not enough
    if obj.quality not in gps_required_quality:
        return

    coord = converter.convert(obj)
    tf_b.sendTransform(coord,
                       [0, 0, 0, 1],
                       msg.header.stamp,
                       gps_antenna_frame,
                       gps_origin_frame)

    if visualize:
        msg.header.frame_id = gps_antenna_frame
        m = nmea2tf.MarkerPublisher.make_marker(color, marker_phi, msg.header)
        marker_pub.publish(m)


nmea_sub = rospy.Subscriber(nmea_topic, Sentence, nmea_cb, queue_size=1)

print('Listening to GGA sentences')
rospy.spin()
