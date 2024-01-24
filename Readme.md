# Serving robot

Simulation for a serving robot using TurtleBot3 in a Gazebo environment

## Introduce
this project is simulation for serving robot in cafe. this project's objective is quickly and safety serving robot.

## Development Period
- 2024.01.22 ~ 2024.01.26

## Member
- 김혜성(zozibush) | [Github](https://github.com/zozibush)
- 류재웅(woong137) | [Github](https://github.com/woong137)
- 박정훈(pjh9712) | [Github](https://github.com/pjh9712)
- 정성인(Jeong0806) | [Github](https://github.com/Jeong0806)

## Development Enviroment
- `Ubuntu 20.04 (LTS)` Navtive
- `ROS noetic`
- IDE: VSCode

## Run
build:
```bash
cd your_workspace
rosdep install -i --from-path src --rosdistro noetic -y --os=ubuntu:focal
catkin build
source devel/setup.sh
```

run:
```bash
roslaunch final_project costa_launch_final.launch
```

## Dependency
- gazebo
- gazebo_plugins
- gazebo_ros
- roscpp
- rospy
- urdf
- xacro
- std_msgs
- geometry_msgs
- move_base_msgs

## Open Source LICENSE
- TurtleBot3

## LICENSE

MIT LICENSE.
