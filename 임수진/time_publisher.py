#!/usr/bin/env python3

import rospy
from std_msgs.msg import Time

def talker():
    pub = rospy.Publisher('/my_time', Time, queue_size=10)
    rospy.init_node('talker_node', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        pub.publish(current_time)
        rospy.loginfo(f"Publishing time.. : {current_time}")
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass