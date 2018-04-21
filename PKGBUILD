# Script generated with Bloom
pkgdesc="ROS - This stack holds packages for hardware configuration as well as launch files for starting up the basic layer for operating Care-O-bot."
url='http://ros.org/wiki/cob_robots'

pkgname='ros-kinetic-cob-robots'
pkgver='0.6.8_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-cob-bringup'
'ros-kinetic-cob-default-robot-behavior'
'ros-kinetic-cob-default-robot-config'
'ros-kinetic-cob-hardware-config'
'ros-kinetic-cob-moveit-config'
)

conflicts=()
replaces=()

_dir=cob_robots
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_robots $srcdir/cob_robots
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

