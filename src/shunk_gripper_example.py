#!/usr/bin/env python3

# Imports
import time
import sys
sys.path.append('../src')
from robot_controller import robot

# Global Constants
drive_path = '10.1.1.31' # Bill

def main():
    """! Main program entry"""

    # Create new robot object
    crx10 = robot(drive_path)

    # Set robot speed
    crx10.set_speed(300)

    p1 = [628.131714,    8.591301, 163.363220, -177.848907,  1.335983, -133.099274]
    p2 = [632.453491,   -1.933844,  58.801567, -179.585831,  0.608375, -135.836243]
    p3 = [627.835571,   -2.741052, 423.763000, -179.585892,  0.608179, -135.836578]
    p4 = [-144.621658, -610.987061, 423.781921, -179.461624,  0.501333, 133.040817]
    p5 = [-152.782013, -609.548950, 247.142181, -179.461426,  0.501426, 133.040710]
    p6 = [-144.621597, -820.365540, 423.781982, -179.461426,  0.501225, 133.040817]
    p7 = [-144.621582, -820.365662, 248.102463, -179.461411,  0.501228, 133.040817]
    p8 = [628.131653,    8.591290, 163.363190, -178.613419, -2.118839, -44.482456]
    p9 = [609.493042,    2.590255,  62.679287, -178.439102, -2.631527, -45.399109]

    # Move to start
    crx10.onRobot_gripper(150, 60)
    time.sleep(1)
    crx10.write_cartesian_position(p1)
    time.sleep(1)

    # Grab dice
    crx10.write_cartesian_position(p2)
    crx10.onRobot_gripper(76, 40)

    # Drop dice on belt
    crx10.write_cartesian_position([p3, p4, p5])
    crx10.onRobot_gripper(150, 60)
    crx10.write_cartesian_position(p4)

    # Reverse belt until dice hits sensor
    crx10.conveyor("reverse")
    while True:
        left = crx10.conveyor_proximity_sensor("left")
        if left:
            crx10.conveyor("forward")
            break
        time.sleep(0.1)

    # Forward belt until dice hits sensor
    while True:
        right = crx10.conveyor_proximity_sensor("right")
        if right:
            crx10.conveyor("stop")
            break
        time.sleep(0.1)

    # Grab dice on belt
    crx10.write_cartesian_position([p6, p7])
    crx10.onRobot_gripper(76, 40)

    # Move to dice start position and rotate 90 degrees
    crx10.write_cartesian_position([p6, p1, p8, p9])

    # Drop dice at start
    crx10.onRobot_gripper(150, 60)
    crx10.write_cartesian_position(p8)

    print("==============================")
    print("END OF PROGRAM")
    print("==============================")

if __name__=="__main__":
    main()
