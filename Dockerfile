# Udacity capstone project dockerfile
FROM ros:kinetic-robot
LABEL maintainer="olala7846@gmail.com"

# Install Dataspeed DBW https://goo.gl/KFSYi1 from binary
# adding Dataspeed server to apt
COPY requirements.txt ./requirements.txt
RUN sh -c 'echo "deb [ arch=amd64 ] http://packages.dataspeedinc.com/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-dataspeed-public.list' \
&&  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FF6D3CDA \ 
&&  apt-get update \
&&  sh -c 'echo "yaml http://packages.dataspeedinc.com/ros/ros-public-'$ROS_DISTRO'.yaml '$ROS_DISTRO'" > /etc/ros/rosdep/sources.list.d/30-dataspeed-public-'$ROS_DISTRO'.list' \
&&  rosdep update \
&&  apt-get install -y ros-$ROS_DISTRO-dbw-mkz \
&&  apt-get upgrade -y \
&&  apt-get install -y python-pip \
&&  pip install -r requirements.txt \
&&  apt-get install -y ros-$ROS_DISTRO-cv-bridge \
&&  apt-get install -y ros-$ROS_DISTRO-pcl-ros \
&&  apt-get install -y ros-$ROS_DISTRO-image-proc \
&&  apt-get install -y netbase \
&&  apt-get install -y vim \
&&  rm -rf /var/lib/apt/lists/*

RUN mkdir /capstone
VOLUME ["/capstone"]
VOLUME ["/root/.ros/log/"]
WORKDIR /capstone/ros
