#!/usr/bin/env python3
import rospy
from std_msgs.msg import Time

def time_publisher():
    # ROS 노드 초기화
    rospy.init_node('time_publisher_node', anonymous=True)

    # /my_time 토픽에 Time 메시지 타입으로 퍼블리셔 생성
    pub = rospy.Publisher('/my_time', Time, queue_size=10)

    # 1초에 한 번씩 퍼블리시하도록 설정
    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
        # 현재 ROS 시간을 가져옴
        current_time = rospy.Time.now()

        # 로그 출력
        rospy.loginfo(f"Published time : {current_time}")

        # 현재 시간을 퍼블리시
        pub.publish(current_time)

        # 설정한 주기에 맞게 대기
        rate.sleep()

if __name__ == '__main__':
    try:
        time_publisher()
    except rospy.ROSInterruptException:
        pass
