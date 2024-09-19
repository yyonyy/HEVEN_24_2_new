#!/usr/bin/env python3

import rospy
from std_msgs.msg import Time

def time_publisher():
    # 노드 초기화
    rospy.init_node('time_publisher', anonymous=True)
    # 퍼블리셔 생성
    pub = rospy.Publisher('/my_time', Time, queue_size=10)
    rate = rospy.Rate(1)  # 1Hz로 퍼블리시

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()  # 현재 ROS 시간 가져오기
        pub.publish(current_time)  # 퍼블리시
        rospy.loginfo("Published time: %i.%i", current_time.secs, current_time.nsecs)
        rate.sleep()  # 주기 유지

if __name__ == '__main__':
    try:
        time_publisher()
    except rospy.ROSInterruptException:
        pass
