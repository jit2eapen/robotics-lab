# Lab: xArm5 Coordinate Tracking (ROS 2)

** This repository contains a ROS 2 Python script to monitor the real-time position of the xArm5 robot. It listens to the Transform (TF) tree and outputs the coordinates of the robot's end-effector relative to its base.
## 1. Prerequisites

Ensure you have the xarm_ros2 packages installed in your workspace:

    * Workspace Path: ~/dev_ws

    * Robot Model: xArm5

## 2. Setup & Sourcing

Every new terminal opened during this lab must be sourced. Run these commands in every new window:

```bash
source /opt/ros/humble/setup.bash
cd ~/dev_ws
source install/setup.bash
```

## 3. Running the Lab
Step 1: Launch the Simulation (Terminal 1)

Start the fake MoveIt execution environment. This provides the TF data and the RViz visualization tool.

```bash
ros2 launch xarm_moveit_config xarm5_moveit_fake.launch.py add_gripper:=true
```
Step 2: Run the TF Listener (Terminal 2)

In a second sourced terminal, run the tracking script:

```bash
# Navigate to the script folder
python3 tf_listener.py
```
## 4. Usage & Parameters

The script is designed to be simple by default, but can be customized using ROS 2 parameters.
Default Mode (Position Only)

By default, the script only shows the Cartesian coordinates:

Command:
```bash
python3 tf_listener.py
```
    Output: [INFO] x = 0.207, y = 0.000, z = 0.112

Rotation Mode

If you need to see the Quaternion rotation (rx, ry, rz, rw), use the show_rotation parameter:

Command:
```bash
python3 tf_listener.py --ros-args -p show_rotation:=true 
```

    Output: [INFO] x = 0.207, y = 0.000, z = 0.112 | rx = 1.000, ry = 0.000, rz = 0.000, rw = 0.000

## 5. Lab Activity: Moving the Robot

To see the values change in your terminal:

    Go to the RViz window opened by Terminal 1.

    Find the Interactive Marker (the ball with arrows) at the tip of the robot.

    Move Position: Click and drag the Arrows (Red, Green, Blue). Observe the x, y, z values updating in Terminal 2.

    Change Orientation: Click and drag the Rings around the marker. (Note: You must have show_rotation:=true enabled to see these changes in the logs).

## 6. Troubleshooting

    No output? Make sure you have clicked "Motion Planning" -> "Planning" -> "Plan and Execute" in RViz or are actively dragging the interactive markers.

    Permission Denied? Run chmod +x tf_listener.py to give the script execution rights.


    README.md (The text above)

    tf_listener.py (The Python script)
