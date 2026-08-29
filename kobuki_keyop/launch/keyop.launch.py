"""
This launch file is based on the ROS 1 launch file that looks like this:

<!--
  Raw keyop configuration for working with the default kobuki launcher (minimal.launch). 
 -->
<launch>
  <node pkg="kobuki_keyop" type="keyop" name="keyop" output="screen">
    <remap from="keyop/motor_power" to="mobile_base/commands/motor_power"/>
    <remap from="keyop/cmd_vel" to="mobile_base/commands/velocity"/>
    <param name="linear_vel_step"  value="0.05" type="double"/>
    <param name="linear_vel_max"   value="1.5"  type="double"/>
    <param name="angular_vel_step" value="0.33" type="double"/>
    <param name="angular_vel_max"  value="6.6"  type="double"/>
    <param name="wait_for_connection_" value="true" type="bool"/>
  </node>
</launch>

"""


from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    kobuki_keyop_node = Node(
        package="kobuki_keyop",
        executable="kobuki_keyop_node",
        output="both",
        # Copied these values from the old XML file.
        remappings=[
            ("/motor_power", "/commands/motor_power"),
            ("/cmd_vel", "/commands/velocity"),
        ],
        parameters=[{
            "linear_vel_step": 0.05,
            "linear_vel_max": 1.5,
            "angular_vel_step": 0.33,
            "angular_vel_max": 6.6,
            "wait_for_connection": True,
        }],
    )

    ld = LaunchDescription()
    ld.add_action(kobuki_keyop_node)
    return ld
