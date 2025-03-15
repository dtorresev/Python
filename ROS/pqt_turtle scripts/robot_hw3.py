#!/usr/bin/env python
import rospy
import time
import numpy as np
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist, Point
from visualization_msgs.msg import Marker

current_x = 0.0
current_y = 0.0
current_angle = 0.0
cmd_vel_pub = None
dato_valido = False

def punto_callback(msg):
    global next_x, next_y, dato_valido
    next_x = msg.x
    next_y = msg.y
    dato_valido = True

def calculate_angle_and_time(next_x,next_y):
    global current_x,current_y,current_angle

    delta_x = next_x - current_x
    delta_y = next_y - current_y

    target_angle = np.arctan2(delta_y,delta_x)
    angle_diff = target_angle - current_angle

    while angle_diff > np.pi:
        angle_diff -= 2*np.pi
    while angle_diff < -np.pi:
        angle_diff += 2*np.pi
    
    angular_velocity = np.pi/4
    time_to_rotate = abs(angle_diff) / angular_velocity
    print("Angle diff " + str(angle_diff))
    return angular_velocity, time_to_rotate

def rotate_to_point(angular_velocity, time_to_rotate):
    global cmd_vel_pub, current_angle

    cmd_vel = Twist()
    cmd_vel.linear.x = 0.0
    cmd_vel.angular.z = angular_velocity

    start_time = rospy.get_time()
    while ((rospy.get_time() - start_time) < time_to_rotate):
        cmd_vel_pub.publish(cmd_vel)

    cmd_vel.angular.z = 0.0
    cmd_vel_pub.publish(cmd_vel)

# Actualiza el ángulo actual después de la rotación
    current_angle += angular_velocity * time_to_rotate

def calculate_distance_and_time(next_x, next_y, velocity):
    global current_x, current_y
    
    delta_x = next_x - current_x
    delta_y = next_y - current_y
    distance = np.sqrt(delta_x ** 2 + delta_y ** 2)
    time_to_next_point = distance / velocity
    
    return distance, time_to_next_point

def move_linear(vel, duration):
    global cmd_vel_pub
    start_time = rospy.get_time()
    cmd_vel = Twist()
    cmd_vel.linear.x = vel
    cmd_vel.angular.z = 0.0
    while ((rospy.get_time() - start_time) < duration):
        cmd_vel_pub.publish(cmd_vel)
    cmd_vel.linear.x = 0.0
    cmd_vel_pub.publish(cmd_vel)

if __name__ == '__main__':
    
    rospy.init_node('go_to_goal')
    loop_rate = rospy.Rate(10)

cmd_vel_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
puntos_sub = rospy.Subscriber('/coordenada', Point, punto_callback)

rospy.loginfo("Esperando coordenadas desde el tópico /coordenada...")

while (dato_valido == False) and (not rospy.is_shutdown()):
    rospy.sleep(1.0)

try:
    rospy.loginfo("Coordenada: " + str(next_x) + ", " + str(next_y))
    angular_velocity, time_to_rotate = calculate_angle_and_time(next_x, next_y)
    rotate_to_point(angular_velocity, time_to_rotate)
    
    distance, tiempo_para_siguiente_punto = calculate_distance_and_time(next_x, next_y, 0.5)
    move_linear(0.5, tiempo_para_siguiente_punto)
    
    current_x = next_x
    current_y = next_y

except rospy.ROSInterruptException:
    pass
