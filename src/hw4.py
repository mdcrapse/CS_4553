#!/usr/bin/env python3

"""Host script for assignment 4."""







"""
1. Go to start
    1.1 BILL is the dice robot.
    1.2 BILL Picks up Dice.
    1.3 BILL Send Communicate Offset. 
    1.4 DJ Receive Communication Offset.
2. Bill goes to meeting point + offset
    2.1 DJ goes to meeting point minus (90 mm in Y axis) + offset
    2.2 BILL infroms DJ it is done moving
    2.3 DJ infroms Bill it is done moving
    2.4 DJ goes for dap up. 
    2.5 DJ grabs dice
    2.6 DJ inform BILL about grab
3. BILL infers DJ's grab
    3.1 BILL releases dice
    3.2 BILL moves away in y position
    3.3 BILL decides new random position
    3.4 BILL communicates new position to DJ.
    3.5 Repeat step 2 with BILL and DJ swapped. 
4. After done three times
    4.1 BILL puts dice on home positon with 90 degree z axis turn.

"""

#MQTT Channels:
    # Robot Status channel
        # Moving to random
        # Moving to dap up
        # Grabbing
        # Grabbed
    # Position Channel


"""
1) Robot A – Pick up Block from designated
location
2)Robot A – Move to a position above your
table/conveyor belt (at least 40cm above the
table). Randomize your position by +/- 50 cm X,
+/- 50cm Y, +/-30cm Z. (ex: (+3.5, -3, +7) to your
chosen position
3) Robot A – Send your location to Robot B
4) Robot A – Wait for Robot B to signal it has the
block in the gripper
5) Robot A – Release gripper
6) Robot A – Wait for Robot B to signal your new
position, go there
7) Grab block from Robot B
8) Repeat the process 1-7 three times (3 times!)
9) place Block in the same location as #1
10) Rotate block in the Z axis 90 degrees
"""

"""
1) Robot B – Wait for message from Robot A
2)Robot B – Grab the block from Robot A
3)Robot B – Move to a position above your
table/conveyor belt (at least 40cm above the table).
Randomize your position by +/- 30 cm X, +/- 30cm Y,
+/-30cm Z. (ex: (+3.5, -3, +7) to your chosen position
4) Send your location to Robot A
5) Robot B – Wait for Robot A to signal it has the block
in the gripper
6) Robot B – Release gripper
7) Robot B – Wave bye-bye to the block
8) Repeat the process 1-6 as many times as Robot A
wants to.
"""









import time
import sys
sys.path.append('../src')
from robot_controller import robot

DJ_IP = '10.1.1.30'

# POSITIONS
START_LOCATION = [0, 0, 0, 0, 0, 0] # rot position
MEETING_LOCATION = [0, 0, 0, 0, 0, 0] # cart position
SAFE_LOCATION = list(MEETING_LOCATION) # cart position
SAFE_LOCATION[1] -= 90
RANDOM_OFFSET = [500, 500, 30]

# CHANNELS
CHANNEL_DJ_HAS_DICE = 'DJ/has_dice'
CHANNEL_DJ_CURRENT_STAGE = 'DJ/stage'
CHANNEL_DJ_POSITIONED = 'DJ/positioned'

def main():
    """! Main program entry"""

    has_dice = True

    # Create new robot object
    crx10 = robot(drive_path)

    # Set robot speed
    crx10.set_speed(300)

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
