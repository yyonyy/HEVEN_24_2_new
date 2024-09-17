#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def publish_time():
    rospy.init_node('time_publisher')
    pub = rospy.Publisher('/my_time', Float64, queue_size=10)
    rate = rospy.Rate(1)  

    while not rospy.is_shutdown():
        now = rospy.Time.now()
        rospy.loginfo(f"Published time: {now.secs}.{now.nsecs}")
        pub.publish(now.to_sec())
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_time()
    except rospy.ROSInterruptException:
        pass