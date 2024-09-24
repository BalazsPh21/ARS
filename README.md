# Autonomous Racing Simulation

## Description

This repository is planned to extend the functionality of a [single Ackermann-steering car simulation](https://github.com/BalazsPh21/ackermann_simulation) by introducing a multi-agent environment where two or more autonomous cars can race against each other. Providing a place for you to develop your own planning, control and other packages.

### Still under heavy developement

# Installation

**System Requirements**
- Ubuntu (tested on 22.04) native with ROS 2 Humble
- Ubuntu (tested on 22.04) with Docker and Dev Containers installed

## Option 1 - Native on Ubuntu 22.04
- 
     ```bash
    sudo apt install ros-humble-ros-ign-bridge
    sudo apt install ros-humble-ign-ros2-control
    sudo apt install ros-humble-ackermann-steering-controller
    ```
- Create a workspace:
    ```bash
    cd $HOME && mkdir -p ars_ws/src
    ```
- Clone the repo into the workspace:
    ```bash
    cd $HOME/ars_ws/src
    git clone https://github.com/BalazsPh21/ARS.git
    ```
- Install dependencies with rosdep:
    ```bash
    source /opt/ros/humble/setup.bash
    cd $HOME/ars_ws
    rosdep install --from-paths src -y --ignore-src
    ```
- Build the workspace:
    ```bash
    cd $HOME/ars_ws
    colcon build
    ```

## Option 2 - Dev Containers
- Create a workspace:
    ```bash
    cd $HOME && mkdir -p ars_ws/src
    ```
- Clone the repo into the workspace:
    ```bash
    cd $HOME/ars_ws/src
    git clone https://github.com/BalazsPh21/ARS.git
    ```
- Open the src folder in vscode:
    ```bash
    cd $HOME/ars_ws/src
    code .
    ```
- Reopen in Container
- Inside the image, build the container:
    ```bash
    colcon build
    ```

# Launching the simulation
```bash
cd $HOME/ars_ws
source /opt/ros/foxy/setup.bash
source install/setup.sh
ros2 launch ars_bringup ars_bringup.launch.py
ros2 run twist_stamper twist_stamper --ros-args -r cmd_vel_in:=cmd_vel -r cmd_vel_out:=/ackermann_steering_controller/reference
ros2 run teleop_twist_keyboard keyboard_teleop_twist_keyboard
```