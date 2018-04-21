# Script generated with Bloom
pkgdesc="ROS - This package provides launch files for operating Care-O-bot."
url='http://ros.org/wiki/cob_bringup'

pkgname='ros-kinetic-cob-bringup'
pkgver='0.6.8_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cob-supported-robots'
'ros-kinetic-roslaunch'
)

depends=('ros-kinetic-canopen-chain-node'
'ros-kinetic-canopen-motor-node'
'ros-kinetic-cob-android-script-server'
'ros-kinetic-cob-base-velocity-smoother'
'ros-kinetic-cob-bms-driver'
'ros-kinetic-cob-calibration-data'
'ros-kinetic-cob-cam3d-throttle'
'ros-kinetic-cob-collision-monitor'
'ros-kinetic-cob-collision-velocity-filter'
'ros-kinetic-cob-command-gui'
'ros-kinetic-cob-control-mode-adapter'
'ros-kinetic-cob-dashboard'
'ros-kinetic-cob-default-env-config'
'ros-kinetic-cob-default-robot-behavior'
'ros-kinetic-cob-default-robot-config'
'ros-kinetic-cob-docker-control'
'ros-kinetic-cob-frame-tracker'
'ros-kinetic-cob-hand-bridge'
'ros-kinetic-cob-hardware-config'
'ros-kinetic-cob-helper-tools'
'ros-kinetic-cob-image-flip'
'ros-kinetic-cob-light'
'ros-kinetic-cob-linear-nav'
'ros-kinetic-cob-mimic'
'ros-kinetic-cob-monitoring'
'ros-kinetic-cob-moveit-config'
'ros-kinetic-cob-obstacle-distance'
'ros-kinetic-cob-omni-drive-controller'
'ros-kinetic-cob-phidget-em-state'
'ros-kinetic-cob-phidget-power-state'
'ros-kinetic-cob-phidgets'
'ros-kinetic-cob-reflector-referencing'
'ros-kinetic-cob-safety-controller'
'ros-kinetic-cob-scan-unifier'
'ros-kinetic-cob-script-server'
'ros-kinetic-cob-sick-lms1xx'
'ros-kinetic-cob-sick-s300'
'ros-kinetic-cob-sound'
'ros-kinetic-cob-teleop'
'ros-kinetic-cob-twist-controller'
'ros-kinetic-cob-voltage-control'
'ros-kinetic-compressed-depth-image-transport'
'ros-kinetic-compressed-image-transport'
'ros-kinetic-controller-manager'
'ros-kinetic-costmap-2d'
'ros-kinetic-diagnostic-aggregator'
'ros-kinetic-image-proc'
'ros-kinetic-joint-state-controller'
'ros-kinetic-joint-state-publisher'
'ros-kinetic-joint-trajectory-controller'
'ros-kinetic-joy'
'ros-kinetic-laser-filters'
'ros-kinetic-nodelet'
'ros-kinetic-openni-launch'
'ros-kinetic-openni2-launch'
'ros-kinetic-position-controllers'
'ros-kinetic-realsense-camera'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-roslaunch'
'ros-kinetic-rosserial-python'
'ros-kinetic-rosserial-server'
'ros-kinetic-rostopic'
'ros-kinetic-rplidar-ros'
'ros-kinetic-rviz'
'ros-kinetic-sick-visionary-t-driver'
'ros-kinetic-spacenav-node'
'ros-kinetic-tf2-ros'
'ros-kinetic-theora-image-transport'
'ros-kinetic-topic-tools'
'ros-kinetic-twist-mux'
'ros-kinetic-ur-driver'
'ros-kinetic-usb-cam'
'ros-kinetic-velocity-controllers'
)

conflicts=()
replaces=()

_dir=cob_bringup
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_bringup $srcdir/cob_bringup
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

