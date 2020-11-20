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


url = pika.ConnectionParameters('rmq1.pptik.id', 5672, '/', pika.PlainCredentials('tmdgdai','tmdgdai'))
connection = pika.BlockingConnection(url)
channel = connection.channel()

channel.queue_declare(queue='tmdgdai20201', durable=True)
print(' [*] Waiting for messages. To exit press CTRl + C')


def callback(ch, method, properties, body):
    # print(" [x] Received %r" % body.decode())
    data = json.loads(body.decode())
    el_pitch = int(data.get("z"))
    wr_yaw   = int(data.get("x"))
    wr_roll  = int(data.get("y"))
    # strength = int(data.get("a"))
    # armdir   = int(data.get("b"))
    # shoulder_pitch = int(data.get("c"))
    # shoulder_roll = int(data.get("d"))
    # elbow_pitch = int(data.get("e"))
    
    # wr_roll = (55 - wr_roll) 

    # r.left_arm.elbow_pitch.goal_position = (150 - elbow_pitch) * -1
    # r.left_arm.hand.wrist_roll.goal_position = wr_yaw 
    # r.left_arm.hand.forearm_yaw.goal_position = wr_roll
    # r.left_arm.hand.gripper.goal_position = 20 - strength 
    # r.left_arm.arm_yaw.goal_position = wr_yaw - 10
    # r.left_arm.shoulder_pitch.goal_position = shoulder_pitch - 80
    # r.left_arm.shoulder_roll.goal_position = 50  + (shoulder_roll * -1)
    
    print("left elbow:" + str(el_pitch) + "  left wrist_r: "+ str(wr_roll) + 
    "  Grip_strength: "+ str(wr_yaw)
    )
    # print("left elbow:" + str(elbow_pitch) + "  left wrist_r: "+ str(wr_roll) + 
    # "  Grip_strength: "+ str(strength), " arm_dir: "+ str(armdir), 
    # " shoulder_p: "+str(shoulder_pitch)+" shoulder_r: "+str(shoulder_roll) + 
    # " wrist_yaw: "+ str(wr_yaw)
    # )
    
    # time.sleep(body.count(b'.'))
    # print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='tmdgdai20201', on_message_callback=callback)

channel.start_consuming()





try:
    while True:
        
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

        r.left_arm.elbow_pitch.goal_position = (150 - elbow_pitch) * -1
        r.left_arm.hand.wrist_roll.goal_position = wr_yaw 
        r.left_arm.hand.forearm_yaw.goal_position = wr_roll
        r.left_arm.hand.gripper.goal_position = 20 - strength 
        r.left_arm.arm_yaw.goal_position = wr_yaw - 10
        r.left_arm.shoulder_pitch.goal_position = shoulder_pitch - 80
        r.left_arm.shoulder_roll.goal_position = 50  + (shoulder_roll * -1)
        
        print("left elbow:" + str(elbow_pitch) + "  left wrist_r: "+ str(wr_roll) + 
        "  Grip_strength: "+ str(strength), " arm_dir: "+ str(armdir), 
        " shoulder_p: "+str(shoulder_pitch)+" shoulder_r: "+str(shoulder_roll) + 
        " wrist_yaw: "+ str(wr_yaw)
        )
        
      
except KeyboardInterrupt:
    pass
    
  