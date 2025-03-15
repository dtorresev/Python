#!/usr/bin/env python
#Importar librerías de ROS
import rospy 
#Importar mensajes tipo Twist de geometry_msgs
from geometry_msgs.msg import Quaternion, Twist, Pose
#Importar mensajes tipo Float32 de std_msgs
from std_msgs.msg import UInt16,Float64
from std_msgs.msg import String
#Importar mensajes tipo Range de sensor_msgs
from nav_msgs.msg import Odometry
from math import cos, sin, pi

left_ticks = 0
right_ticks = 0
wheelbase = 0.4  # Example value, adjust based on your robot

# Define variables for current pose and orientation
current_x = 0.0
current_y = 0.0
current_theta = 0.0
odometry = Odometry()
original_odom = Odometry()
ticks_per_revolution = 600 # Medir empìricamente
wheel_diameter = 0.12 # Magnitude in m ·Circumferencia -> 0.376
wheel_track = 0.4 #2.653 por metro -> 1591.9 pulsos por metro
ticks_per_meter = 1591
th = 0

#Float64 x,y,z

ODOM_POSE_COVARIANCE = [1e-3, 0, 0, 0, 0, 0, 
                        0, 1e-3, 0, 0, 0, 0,
                        0, 0, 1e6, 0, 0, 0,
                        0, 0, 0, 1e6, 0, 0,
                        0, 0, 0, 0, 1e6, 0,
                        0, 0, 0, 0, 0, 1e3]

ODOM_POSE_COVARIANCE2 = [1e-9, 0, 0, 0, 0, 0, 
                         0, 1e-3, 1e-9, 0, 0, 0,
                         0, 0, 1e6, 0, 0, 0,
                         0, 0, 0, 1e6, 0, 0,
                         0, 0, 0, 0, 1e6, 0,
                         0, 0, 0, 0, 0, 1e-9]

ODOM_TWIST_COVARIANCE = [1e-3, 0, 0, 0, 0, 0, 
                         0, 1e-3, 0, 0, 0, 0,
                         0, 0, 1e6, 0, 0, 0,
                         0, 0, 0, 1e6, 0, 0,
                         0, 0, 0, 0, 1e6, 0,
                         0, 0, 0, 0, 0, 1e3]

ODOM_TWIST_COVARIANCE2 = [1e-9, 0, 0, 0, 0, 0, 
                          0, 1e-3, 1e-9, 0, 0, 0,
                          0, 0, 1e6, 0, 0, 0,
                          0, 0, 0, 1e6, 0, 0,
                          0, 0, 0, 0, 1e6, 0,
                          0, 0, 0, 0, 0, 1e-9]

class encoder():
    def left_ticks_callback(self,msg):
        global left_ticks
        self.left_ticks = msg.data
        #rospy.loginfo(f"I heard left: {self.left_ticks}")

    def right_ticks_callback(self,msg):
        global right_ticks
        self.right_ticks = msg.data
        #rospy.loginfo(f"I heard right: {self.right_ticks} ")
    
    def original_odom_callback(self,msg):
        global x,y, original_odom
        self.original_odom= msg.twist.twist.linear.x
        rospy.loginfo(original_odom)

ticks  = encoder()


def publish_odometry():
    global left_ticks, th,right_ticks, current_x, current_y, current_theta, odom

    l_revolutions = left_ticks / ticks_per_revolution
    left_distance = wheel_diameter * pi * l_revolutions
    r_revolutions = right_ticks / ticks_per_revolution
    right_distance = wheel_diameter* pi* r_revolutions


        # Calculate change in position and orientation
    delta_theta = (right_distance - left_distance) / wheelbase
    delta_x = (left_distance + right_distance) / 2.0 * cos(delta_theta)
    delta_y = (left_distance + right_distance) / 2.0 * sin(delta_theta)
    rospy.loginfo(f"dx {delta_x} dy {delta_y} ")

    now = rospy.Time.now()
    dt = now - then
    then = now
    dt = dt.to_sec()    

    dright = prev_right_ticks - right_ticks / ticks_per_meter
    dleft = prev_left_ticks - left_ticks / ticks_per_meter
    prev_right_ticks = right_ticks
    prev_left_ticks = left_ticks

    dxy_ave = (dright + dleft) / 2.0
    dth = (dright - dleft) / wheel_track
    vxy = dxy_ave / dt
    vth = dth / dt
        # Update current pose and orientation
    
    current_x += delta_x
    current_y += delta_y
    current_theta += delta_theta

    if (dxy_ave != 0):
        dx = cos(dth) * dxy_ave
        dy = -sin(dth) * dxy_ave
        x += (cos(th) * dx - sin(th) * dy)
        y += (sin(th) * dx + cos(th) * dy)    

    if (dth != 0):
        th += dth 

        # Create Odometry message
    quaternion = Quaternion()
    quaternion.x = 0.0 
    quaternion.y = 0.0
    quaternion.z = sin(th / 2.0)
    quaternion.w = cos(th / 2.0)
   

    odometry.header.stamp = rospy.Time.now()
    odometry.pose.pose.position.x = current_x
    odometry.pose.pose.position.y = current_y
    odometry.pose.pose.orientation.z = sin(current_theta / 2.0)
    odometry.pose.pose.orientation.w = cos(current_theta / 2.0)
    odometry.pose.pose.orientation = quaternion
    odometry.twist.twist.linear.x = vxy
    odometry.twist.twist.linear.y = 0
    odometry.twist.twist.angular.z = vth
    odometry.pose.covariance = ODOM_POSE_COVARIANCE
    odometry.twist.covariance = ODOM_TWIST_COVARIANCE    

def __init__():
    global odom_pub, rate
    rospy.init_node('encoder_to_odometry')
    # Subscribe to left and right ticks topics
    rospy.Subscriber('/Lencoder', UInt16, ticks.left_ticks_callback)
    rospy.Subscriber('/Rencoder', UInt16, ticks.right_ticks_callback)
    rospy.Subscriber('/odom', Odometry, ticks.original_odom_callback)
    # Create Odometry publisher
    odom_pub = rospy.Publisher('odome', Odometry, queue_size=10)
    rate = rospy.Rate(10)  # Publish at 10 Hz

def main():
    global odometry, odom_pub, rate
    #rospy.loginfo(f"Pos -> x {odometry.pose.pose.position.x} y {odometry.pose.pose.position.y}")
    #rospy.loginfo(f"Ori -> z {odometry.pose.pose.orientation.z} w: {odometry.pose.pose.orientation.w}")
    #odom_pub.publish(odometry)
    rospy.sleep(2)
    rate.sleep()

if __name__ == '__main__':
    try:
        __init__()
        rospy.loginfo("Done initalizing node")
        rospy.loginfo("Publishing odometry messages")
        while not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
