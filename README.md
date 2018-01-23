# nmea2tf

Converts a GGA sentence to TF transformation.


## Dependencies

- [python-gdal](https://pypi.python.org/pypi/GDAL)


## Parameters

- `nmea_topic`: topic name that publishes the NMEA GGA sentence
- `gps_origin_frame`: frame id for the GPS origin
- `gps_antenna_frame`: frame id for the antenna
- `gps_required_quality`: required data quality to publish tf
- `gps_src_epsg`: EPSG of the GGA sentence (should be fine with 4326)
- `gps_tgt_epsg`: target EPSG for projecting llh to xyz (default: 32653; UTM
  Zone 53N)


## Subscribed topics

- `nmea_sentence`: listens to the GGA sentence


## Published topics

None


## Published TF transformations

- `gps_origin` to `gps_antenna`


## License

MIT License


## Author

Naoki Mizuno
