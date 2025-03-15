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


class encoder():    

    def __init__(self):
        global rate
        rospy.init_node('odom_listener')
        # Subscribe to left and right ticks topics
        rospy.Subscriber('/odom', Odometry, self.original_odom_callback)

         # Inicializar todos los atributos para evitar errores de atributos no inicializados
        self.linear_velocity_x = 0.0
        self.linear_velocity_y = 0.0
        self.linear_velocity_z = 0.0

        self.angular_velocity_x = 0.0
        self.angular_velocity_y = 0.0
        self.angular_velocity_z = 0.0

        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.orientation_x = 0.0
        self.orientation_y = 0.0
        self.orientation_z = 0.0
        self.orientation_w = 0.0
        
        rate = rospy.Rate(10)  # Publish at 10 Hz
        
    def original_odom_callback(self,msg):
        # Read position attributes
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.z = msg.pose.pose.position.z

        # Read orientation attributes (quaternion)
        self.orientation_x = msg.pose.pose.orientation.x
        self.orientation_y = msg.pose.pose.orientation.y
        self.orientation_z = msg.pose.pose.orientation.z
        self.orientation_w = msg.pose.pose.orientation.w
        
        # Extraer las velocidades lineales
        self.linear_velocity_x = msg.twist.twist.linear.x
        self.linear_velocity_y = msg.twist.twist.linear.y
        self.linear_velocity_z = msg.twist.twist.linear.z
        
        # Extraer las velocidades angulares
        self.angular_velocity_x = msg.twist.twist.angular.x
        self.angular_velocity_y = msg.twist.twist.angular.y
        self.angular_velocity_z = msg.twist.twist.angular.z
        


def main():
    global rate
    rate.sleep()

if __name__ == '__main__':
    try:
        ticks  = encoder()
        ticks.__init__()
        rospy.loginfo("Done initalizing node")
        rospy.loginfo("Publishing odometry messages")
        while not rospy.is_shutdown():
            main()
             # Mostrar las velocities
# Mostrar las velocidades redondeadas a 5 decimales
            rospy.loginfo(f"\nVelocidad lineal:\n\t x: {round(ticks.linear_velocity_x, 5)}, y: {round(ticks.linear_velocity_y, 5)}, z: {round(ticks.linear_velocity_z, 5)}")
            rospy.loginfo(f"\nVelocidad angular:\n\t x: {round(ticks.angular_velocity_x, 5)}, y: {round(ticks.angular_velocity_y, 5)}, z: {round(ticks.angular_velocity_z, 5)}")

            # Mostrar posiciones y orientaciones redondeadas a 5 decimales
            rospy.loginfo(f"\nPosición:\n\t x: {round(ticks.x, 5)}, y: {round(ticks.y, 5)}, z: {round(ticks.z, 5)}")
            rospy.loginfo(f"\nOrientación:\n\t x: {round(ticks.orientation_x, 5)}, y: {round(ticks.orientation_y, 5)}, z: {round(ticks.orientation_z, 5)}, w: {round(ticks.orientation_w, 5)}")
            rospy.sleep(1)
    except rospy.ROSInterruptException:
        pass
