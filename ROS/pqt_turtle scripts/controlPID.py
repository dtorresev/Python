#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

current_pose = Pose()
desired_pose = Pose()
obstacle_pose = Pose()
clearance = 0.5
Kp = 2

def callback(msg):
    global current_pose
    current_pose = msg

def obstacle_callback(msg):
    global obstacle_pose
    obstacle_pose = msg

def init():
    global desired_pose, pub, rate, cmd_vel, linear_velocity
    rospy.init_node('controlPID', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    rospy.Subscriber('/mich/pose', Pose, obstacle_callback)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    print("Introduce la posiciòn final en x,y y una orientaciòn en radianes")
    desired_pose.x = float(input("x: "))
    desired_pose.y = float(input("y: "))
    desired_pose.theta = float(input("phi: "))
    linear_velocity = float(input("vel: "))
    cmd_vel = Twist()
    rate = rospy.Rate(10) 

def obstacle_clearance():
    global obstacle_distance
    obstacle_distance =  ((obstacle_pose.x-current_pose.x)**2 + ( obstacle_pose.y - current_pose.y)**2)**0.5

def controlPID():
    global desired_pose, current_pose, w, error_x, error_y
    error_x = desired_pose.x - current_pose.x
    error_y = desired_pose.y - current_pose.y
    target_theta = math.atan2(error_y,error_x)


    error_theta = target_theta - current_pose.theta
    while error_theta > math.pi:
        error_theta -= 2.0 * math.pi
    while error_theta < -math.pi:
        error_theta += 2.0 * math.pi
    w = Kp * (error_theta)

def main():
    global desired_pose, rate, obstacle_distance
    while not rospy.is_shutdown():
        controlPID()
        obstacle_clearance()
        # Enviar comandos de control a TurtleSim
        cmd_vel.linear.x = linear_velocity
        cmd_vel.angular.z = w
        l = ((error_x)**2 + (error_y)**2)**0.5
        rospy.loginfo(f"w: {w}")
        rospy.loginfo(f"l: {l}")
        rospy.loginfo(f"dis: {obstacle_distance}")
        pub.publish(cmd_vel)

        if obstacle_distance < 0.3 + clearance:
            cmd_vel.linear.x = 0
            cmd_vel.angular.z = 0
            pub.publish(cmd_vel)
            rospy.loginfo("Muèvete obstàculo")
        else:
            continue

        if current_pose.y == desired_pose.y and current_pose.x == desired_pose.x:
            cmd_vel.linear.x = 0
            cmd_vel.angular.z = 0
            pub.publish(cmd_vel)
            rospy.loginfo(f"Posición actual : x = {current_pose.x}, y = {current_pose.y}, phi = {current_pose.theta}")

        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        init()
        main()
    except rospy.ROSInterruptException:
        pass

    