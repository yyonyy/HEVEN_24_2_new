#!/usr/bin/env python3

import rospy
from std_msgs.msg import Time


class TimeSubscriber:
    def __init__(self):
        self.clock = None
        rospy.init_node('time_subscriber', anonymous=True)
        rospy.Subscriber('/my_time', Time, self.callback)
        rospy.spin()
        
        
    def callback(self, data):
        self.clock = data
        rospy.loginfo(f"Received time: {self.clock}")


if __name__ == '__main__':
    try:
        TimeSubscriber()
    except rospy.ROSInterruptException:
        pass