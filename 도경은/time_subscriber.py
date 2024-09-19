#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Time() :
    def __init__(self) :
        self.clock = None
        rospy.init_node('time_subscriber', anonymous=True)
        self.sub = rospy.Subscriber("my_time", String, self.callback)
        rospy.spin()

    def callback(self, data):
        self.clock = data.data 
        rospy.loginfo("%s" % self.clock)


if __name__ == "__main__":
    try:
        Time()  # Time 클래스의 인스턴스 생성
    except rospy.ROSInterruptException:
        pass
