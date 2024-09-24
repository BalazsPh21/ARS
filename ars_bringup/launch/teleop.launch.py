import os



from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.event_handlers import OnProcessExit

import xacro


def generate_launch_description():

    teleop_twist_keyboard = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        output='screen'
    )

    twist_stamper = Node(
        package='twist_stamper',
        executable='twist_stamper',
        remappings=[
            ('/cmd_vel_in', '/cmd_vel'),
            ('/cmd_vel_out', '/ackermann_steering_controller/reference')
        ]
    )

    # Launch!
    return LaunchDescription([
        teleop_twist_keyboard,
        twist_stamper
    ])