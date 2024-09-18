#!/usr/bin/env python3

import rospy
from std_msgs.msg import Time

def time_publisher():
    rospy.init_node('time_publisher', anonymous=True)
    pub = rospy.Publisher('my_time', Time, queue_size=10)
    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        pub.publish(current_time)
        rospy.loginfo("Published time: %i.%i", current_time.secs, current_time.nsecs)
        rate.sleep()

if __name__ == '__main__':
    try:
        time_publisher()
    except rospy.ROSInterruptException:
        pass