#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


class Time:
    def __init__(self):
        rospy.init_node("listener_node", anonymous = True)
        self.sub = rospy.Subscriber("my_time", String, self.callback)
        rospy.spin()

    def callback(self, data):
        msg = data
        rospy.loginfo(msg)

if __name__ == "__main__":
    try:
        Time()
    except rospy.ROSInterruptException:
        pass
