from reachy import parts, Reachy

r = Reachy(
    right_arm=parts.RightArm(io='ws', hand='force_gripper'),
    left_arm=parts.LeftArm(io='ws', hand='force_gripper'),
)

r.left_arm.shoulder_roll.goal_position = 35
r.left_arm.arm_yaw.goal_position = 90
r.left_arm.elbow_pitch.goal_position = -110
r.left_arm.hand.forearm_yaw.goal_position = 90

for _ in range(3):
    r.left_arm.hand.wrist_roll.goto(goal_position=45, duration=0.5, wait=True)
    r.left_arm.hand.wrist_roll.goto(goal_position=-45, duration=0.5, wait=True)