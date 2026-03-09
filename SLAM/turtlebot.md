## Install Gazebo Harmonic

Run the following commands in the terminal:

```bash
sudo apt-get update
sudo apt-get install curl lsb-release gnupg

sudo curl https://packages.osrfoundation.org/gazebo.gpg \
  --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) \
signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] \
http://packages.osrfoundation.org/gazebo/ubuntu-stable \
$(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

sudo apt-get update
sudo apt-get install gz-harmonic
```

## Install Cartographer for ROS 2 Jazzy

```bash
sudo apt update
sudo apt install ros-jazzy-cartographer
sudo apt install ros-jazzy-cartographer-ros
```
## Install Navigation2 for ROS 2 Jazzy

```bash
sudo apt update
sudo apt install ros-jazzy-navigation2
sudo apt install ros-jazzy-nav2-bringup
```
## source your ROS 2 Jazzy environment
```bash
source /opt/ros/jazzy/setup.bash
```
## Clone and Build TurtleBot3 Simulations (ROS 2 Jazzy)

```bash
# Create workspace
mkdir -p ~/turtlebot3_ws/src

# Navigate to the src folder of your workspace
cd ~/turtlebot3_ws/src/

# Clone the TurtleBot3 simulations repository (jazzy branch)
git clone -b jazzy https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git

# Go back to workspace root and build with colcon
cd ~/turtlebot3_ws
colcon build 
```
## source your ROS 2 Jazzy environment
```bash
source /opt/ros/jazzy/setup.bash
source install/setup.bash

```
## Launch TurtleBot3 in Gazebo

```bash
# Set your TurtleBot3 model (burger, waffle, or waffle_pi)
export TURTLEBOT3_MODEL=burger

# Launch an empty world in Gazebo with TurtleBot3
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

## Launch teleop in new terminal

```bash
## source your ROS 2 Jazzy environment
source /opt/ros/jazzy/setup.bash
source install/setup.bash

# Set your TurtleBot3 model (burger, waffle, or waffle_pi)
export TURTLEBOT3_MODEL=burger

# Launch an empty world in Gazebo with TurtleBot3
ros2 run turtlebot3_teleop teleop_keyboard
```
## Run TurtleBot3 in Gazebo with Cartographer SLAM

```bash
# Set your TurtleBot3 model (burger, waffle, or waffle_pi)
export TURTLEBOT3_MODEL=burger

# Launch TurtleBot3 in a predefined Gazebo world
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

# Launch Cartographer SLAM for mapping
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```
## Launch teleop in new terminal for mapping

```bash
# Set your TurtleBot3 model (burger, waffle, or waffle_pi)
export TURTLEBOT3_MODEL=burger

# Launch an empty world in Gazebo with TurtleBot3
ros2 run turtlebot3_teleop teleop_keyboard
```
## Save the Map from Navigation2

```bash
# Save the current map to your home directory
ros2 run nav2_map_server map_saver_cli -f ~/map
```
## Run TurtleBot3 in Gazebo with Navigation2

```bash
# Set your TurtleBot3 model (burger, waffle, or waffle_pi)
export TURTLEBOT3_MODEL=burger

# Launch TurtleBot3 in a predefined Gazebo world
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

# Launch Navigation2 with your saved map
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$HOME/map.yaml
```

## Initial Pose Estimation for TurtleBot3 Navigation

Before running Navigation2, you must **initialize the AMCL parameters** with the robot's correct pose on the map. This ensures accurate localization and navigation.

### Steps:

1. **Open RViz2** with your running TurtleBot3 simulation and Navigation2.

2. **Click the `2D Pose Estimate` button** in the RViz2 toolbar.

3. **Set the robot’s initial pose:**
   - Click on the map where the TurtleBot3 is actually located.
   - Drag the **large green arrow** toward the direction the robot is facing.

4. **Refine the pose estimation:**
   - Repeat step 2 and 3 until the **LDS (Laser Distance Sensor) scan data** neatly overlaps the saved map.
   - Move the robot slightly back and forth in the simulation or real world to help AMCL refine the pose.
     ## Teleoperate TurtleBot3 with Keyboard

```bash
# Launch keyboard teleoperation to manually control the robot
ros2 run turtlebot3_teleop teleop_keyboard
```

5. **Verify localization:**
   - The TurtleBot3’s estimated location is displayed with **small green arrows** on the map.
   - Ensure the arrows align with the map features and sensor data before starting Navigation2.

### Notes 🤖

- Accurate **Initial Pose Estimation** is critical for autonomous navigation.  
- The process uses **:contentReference[oaicite:0]{index=0}** to match sensor data with the map.  
- Once the robot is correctly localized, you can safely run Navigation2 for autonomous path planning and obstacle avoidance.
