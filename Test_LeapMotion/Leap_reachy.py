import sys
sys.path.insert(0, "LeapLib/")

import Leap, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

import socket
import random
from random import seed
from random import randint
import time
import json


s = socket.socket()
hostname = "DESKTOP-7691C84"
port = 8080
s.connect((hostname, port))

class SampleListener(Leap.Listener):
    
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    
    def on_init(self, controller):

        # # if your arduino was running on a serial port other than '/dev/ttyACM0/'
        # # declare: a = Arduino(serial_port='/dev/ttyXXXX')
        # self.a = Arduino()
        
        # # sleep to ensure ample time for computer to make serial connection 
        # time.sleep(3)
        
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        
        # Reset servo position when you stop program
        # self.a.servo_write(self.SERVO_PIN,90) 
        # self.a.close()

        print "Exited"

    def on_frame(self, controller):
        # data = [] 
        frame = controller.frame()
           
       
        # print some statistics
        # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
        #         frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

            # Get hands
        for hand in frame.hands:
            matrix = Leap.Matrix()
            handType = "Left hand" if hand.is_left else "Right hand"
            if (handType == "Left hand"):
            # print handType + "Hand Id: " + str(hand.id) + " Palm Pos: " + str(hand.palm_position)
            
                pointable = hand.pointables

                hand_center = hand.palm_position
                
                normal = hand.palm_normal
                arm = hand.arm
                direction = hand.direction
                strength = hand.grab_strength #grip pos minimum -20 maks 69 di unity jika disini 0 sampe 1
                strength = int((strength * 89) - 20)
                pergelangan = arm.wrist_position
                # l_y = int(lengan.yaw * 100)
                # l_p = lengan.pitch
                #normalized_point = interaction_box.normalize_point(hand.palm_position,True)
                #wrist_pitch_r = int(direction.pitch * Leap.RAD_TO_DEG)
                wrist_roll_r  = int(normal.roll * Leap.RAD_TO_DEG)
                normal_yaw = int(normal.yaw)
                forearm_yaw_r = int(direction.yaw * Leap.RAD_TO_DEG)
                elbow = arm.elbow_position
                
                # r.right_arm.wrist_pitch.goal_position = wrist_pitch_r
                # r.right_arm.wrist_roll.goal_position = wrist_roll_r
                # r.right_arm.forearm_yaw.goal_position = forearm_yaw_r
                armdir = int(arm.direction.yaw * Leap.RAD_TO_DEG)
                # wrist_pos_pitch = (lengan.pitch* Leap.RAD_TO_DEG)
                width = arm.width
                displacement = arm.wrist_position - elbow
                length = displacement.magnitude
                #wrist_pos_roll = int(lengan.roll* Leap.RAD_TO_DEG)
                #print "Hand type: " +handType+ " Elbow :" + str(elbow) + " forearm_y "+ str(forearm_yaw_r) + " posisi_palm_y "+str(normal_yaw)
                #print "Hand type: " +handType+ " wrist_y: " +str(l_y) + " wrist_p: " + str(l_p)
                
                # data.append((wrist_pitch_r, wrist_roll_r, forearm_yaw_r))
                # print "Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) + " Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)
                #print(data)

                z = (hand_center.z + 100)
                z = z / 400
                z = z * 100
                # y ====== posisi hand sumbu z (pitch soulder reachy)
                x = hand_center.x + 350
                x = x / 700
                x = x * 100

                y = hand_center.y - 80
                y = y / 420
                y = y * 125

                basis = hand.basis
                x_basis = basis.x_basis
                wrist_roll = x_basis.x * 100
                
                for pointable in hand.pointables:
                    stabilized_position = pointable.stabilized_tip_position
                    hand_y = pointable.hand.direction.yaw
                    hand_y = hand_y * 100
            
                data = json.dumps({"x":hand_y, "y":wrist_roll, "z":forearm_yaw_r, "a":strength, "b":armdir, "c":z, "d":x, "e":y})
                s.send(data.encode())
                
                #print "Arm direction: " + str(arm.direction) + " Wrist Pos: " + str(arm.wrist_position) + " Elbow Pos: " + str(arm.elbow_position)
            
                time.sleep(0.1)
                
                # print "  %s, id %d, x-position: %s" % (handType, hand.id, normalized_point.x )
                # print "  %s, id %d, y-position: %s" % (handType, hand.id, normalized_point.y )
                # print "  %s, id %d, z-position: %s" % (handType, hand.id, normalized_point.z )

            #     # FIXME depending on orientation of servo motor
            #     # if motor is upright, Leap Device will register a 0 degree angle if hand is all the way to the left
            #     XPOS_servo = abs(AZIMUTHAL_LIMIT-normalized_point.x*AZIMUTHAL_LIMIT) 
            #     print " Servo Angle = %d " %(int(XPOS_servo))
                
            #     # write the value to servo on arduino
            #     self.a.servo_write(self.SERVO_PIN,int(XPOS_servo)) # turn LED on

            #     # update the old time
            #     self.oldtime = self.newtime
            # else:
            #     pass # keep advancing in time until 10 millisecond is reached

def main():
    
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()    
    controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()