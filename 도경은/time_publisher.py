#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('my_time', String, queue_size=10)
    rospy.init_node('time_publisher', anonymous=True)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        current_time = rospy.get_time()
        pub.publish("%s" % current_time)
        
        # 로그 메시지 형식 수정
        rospy.loginfo(f"Published time : {current_time}")
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
