The purpose of this project is to drive Carla, an autonomous vehicle around a track. The software is implemented with ROS Kinetic on a Ubuntu 16.04 Docker image.

### Docker Installation
[Install Docker](https://docs.docker.com/engine/installation/)

### Usage

1. Clone the project repository
```bash
git clone https://github.com/sketchc89/CarlaAutonomous-P13.git ~/projects/CarlaAutonomous-P13
```

2. Build the docker container
```bash
docker build . -t capstone
```

3. Run the docker file
```bash
docker run -p 4567:4567 \
  --mount type=bind,source=$HOME,target=/capstone \
  --mount type=bind,source=/tmp/log,target=/root/.ros/ \
  --mount type=bind,source=$/projects/CarlaAutonomous-P13,target=/capstone/ros/CarlaAutonomous-P13
  --rm -it \
  capstone
```

4. Install python dependencies
```bash
cd CarlaAutonomous-P13
pip install -r requirements.txt
```

5. Make and run styx
```bash
cd ros
catkin_make
source devel/setup.sh
roslaunch launch/styx.launch
```

4. Run the simulator

Tips for using docker/ros: 
* Start additional shells connected to docker container.
```bash
docker container ls
docker exec -it CONTAINER-ID-HERE bash
```
