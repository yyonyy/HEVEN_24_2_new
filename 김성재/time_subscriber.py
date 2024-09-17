#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

class Time:
    def __init__(self):
        self.clock = 0.0  
        self.subscriber = rospy.Subscriber('my_time', Float64, self.callback)
        self.node = rospy.init_node('time_subscriber', anonymous=True)
        rospy.spin()
        

    def callback(self, data):
        self.clock = data.data
        rospy.loginfo(self.clock)

if __name__ == '__main__':
    time_subscriber = Time()
