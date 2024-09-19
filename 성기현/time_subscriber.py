#!/usr/bin/env python3
import rospy
from std_msgs.msg import Time

class TimeSubscriber:
    def __init__(self):
        # 시간 정보를 저장할 변수 선언
        self.clock = None

        # ROS 노드 초기화
        rospy.init_node('time_subscriber_node', anonymous=True)

        # /my_time 토픽을 구독하는 Subscriber 생성
        rospy.Subscriber('/my_time', Time, self.callback)

        # 콜백 함수로 데이터를 받는 동안 노드를 계속 실행
        rospy.spin()

    # 콜백 함수: 토픽에서 데이터를 받아오는 함수
    def callback(self, data):
        # 받은 데이터를 self.clock에 저장
        self.clock = data
        # 저장된 시간을 로그로 출력
        rospy.loginfo(f"Received time: {self.clock}")

if __name__ == '__main__':
    try:
        # TimeSubscriber 클래스 인스턴스 생성
        TimeSubscriber()
    except rospy.ROSInterruptException:
        pass
