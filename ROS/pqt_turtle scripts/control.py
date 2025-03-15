#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

current_pose = Pose()
desired_pose = Pose()

# Referencias deseadas
K1 = 0.5
K2 = 0.5
q2 = 0.5

def callback(msg):
    global current_pose
    current_pose = msg

def init():
    global desired_pose, pub, rate
    rospy.init_node('control', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    print("Introduce la posiciòn final en x,y y una orientaciòn en radianes")
    desired_pose.x = float(input("x: "))
    desired_pose.y = float(input("y: "))
    desired_pose.theta = float(input("phi: "))
    rate = rospy.Rate(10) 


def main():
    global desired_pose, pub, rate

    while not rospy.is_shutdown():

        #Errores de control
        l = math.sqrt((desired_pose.x - current_pose.x)**2 + (desired_pose.y - current_pose.y)**2)
        zeta = math.atan2((desired_pose.y - current_pose.y), (desired_pose.x - current_pose.x)) - current_pose.theta
        psi = math.atan2((desired_pose.y - current_pose.y), (desired_pose.x - current_pose.x)) - desired_pose.theta

        u = K1 * math.cos(zeta) * l     # Velocidad lineal de entrada
        
        if zeta != 0:
            w = K2 * zeta + (K1 / zeta) * math.cos(zeta) * math.sin(zeta) * (zeta + q2 * psi)  # Velocidad angular de entrada
        else:
            w = 0  # Evitar dividir por cero

        # Enviar comandos de control a TurtleSim
        cmd_vel = Twist()
        cmd_vel.linear.x = u
        cmd_vel.angular.z = w
        pub.publish(cmd_vel)

        if l < 0.1 and abs(desired_pose.theta - current_pose.theta) < 0.1:
            cmd_vel.linear.x = 0
            cmd_vel.angular.z = 0
            pub.publish(cmd_vel)
            rospy.loginfo(f"Posición actual : x = {current_pose.x}, y = {current_pose.y}, phi = {current_pose.theta}")
            break
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        init()
        main()
    except rospy.ROSInterruptException:
        pass