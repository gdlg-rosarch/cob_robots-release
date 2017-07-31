Name:           ros-indigo-cob-hardware-config
Version:        0.6.7
Release:        0%{?dist}
Summary:        ROS cob_hardware_config package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_hardware_config
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-calibration-data
Requires:       ros-indigo-cob-description
Requires:       ros-indigo-cob-omni-drive-controller
Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-joint-state-controller
Requires:       ros-indigo-joint-trajectory-controller
Requires:       ros-indigo-position-controllers
Requires:       ros-indigo-raw-description
Requires:       ros-indigo-roslaunch
Requires:       ros-indigo-rostest
Requires:       ros-indigo-schunk-description
Requires:       ros-indigo-ur-description
Requires:       ros-indigo-velocity-controllers
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-supported-robots
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-rostest

%description
This package contains configuration for each robot instance (e.g. cob4-X,
raw3-X). There is a directory for each robot with configuration about urdf and
hardware/device configurations.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jul 31 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Sat Aug 29 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Mon Dec 15 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Thu Aug 28 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.4-0
- Autogenerated by Bloom

