#!/usr/bin/env python2

import rospy
import tf
from nmea_msgs.msg import Sentence

import nmea2tf


rospy.init_node('nmea2tf_node')

nmea_topic = rospy.get_param('~nmea_topic', 'nmea_sentence')
gps_origin_frame = rospy.get_param('~gps_origin_frame', 'gps_origin')
gps_antenna_frame = rospy.get_param('~gps_antenna_frame', 'gps_antenna')
gps_required_quality = rospy.get_param('~gps_required_quality', ['2', '4', '5'])
gps_src_epsg = rospy.get_param('~gps_src_epsg', 4326)
gps_tgt_epsg = rospy.get_param('~gps_tgt_epsg', 32653)

converter = nmea2tf.Converter(gps_src_epsg, gps_tgt_epsg)
tf_b = tf.TransformBroadcaster()


def nmea_cb(msg):
    msg_id, obj = nmea2tf.Parser.parse(msg.sentence)
    if msg_id != 'GPGGA':
        return

    # Data quality not enough
    if obj.quality not in gps_required_quality:
        return

    tf_b.sendTransform(converter.convert(obj),
                        [0, 0, 0, 1],
                        msg.header.stamp,
                        gps_antenna_frame,
                        gps_origin_frame)


nmea_sub = rospy.Subscriber(nmea_topic, Sentence, nmea_cb, queue_size=1)

print('Listening to GGA sentences')
rospy.spin()
