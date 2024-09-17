#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('my_msg', String, queue_size=10)
	rospy.init_node('talker_node', anonymous=True)
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		current_time = str(rospy.get_time())
		pub.publish(current_time)
		rospy.loginfo(f"Pusblishing time...")
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass