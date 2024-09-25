#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tutorial.msg import turtle_path
from math import pow, atan2, sqrt

KV = 1.5
KA = 6
TOLERANCE = 0.1

class TurtleBot:

    def __init__(self):
        rospy.init_node("turtlebot_controller", anonymous=False)
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("/path", turtle_path, self.path_callback)
        rospy.Subscriber("/turtle1/pose", Pose, self.pose_callback)

        self.goal = [5, 5]
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def path_callback(self, data):
        
        self.goal = [data.x, data.y]
        rospy.loginfo(f"New goal received: {self.goal}")

    def pose_callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        return sqrt(pow((goal_pose[0] - self.pose.x), 2) +
                    pow((goal_pose[1] - self.pose.y), 2))

    def linear_vel(self, goal_pose):
        return KV * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose[1] - self.pose.y, goal_pose[0] - self.pose.x)

    def angular_vel(self, goal_pose):
        return KA * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self):
        cmd_vel = Twist()
        
        while not rospy.is_shutdown():
            if self.euclidean_distance(self.goal) > TOLERANCE:
                cmd_vel.linear.x = self.linear_vel(self.goal)
                cmd_vel.angular.z = self.angular_vel(self.goal)
            else:
                cmd_vel.linear.x = 0
                cmd_vel.angular.z = 0
            
            self.pub.publish(cmd_vel)
            self.rate.sleep()

        cmd_vel.linear.x = 0
        cmd_vel.angular.z = 0
        self.pub.publish(cmd_vel)

if __name__ == "__main__":
    turtle1 = TurtleBot()
    turtle1.move2goal()
    rospy.spin()
