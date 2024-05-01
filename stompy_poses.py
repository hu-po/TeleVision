""" stompy poses """

from typing import Dict
import math

# URDF standard pose and in the order of the URDF file
FULL_ZERO_POSE: Dict[str, float] = {
    "joint_right_arm_1_x8_1_dof_x8": 0.0,
    "joint_left_arm_2_x8_1_dof_x8": 0.0,
    "joint_head_1_x4_1_dof_x4": 0.0,
    "joint_torso_1_x8_1_dof_x8": 0.0,
    "joint_right_arm_1_x8_2_dof_x8": 0.0,
    "joint_left_arm_2_x8_2_dof_x8": 0.0,
    "joint_legs_1_x8_1_dof_x8": 0.0,
    "joint_legs_1_x8_2_dof_x8": 0.0,
    "joint_head_1_x4_2_dof_x4": 0.0,
    "joint_right_arm_1_x6_1_dof_x6": 0.0,
    "joint_left_arm_2_x6_1_dof_x6": 0.0,
    "joint_legs_1_right_leg_1_x8_1_dof_x8": 0.0,
    "joint_legs_1_left_leg_1_x8_1_dof_x8": 0.0,
    "joint_right_arm_1_x6_2_dof_x6": 0.0,
    "joint_left_arm_2_x6_2_dof_x6": 0.0,
    "joint_legs_1_right_leg_1_x10_2_dof_x10": 0.0,
    "joint_legs_1_left_leg_1_x10_1_dof_x10": 0.0,
    "joint_legs_1_left_leg_1_knee_revolute": 0.0,
    "joint_legs_1_right_leg_1_knee_revolute": 0.0,
    "joint_right_arm_1_x4_1_dof_x4": 0.0,
    "joint_left_arm_2_x4_1_dof_x4": 0.0,
    "joint_legs_1_right_leg_1_x10_1_dof_x10": 0.0,
    "joint_legs_1_right_leg_1_ankle_revolute": 0.0,
    "joint_legs_1_left_leg_1_x10_2_dof_x10": 0.0,
    "joint_legs_1_left_leg_1_ankle_revolute": 0.0,
    "joint_legs_1_left_leg_1_x6_1_dof_x6": 0.0,
    "joint_legs_1_right_leg_1_x6_1_dof_x6": 0.0,
    "joint_legs_1_left_leg_1_x4_1_dof_x4": 0.0,
    "joint_legs_1_right_leg_1_x4_1_dof_x4": 0.0,
    "joint_right_arm_1_hand_1_x4_1_dof_x4": 0.0,
    "joint_left_arm_2_hand_1_x4_1_dof_x4": 0.0,
    "joint_right_arm_1_hand_1_slider_1": -0.034,
    "joint_right_arm_1_hand_1_slider_2": -0.034,
    "joint_left_arm_2_hand_1_slider_1": -0.034,
    "joint_left_arm_2_hand_1_slider_2": -0.034,
    "joint_right_arm_1_hand_1_x4_2_dof_x4": 0.0,
    "joint_left_arm_2_hand_1_x4_2_dof_x4": 0.0,
}


# right arm kinematic chain, ordered from shoulder to wrist
RIGHT_ARM_READY_TO_MANIP: Dict[str, float] = {
    "joint_right_arm_1_x8_1_dof_x8": math.pi / 2,
    "joint_right_arm_1_x8_2_dof_x8": math.pi / 2,
    "joint_right_arm_1_x6_1_dof_x6": math.pi / 3,
    "joint_right_arm_1_x6_2_dof_x6": math.pi / 2,
    "joint_right_arm_1_x4_1_dof_x4": math.pi / 2,
    "joint_right_arm_1_hand_1_x4_1_dof_x4": -math.pi / 4,
}

# left arm kinematic chain, ordered from shoulder to wrist
LEFT_ARM_READY_TO_MANIP: Dict[str, float] = {
    "joint_left_arm_2_x8_1_dof_x8": -math.pi / 2,
    "joint_left_arm_2_x8_2_dof_x8": -math.pi / 2,
    "joint_left_arm_2_x6_1_dof_x6": -math.pi / 3,
    "joint_left_arm_2_x6_2_dof_x6": -math.pi / 2,
    "joint_left_arm_2_x4_1_dof_x4": -math.pi / 2,
    "joint_left_arm_2_hand_1_x4_1_dof_x4": -math.pi / 4,
}

# head looking forward
HEAD_LOOK_FORWARD: Dict[str, float] = {
    "joint_head_1_x4_2_dof_x4": 0.0,
    "joint_head_1_x4_1_dof_x4": -math.pi/4,
}

# right leg kinematic chain, ordered from hip to ankle
RIGHT_LEG_STAND: Dict[str, float] = {
    "joint_legs_1_x8_1_dof_x8" : -0.52,
    "joint_legs_1_right_leg_1_x8_1_dof_x8": -0.65,
    "joint_legs_1_right_leg_1_x10_2_dof_x10": -0.8,
    "joint_legs_1_right_leg_1_knee_revolute": 0.1,
    "joint_legs_1_right_leg_1_ankle_revolute": 0.0,
    "joint_legs_1_right_leg_1_x4_1_dof_x4": 0.0,
}

# left leg kinematic chain, ordered from hip to ankle
LEFT_LEG_STAND: Dict[str, float] = {
    "joint_legs_1_x8_2_dof_x8" : 0.52,
    "joint_legs_1_left_leg_1_x8_1_dof_x8": -0.65,
    "joint_legs_1_left_leg_1_x10_1_dof_x10": 0.8,
    "joint_legs_1_left_leg_1_knee_revolute": -0.1,
    "joint_legs_1_left_leg_1_ankle_revolute": 0.0,
    "joint_legs_1_left_leg_1_x4_1_dof_x4": 0.0,
}

# default standing pose
DEFAULT_STANDING_POSE = FULL_ZERO_POSE.copy()
DEFAULT_STANDING_POSE.update(RIGHT_LEG_STAND)
DEFAULT_STANDING_POSE.update(LEFT_LEG_STAND)
DEFAULT_STANDING_POSE.update(HEAD_LOOK_FORWARD)
DEFAULT_STANDING_POSE.update(RIGHT_ARM_READY_TO_MANIP)
DEFAULT_STANDING_POSE.update(LEFT_ARM_READY_TO_MANIP)