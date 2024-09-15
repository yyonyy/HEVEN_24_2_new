#!/usr/bin/env python3

import rospy
from std_msgs.msg import Time

class TimeListener:
    def __init__(self):
        rospy.Subscriber("my_time", Time, self.callback)
        rospy.init_node('listener_node', anonymous=True)
        rospy.spin()
    
    def callback(self, data):
        #since data is Time object, data.data.secs
        clock = data.data.secs
        rospy.loginfo("%d" %clock)
        

if __name__ == "__main__":
    try:
        TimeListener()
    except rospy.ROSInterruptException:
        pass