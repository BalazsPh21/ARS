import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.conditions import IfCondition

import xacro


def generate_launch_description():
    # Process the URDF file
    ars_description = os.path.join(get_package_share_directory('ars_description'))
    xacro_file = os.path.join(ars_description,'urdf','arc.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    
    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config.toxml(),  'use_sim_time': True}
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    # Setup to launch the simulator and Gazebo world
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments=[('gz_args', [' -r -v 4 empty.sdf'])]
    )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(
        package='ros_gz_sim', 
        executable='create',
        arguments=[
            '-topic', '/robot_description',
            '-name', 'arc',
            '-allow_remapping', 'true'],
        output='screen'
    )

    ackermann_steering_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["ackermann_steering_controller"],
    )

    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
    )

    load_joint_state_broadcaster = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
             'joint_state_broadcaster'],
        output='screen'
    )

    # Bridge
    pkg_project_bringup = get_package_share_directory('ars_bringup')
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': os.path.join(pkg_project_bringup, 'config', 'ros_gz_bridge.yaml')
        }],
        output='screen'
    )

    rviz = Node(
       package='rviz2',
       executable='rviz2',
       arguments=['-d', os.path.join(pkg_project_bringup, 'config', 'ars.rviz')],
       condition=IfCondition(LaunchConfiguration('rviz'))
    )

    # Launch!
    return LaunchDescription([
        gazebo,
        DeclareLaunchArgument('rviz', default_value='true',
                              description='Open RViz.'),
        bridge,
        robot_state_publisher,
        spawn_entity,
        joint_state_broadcaster,
        ackermann_steering_controller,
        rviz
    ])