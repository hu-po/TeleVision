"""
    Cannonical Stompy Poses    
"""

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


# Right Arm kinematic chain, ordered from shoulder to wrist
RIGHT_ARM_READY_TO_MANIP: Dict[str, float] = {
    "joint_right_arm_1_x8_1_dof_x8": math.pi / 2,
    "joint_right_arm_1_x8_2_dof_x8": math.pi / 2,
    "joint_right_arm_1_x6_1_dof_x6": math.pi / 3,
    "joint_right_arm_1_x6_2_dof_x6": math.pi / 2,
    "joint_right_arm_1_x4_1_dof_x4": math.pi / 2,
    "joint_right_arm_1_hand_1_x4_1_dof_x4": -math.pi / 4,
}

# Left Arm kinematic chain, ordered from shoulder to wrist
LEFT_ARM_READY_TO_MANIP: Dict[str, float] = {
    "joint_left_arm_2_x8_1_dof_x8": -math.pi / 2,
    "joint_left_arm_2_x8_2_dof_x8": -math.pi / 2,
    "joint_left_arm_2_x6_1_dof_x6": -math.pi / 3,
    "joint_left_arm_2_x6_2_dof_x6": -math.pi / 2,
    "joint_left_arm_2_x4_1_dof_x4": -math.pi / 2,
    "joint_left_arm_2_hand_1_x4_1_dof_x4": -math.pi / 4,
}

# Head looking forward
HEAD_LOOK_FORWARD: Dict[str, float] = {
    "joint_head_1_x4_2_dof_x4": 0.0,
    "joint_head_1_x4_1_dof_x4": -math.pi/4,
}