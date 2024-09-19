import rospy
from std_msgs.msg import String

class TimeListener:
    def __init__(self):
        
        self.current_time = None

        
        rospy.init_node('unified_time_listener', anonymous=True)

        
        rospy.Subscriber('/my_time', String, self.time_callback)

        
        rospy.spin()

    
    def time_callback(self, data):
        
        self.current_time = data.data
        
        rospy.loginfo(f"Current Time Received: {self.current_time}")

if __name__ == '__main__':
    try:
        
        TimeListener()
    except rospy.ROSInterruptException:
        pass
