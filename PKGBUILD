# Script generated with Bloom
pkgdesc="ROS - This package contains configuration for each robot instance (e.g. cob4-X, raw3-X). There is a directory for each robot with configuration about urdf and hardware/device configurations."
url='http://ros.org/wiki/cob_hardware_config'

pkgname='ros-kinetic-cob-hardware-config'
pkgver='0.6.8_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cob-supported-robots'
'ros-kinetic-roslaunch'
'ros-kinetic-rostest'
)

depends=('ros-kinetic-cob-calibration-data'
'ros-kinetic-cob-description'
'ros-kinetic-cob-omni-drive-controller'
'ros-kinetic-diagnostic-aggregator'
'ros-kinetic-joint-state-controller'
'ros-kinetic-joint-trajectory-controller'
'ros-kinetic-position-controllers'
'ros-kinetic-raw-description'
'ros-kinetic-roslaunch'
'ros-kinetic-rostest'
'ros-kinetic-ur-description'
'ros-kinetic-velocity-controllers'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=cob_hardware_config
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_hardware_config $srcdir/cob_hardware_config
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

