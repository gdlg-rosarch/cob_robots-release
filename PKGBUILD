# Script generated with Bloom
pkgdesc="ROS - Default configuration of the different robots supported by the Care-O-bot stacks. Configuration is e.g. preconfigured joint positions."
url='http://ros.org/wiki/cob_default_robot_config'

pkgname='ros-kinetic-cob-default-robot-config'
pkgver='0.6.8_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cob-supported-robots'
'ros-kinetic-roslaunch'
)

depends=('ros-kinetic-roslaunch'
)

conflicts=()
replaces=()

_dir=cob_default_robot_config
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_default_robot_config $srcdir/cob_default_robot_config
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

