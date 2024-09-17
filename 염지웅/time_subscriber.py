#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class Time:
    def __init__(self):
        
        self.clock = None
        
        rospy.Subscriber('/my_time', String, self.callback)

    def callback(self, data):
       
        self.clock = data.data
       
        rospy.loginfo(f"Received time: {self.clock}")

if __name__ == '__main__':
  
    rospy.init_node('time_subscriber', anonymous=True)
    
    time_instance = Time()
    rospy.spin()