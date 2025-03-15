#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist

def movel(vel,dist,dir):
	vel_msg = Twist()
	if (dir == 0):
		vel_msg.linear.x = vel
	else:
		vel_msg.linear.x = -vel
	vel_msg.linear.y=0.0
	vel_msg.linear.z=0.0
	vel_msg.angular.x=0.0
	vel_msg.angular.y=0.0
	vel_msg.angular.z=0.0
	t0=rospy.Time.now().to_sec()
	distanciaActual=float(0.0)
	while(distanciaActual<dist):
		velocity_publisher.publish(vel_msg)
		t1=rospy.Time.now().to_sec()
		distanciaActual=float(vel*(t1-t0))
	vel_msg.linear.x=0.0
	velocity_publisher.publish(vel_msg)

def turn(vel_angular,angulo,cw):
	vel_msg = Twist()
	angulo = angulo * 3.1416 / 180
	if (cw == 0):
		vel_msg.angular.z = -abs(vel_angular)
	else: 
		vel_msg.angular.z = abs(vel_angular)
	vel_msg.linear.y=0.0
	vel_msg.linear.y=0.0
	vel_msg.linear.z=0.0
	vel_msg.angular.x=0.0
	vel_msg.angular.y=0.0
	t0 =rospy.Time.now().to_sec() 
	currentAngle=float(0.0) 
	while(currentAngle<angulo): 
		velocity_publisher.publish(vel_msg) 
		t1=rospy.Time.now().to_sec()  
		currentAngle=float(vel_angular*(t1-t0)) 
	vel_msg.angular.z=0.0 
	velocity_publisher.publish(vel_msg)

#NO CAMBIAR
if __name__=='__main__': 
	try:
		rospy.init_node('mueve_tortuga', anonymous=True)
		velocity_publisher=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
		rate = rospy.Rate(10)
		print("MOVING")
		for i in range(1,3,1):
			movel(1,4,0)
			turn(2,90,1)
			#rospy.sleep(2)

			movel(1,1,0)
			#rospy.sleep(1)
			turn(2,90,1)
			#rospy.sleep(1)
			movel(1,4,0)
			turn(2,90,0)

			movel(1,1,0)
			turn(2,90,0)

	except rospy.ROSInterruptException:pass