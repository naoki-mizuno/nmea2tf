# nmea2tf

Converts a GGA sentence to TF transformation.


## Dependencies

- [python-gdal](https://pypi.python.org/pypi/GDAL)
- [nmea_msgs](http://wiki.ros.org/nmea_msgs)


## Parameters

- `nmea_topic`: topic name that publishes the NMEA GGA sentence
- `gps_origin_frame`: frame id for the GPS origin
- `gps_antenna_frame`: frame id for the antenna
- `gps_required_quality`: required data quality to publish tf
- `gps_src_epsg`: EPSG of the GGA sentence (should be fine with 4326)
- `gps_tgt_epsg`: target EPSG for projecting llh to xyz (default: 32653; UTM
  Zone 53N)
- `visualize`: whether or not to publish the GPS coordinate as marker
- `marker_phi`: the diameter of the marker's outer circle
- `marker_color`: List of RGBA values of the marker, each in the range [0, 1]


## Subscribed topics

- `nmea_sentence`: listens to the GGA sentence


## Published topics

- `gps_pose`: when `visualize` is enabled, the GPS coordinate visualization


## Published TF transformations

- `gps_origin` to `gps_antenna`


## License

MIT License


## Author

Naoki Mizuno
