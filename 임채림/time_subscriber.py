#!/usr/bin/env python3

import rospy
from std_msgs.msg import Time

class TimeSubscriber:
    def __init__(self):
        self.clock = None
        rospy.init_node('time_subscriber', anonymous=True)
        rospy.Subscriber('my_time', Time, self.callback)

    def callback(self, data):
        self.clock = data
        rospy.loginfo("Received time: %i.%i", self.clock.data.secs, self.clock.data.nsecs)

if __name__ == '__main__':
    time_subscriber = TimeSubscriber()
    rospy.spin()