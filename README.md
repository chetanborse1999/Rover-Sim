# Rover-Sim
This project demonstrates a simulation of a Rocker Bogie suspension on an exploration Rover in GazeboSim.
<p align="center">
  <img alt="GazeboPerspective" src="https://user-images.githubusercontent.com/36150054/191451555-0bf38b26-dbee-4f7f-b0cd-1d239f7cbe61.png" height="400">
</p>

## Requirements:
1. ROS Noetic (1.15.14)
2. Gazebo 11(11.10.2)
3. Python3 (3.8.10)
4. Keyboard-python library (0.13.5)

## About: 
The project simulates a rover that implements a rocker bogie suspension. It is a suspension arrangement commonly used in Exploration Rovers like NASA's Perseverance. The Rover consists of one rocker (refer image) on each side connected to each other by a differential. The differential enables the rockers to turn in the opposite directions to each other. This maximises the surface contact on soft, uneven terrain such as sand and improves traction. The coupling between the rockers ensure that the chassis maintains the average pitch of both rockers. One end of the rocker has a drive wheel while other end has a bogie which has two more drive wheels at its ends.
<p align="center">
  <img src="https://user-images.githubusercontent.com/36150054/191450118-85a45d69-2e55-4c86-8a08-b847959508d7.png" alt="Simplified-Rocker-Bogie">
  <img src="https://user-images.githubusercontent.com/36150054/191450247-00201f16-4efd-4964-bd0a-d9543c86b185.jpg" alt="Curiosity-Rover">
  <img src="https://user-images.githubusercontent.com/36150054/191453933-833a3265-5e90-400a-be15-2656d1566440.png" alt="Gazebo-Model-SideView" height="266">
</p>
<p align="center">Side of Rocker Bogie Suspension - Simplified diagram (left) and Mars Curiosity Rover (Right)<br>Gazebo Model Side View (Bottom)</p><br>

The simulation is performed in Gazebo, an open-sourced Robotics Simulator. The Rover is modelled in Fusion360 and exported as .stl mesh files. A URDF (Unified Robotics Description Format) file is made in which the name, physical properties and orientation of all parts and joints is defined. This file can be visualized in RViz. To further open this in Gazebo, gazebo specific tags are added which define the type of joints and plugin. A plugin is a shared library that can be added to URDF to control certain function. We use 'gazebo_ros_control' plugin to drive our motor joints.

On loading the URDF in a Gazebo environment, we can observe and interact with our model. A python script included in the package reads commands from the keyboard, translates that into commands for the joints so that the rover can be controlled via keyboard. The launching of Gazebo, loading the URDF, loading the plugin and sending values to the motor joint is all managed by ROS, an open-sourced Robotics framework.

<p align="center">
  <img src="https://user-images.githubusercontent.com/36150054/191462023-9565798e-f280-466b-bfae-0957397516c2.gif" alt="Controlling-Gazebo-Model gif">
  <img src="https://user-images.githubusercontent.com/36150054/191477479-7854fb50-5afc-4ec0-a923-abb6941be94e.gif" alt="Chassis-Levelling gif">
</p>
<p align="center">Controlling the Gazebo Rover Model (left) and <br>Portraying chassis maintaining average pitch of both rockers (Right)</p><br>

## Instructions to run:
1. Install all required softwares and libraries. If using older version, certain functions may be deprecated.
2. Create and build ROS workspace (catkin_make). And copy the 'rover_sim' folder to 'src' folder.
3. In the rover_one_sdf.sdf file in the 'urdf' folder, find and replace paths for mesh files (&lt;uri> tags) to correct path to meshes folder in the repository. This has to be done because unlike .urdf, the .sdf file uses absolute paths to locate mesh files.
4. Build the workspace and source the setup.bash file.
5. Launch the 'spawn_robot.launch' file. (roslaunch rover_sim spawn_robot.launch) to launch the simulation.
6. Launch the 'get_keys.py' and 'send_keys.py' in seperate terminals. The 'get_keys.py' requires root.
7. The robot should be loaded in Gazebo. And should respond to 'WASD' commands to move.
