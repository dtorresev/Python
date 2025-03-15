#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def move():
	rospy.init_node('mueve_tortuga', anonymous=True)
	velocity_publisher=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy. Rate (10); #10Hz
	vel_msg = Twist()
	print("Moving the turtle")
	
	vel_angular = float(input("Give me the angular speed (degree/s) "))
	vel_angular = vel_angular*3.1416/180
	angle = float(input("Give the angle to rotate (degree) "))
	angle = angle*3.1416/180
	clockwise = int(input("Clockwise = 1 / Counterclockwise = 0 ? "))
	if (clockwise==1):
		vel_msg.angular.z=-abs(vel_angular)
		
	else:
		vel_msg.angular.z=abs(vel_angular) 

	vel_msg.linear.x=0.0 
	vel_msg.linear.y=0.0 
	vel_msg.linear.z=0.0 
	vel_msg.angular.x=0.0 
	vel_msg.angular.y=0.0
	while not rospy.is_shutdown(): 
		t0 =rospy.Time.now().to_sec() 
		currentAngle=float(0.0) 
		while(currentAngle<angle): 
			velocity_publisher.publish(vel_msg) 
			t1=rospy.Time.now().to_sec()  
			currentAngle=float(vel_angular*(t1-t0)) 
		vel_msg.angular.z=0.0 
		velocity_publisher.publish(vel_msg) 
		rate.sleep()
if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException:pass
