#!/usr/bin/env pythn



###########################################
#This program works as
#
###########################################


###################
# import statements
###################


import rospy
import numpy as np
import math
import tf

from tf.transformations import euler_from_quaternion
from tf.transformations import compose_matrix
from tf.transformations import is_same_transform
from geometry_msgs.msg import Twist,Vector3
from sensor_msgs.msg import JointState
#from urdf_parser_py.urdf import URDF
from pykdl_utils.kdl_parser import kdl_tree_from_urdf_model
from pykdl_utils.kdl_kinematics import KDLKinematics 
from brics_actuator.msg import JointPositions
from brics_actuator.msg import JointValue
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import UInt32
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import LaserScan




class YoubotStateMachine:
	def __init__(self):

# Subscibe for the target location/object from the image processing package.
# We can start with a known location and identify the object from the laser pointer.

	rospy.init_node('node_name')
	rospy.Subscriber("", , self.navigate_youbot)


	
#	self.pub = rospy.Publisher("arm_1/arm_controller/position_command",JointPositions,queue_size=10)

# This method gets the target location and publish it to the navigation package
# topic - move_base_simple/goal and message - geometry_msgs/stamped
# we use the action services in the navigation package to fine tune the location(once we have it)

	def navigate_youbot():
		pass

# Publish the object that need to be picked up to grasping package.
# Once the pick up is successful, publish a message to the navigation pacakge to 
# deliver the object to the designated location. Then drop the object at the 
# desgnated location

	def pickup_object():
		pass

# Question
# after the drop the object at the designated location, where should youbot stay?
# Then wait 


		

def main():

	pass


if __name__ == '__main__':
	main()

