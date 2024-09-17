#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
		rospy.loginfo("%s" %data.data)
   
def listener():
    sub=rospy.Subscriber("my_msg", String, callback)
    rospy.init_node('listener_node', anonymous=True)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass