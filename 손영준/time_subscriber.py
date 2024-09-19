#!/usr/bin/env python3

import rospy
from std_msgs.msg import Time

class TimeSubscriber:
    def __init__(self):
        # 시간 정보를 저장할 변수
        self.clock = None
        
        # Subscriber 선언
        rospy.Subscriber('/my_time', Time, self.callback)
        
        # 노드 초기화
        rospy.init_node('time_subscriber', anonymous=True)
        
        # rospy.spin()으로 노드가 종료되지 않도록 유지
        rospy.spin()

    def callback(self, data):
        # 받아온 시간 정보를 self.clock에 저장
        self.clock = data.data
        # 저장된 시간 정보를 로그로 출력
        rospy.loginfo("Received time: %s", self.clock)

if __name__ == '__main__':
    try:
        TimeSubscriber()
    except rospy.ROSInterruptException:
        pass
