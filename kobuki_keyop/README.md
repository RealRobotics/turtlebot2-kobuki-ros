# Kobuki Key Operation

## Run

```sh
ros2 run kobuki_keyop kobuki_keyop_node
```

Publishing to different topics ((in this case `my_cmd_vel`)).

```sh
ros2 run kobuki_keyop kobuki_keyop_node --ros-args --remap commands/velocity:=my_cmd_vel
```

__NOTE: There is no launch file for this package as the keyboard input is lost when launch files are used.__

## Usage

This node takes keypresses from the keyboard and publishes them as Twist messages.

* Forward/back arrows : linear velocity incr/decr.
* Right/left arrows : angular velocity incr/decr.
* Spacebar : reset linear/angular velocities.
* d : disable motors.
* e : enable motors.
* CTRL-C to quit

## ROS messages

The following topics and messages are used by this driver.

| Type | Topic | Message |
|---|---|---|
| Publisher | `commands/velocity` | [<geometry_msgs/msg/Twist](https://github.com/ros2/common_interfaces/blob/rolling/geometry_msgs/msg/Twist.msg) |
| Publisher | `commands/motor_power` | [kobuki_ros_interfaces/msg/MotorPower](https://github.com/kobuki-base/kobuki_ros_interfaces/blob/devel/msg/MotorPower.msg) |
| Subscriber | `teleop` | [kobuki_ros_interfaces/msg/KeyboardInput](https://github.com/kobuki-base/kobuki_ros_interfaces/blob/devel/msg/KeyboardInput.msg)|

## ROS Parameters

* `linear_vel_step (double, default: 0.1)`
* `linear_vel_max (double, default: 3.4)`
* `angular_vel_step (double, default: 0.02`
* `angular_vel_max (double, default: 1.2`
