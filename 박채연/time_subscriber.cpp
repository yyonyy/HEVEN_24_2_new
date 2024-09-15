#include <iostream>
#include <ros/ros.h>
#include <std_msgs/Time.h>

class Time
{
public:
    Time() {
        sub = nh.subscribe("/my_time", 10, &Time::callback, this);
    }
    void callback(const std_msgs::Time::ConstPtr& msg) {
        clock = msg->data.sec;
        ROS_INFO("%d", clock);
    }

private:
    ros::NodeHandle nh;
    ros::Subscriber sub;

    int clock;
};

int main(int argc, char** argv) {
    ros::init(argc, argv, "time_subscriber");

    Time time_subscriber;

    ros::spin();

    return 0;
}
