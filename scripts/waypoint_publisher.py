#!/usr/bin/env python3

import rospy
import time
import tf.transformations

from std_msgs.msg import Empty
from geometry_msgs.msg import PoseWithCovarianceStamped

# wp_id : (x, y)
wp_list = {0 :(3.9, -0.44, 0.0, 0.0, 0.0),
           1 : (5.0, -4.5, 0.0, 0.0, 1.6),
           2 : (-6.3, -3.88, 0.0, 0.0, 1.6),
           3 : (-12.3, -0.25, 0.0, 0.0, 1.6),
           4 : (-9, -0.35, 0.0, 0.0, 3.14)}

def talker():
    pub_wp = rospy.Publisher('my_t3_waypoints', PoseWithCovarianceStamped, queue_size=1)
    pub_path_ready = rospy.Publisher('path_ready', Empty, queue_size=1)

    rospy.init_node('waypoint_publisher', anonymous=True)
    rate = rospy.Rate(10) # hz

    my_wp = PoseWithCovarianceStamped()
    my_wp.header.stamp = rospy.Time.now()
    my_wp.header.frame_id = 'map'

    for i in range(len(wp_list)):
        rospy.loginfo("Waypoint " + str(i))
        quaternion = tf.transformations.quaternion_from_euler(wp_list[i][2], wp_list[i][3], wp_list[i][4])
        my_wp.pose.pose.position.x = wp_list[i][0]
        my_wp.pose.pose.position.y = wp_list[i][1]
        my_wp.pose.pose.orientation.x = quaternion[0]
        my_wp.pose.pose.orientation.y = quaternion[1]
        my_wp.pose.pose.orientation.z = quaternion[2]
        my_wp.pose.pose.orientation.w = quaternion[3]

        while not rospy.is_shutdown():
            connections = pub_wp.get_num_connections()
            if connections > 0:
                pub_wp.publish(my_wp)
                break
            rospy.loginfo("Wait for 'my_t3_waypoints' topic")
            rate.sleep()

        rospy.loginfo("Published waypoint number " + str(i))
        time.sleep(2)

    start_command = Empty()

    while not rospy.is_shutdown():
        connections = pub_path_ready.get_num_connections()
        if connections > 0:
            pub_path_ready.publish(start_command)
            rospy.loginfo("Sent waypoint list execution command")
            break
        rospy.loginfo("Waiting for 'path_ready' topic")
        rate.sleep()

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
