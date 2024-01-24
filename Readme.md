# Simulation for a serving robot using TurtleBot3 in a Gazebo environment

this project is for serving robot in cafe. this project's objective is quickly and safety serving robot.

## envirment

- Ubuntu 20.04 LTS
- ROS noetic

## dependency

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

## run

build
```bash
cd your_workspace
rosdep install -i --from-path src --rosdistro noetic -y --os=ubuntu:focal
catkin build
source devel/setup.sh
```

run
```bash
roslaunch final_project costa_launch_final.launch
```