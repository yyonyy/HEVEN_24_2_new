#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('my_time', String, queue_size=10)
    rospy.init_node('talker_node', anonymous=True)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        time_str = f"{current_time.secs}.{current_time.nsecs:09d}"
        msg = String()
        msg.data = time_str
        pub.publish(msg)
        rospy.loginfo("Published time: %s", time_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
