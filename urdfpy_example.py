"""
https://urdfpy.readthedocs.io/en/latest/examples/index.html

urdfpy is no longer maintained so you have to use 
https://github.com/fishbotics/urchin/

pip install urchin


Arm Kinematic Chains - shoulder to wrist for a total of 6dof

joint_right_arm_1_x8_1_dof_x8 = -math.pi/2
joint_right_arm_1_x8_2_dof_x8 = math.pi/2
joint_right_arm_1_x6_1_dof_x6 = math.pi/3
joint_right_arm_1_x6_2_dof_x6 = math.pi/2
joint_right_arm_1_x4_1_dof_x4 = math.pi/2
joint_right_arm_1_hand_1_x4_1_dof_x4 = math.pi/4

"""

from urchin import URDF

robot = URDF.load(
    "urdf/stompy_tiny/robot.urdf",
    lazy_load_meshes=True, # Don't load meshes for speed
)
for joint in robot.actuated_joints:
    print(joint.name)
    print(f"\t {joint.joint_type}")
    print(f"\t [{joint.limit.lower}, {joint.limit.upper}]")