#!/usr/bin/env python3

import rospy
from tutorial.msg import turtle_path  # Assuming this message type has x and y fields
from random import randint

class TurtleSim:
    def __init__(self):
        rospy.init_node("path_publisher", anonymous=False)
        self.pub = rospy.Publisher("/path", turtle_path, queue_size=10)
        
        rate = rospy.Rate(0.3)  # Publish at 0.3 Hz
        while not rospy.is_shutdown():
            self.publish_path()
            rate.sleep()

    def publish_path(self):
        goal = turtle_path()
        goal.x = randint(1, 10)  # Random x value
        goal.y = randint(1, 10)  # Random y value
        rospy.loginfo("Publishing path: (%f, %f)", goal.x, goal.y)
        self.pub.publish(goal)

if __name__ == "__main__":
    try:
        TurtleSim()
    except rospy.ROSInterruptException:
        pass
