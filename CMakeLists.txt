cmake_minimum_required(VERSION 2.8.3)
project(nmea2tf)

find_package(catkin REQUIRED)

catkin_package()

catkin_python_setup()

catkin_install_python(PROGRAMS
    nodes/nmea2tf_node.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
