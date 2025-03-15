#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist
def move():
	rospy.init_node('mueve_tortuga', anonymous=True)
	velocity_publisher=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel_msg = Twist()
	print("Moving the turtle")
	vel= float(input("Give me the speed "))
	dist = float(input("Give me the distance "))
	isForward = int(input("1= Forward / 0=Backward ?  "))
	if (isForward==0):
		vel_msg.linear.x=-vel
	else: 
		vel_msg.linear.x=vel
	vel_msg.linear.y=0.0
	vel_msg.linear.z=0.0
	vel_msg.angular.x=0.0
	vel_msg.angular.y=0.0
	vel_msg.angular.z=0.0
	while not rospy.is_shutdown():
		t0=rospy.Time.now().to_sec()
		distanciaActual=float(0.0)
		while(distanciaActual<dist):
			velocity_publisher.publish(vel_msg)
			t1=rospy.Time.now().to_sec()
			distanciaActual=float(vel*(t1-t0))
		vel_msg.linear.x=0.0
		velocity_publisher.publish(vel_msg)
		rate.sleep()
		

if __name__=='__main__': 
	try:
		move()	
	except rospy.ROSInterruptException:pass
