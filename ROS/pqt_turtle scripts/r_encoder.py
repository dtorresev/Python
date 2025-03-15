#!/usr/bin/env python
#Importar librerías de ROS
import rospy 
#Importar mensajes tipo Twist de geometry_msgs
from geometry_msgs.msg import Twist
#Importar mensajes tipo Float32 de std_msgs
from std_msgs.msg import Int16
from std_msgs.msg import String
#Importar mensajes tipo Range de sensor_msgs
from nav_msgs.msg import Odometry
from math import cos, sin, pi

# Define variables for encoder ticks and wheelbase
left_ticks = 0
right_ticks = 0
wheelbase = 0.4  # Example value, adjust based on your robot

# Define variables for current pose and orientation
current_x = 0.0
current_y = 0.0
current_theta = 0.0

odom = Odometry()

def left_ticks_callback(msg):
    global left_ticks
    left_ticks = msg.data

def right_ticks_callback(msg):
    global right_ticks
    right_ticks = msg.data

def publish_odometry():
    global left_ticks, right_ticks, current_x, current_y, current_theta, odom

    l_revolutions = left_ticks / 280
    left_distance = 2 * pi * 0.065 * l_revolutions
    r_revolutions = right_ticks / 280
    right_distance = 2 * pi * 0.065 * r_revolutions

    # Calculate change in position and orientation
    delta_theta = (right_distance - left_distance) / wheelbase
    delta_x = (left_distance + right_distance) / 2.0 * cos(delta_theta)
    delta_y = (left_distance + right_distance) / 2.0 * sin(delta_theta)

    # Update current pose and orientation
    current_x += delta_x
    current_y += delta_y
    current_theta += delta_theta

    # Create Odometry message
    odom.header.stamp = rospy.Time.now()
    odom.pose.pose.position.x = current_x
    odom.pose.pose.position.y = current_y
    odom.pose.pose.orientation.z = sin(current_theta / 2.0)
    odom.pose.pose.orientation.w = cos(current_theta / 2.0)
    
def main():
    global odom

    rospy.init_node('encoder_to_odometry')

    # Subscribe to left and right ticks topics
    rospy.Subscriber('left_ticks', Int16, left_ticks_callback)
    rospy.Subscriber('right_ticks', Int16, right_ticks_callback)

    # Create Odometry publisher
    odom_pub = rospy.Publisher('odom', Odometry, queue_size=10)

    rate = rospy.Rate(10)  # Publish at 10 Hz

    while not rospy.is_shutdown():
        publish_odometry()
        odom_pub.publish(odom)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

