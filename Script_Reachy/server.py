import socket
from reachy import parts, Reachy
import json
import time
import zmq
import pika


r = Reachy(
    right_arm=parts.RightArm(io='ws', hand='force_gripper'),
    left_arm=parts.LeftArm(io='ws', hand='force_gripper'),
)
listensocket = socket.socket()
port = 8080
maxConnections = 999
IP = socket.gethostname()

listensocket.bind(('', port))

listensocket.listen(maxConnections)
print ("server started " + IP + " on port "+ str(port))
(clientsocket, address) = listensocket.accept()
print ("New connection made!")

running = True

# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")
try:
    while running:
        
        data = clientsocket.recv(1024)
        data = json.loads(data.decode())
        el_pitch = int(data.get("z"))
        wr_yaw   = int(data.get("x"))
        wr_roll  = int(data.get("y"))
        strength = int(data.get("a"))
        armdir   = int(data.get("b"))
        shoulder_pitch = int(data.get("c"))
        shoulder_roll = int(data.get("d"))
        elbow_pitch = int(data.get("e"))
        
        wr_roll = (55 - wr_roll) 

        r.left_arm.elbow_pitch.goal_position = (110 - elbow_pitch) * -1
        r.left_arm.hand.wrist_roll.goal_position = wr_yaw 
        r.left_arm.hand.forearm_yaw.goal_position = wr_roll
        r.left_arm.hand.gripper.goal_position = 20 - strength 
        r.left_arm.arm_yaw.goal_position = wr_yaw - 10
        r.left_arm.shoulder_pitch.goal_position = shoulder_pitch - 80
        r.left_arm.shoulder_roll.goal_position = 30 + (shoulder_roll * -1)
        
        print("left elbow:" + str(elbow_pitch) + "  left wrist_r: "+ str(wr_roll) + 
        "  Grip_strength: "+ str(strength), " arm_dir: "+ str(armdir), 
        " shoulder_p: "+str(shoulder_pitch)+" shoulder_r: "+str(shoulder_roll) + 
        " wrist_yaw: "+ str(wr_yaw)
        )
        
      
except KeyboardInterrupt:
    pass
    
  