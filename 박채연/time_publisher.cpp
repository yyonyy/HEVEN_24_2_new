#include <iostream>
#include <ros/ros.h>
#include <std_msgs/Time.h>

int main(int argc, char** argv) {
    ros::init(argc, argv, "time_publisher");
    ros::NodeHandle nh; 
    ros::Publisher pub;

    // ros::Time::init();
    // ros::Time::useSystemTime();

    pub = nh.advertise<std_msgs::Time>("/my_time", 10);

    ros::Rate loop_rate(10);

    std_msgs::Time time_msg;

    while(ros::ok()) {
        time_msg.data = ros::Time::now();

        ROS_INFO("Publishing time...");

        pub.publish(time_msg);

        loop_rate.sleep();
    }
    return 0;
}