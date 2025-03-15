#!/usr/bin/env python
#Importar librerías de ROS
import rospy 
#Importar mensajes tipo Twist de geometry_msgs
from geometry_msgs.msg import Twist
#Importar mensajes tipo Float32 de std_msgs
from std_msgs.msg import Float32
from std_msgs.msg import String
#Importar mensajes tipo Range de sensor_msgs
from sensor_msgs.msg import Range

vel_x = 0
vel_y = 0
adc_x = 0
adc_y = 0 
value = 0.0
dc_max=700
adc_mid=350
velocity_max=5
velocity = 0


def callback(msg): 
	global value
	value = msg.range
	#rospy.loginfo("Distance: %f", value)

def joy(info): 
	global adc_x
	global adc_y
	value = info.data
	str = value.split(",")
	if len(str)==2:
		adc_x_str = (str[0].split(":")[1])
		adc_y_str = (str[1].split(":")[1])
	adc_x = int(adc_x_str)
	adc_y = int(adc_y_str)
	#rospy.loginfo("I also heard ADC_X is %i and ADC_Y is %i", adc_x,adc_y)
	return adc_x, adc_y

	#rospy.loginfo("I also heard: %s", value)
		
class SignalReader(object):
	def node_init(self):
		#Inicializar el nodo que publica al tópico de cmd_vel
		rospy.init_node('mueve_tortuga', anonymous=True)
		self.rate = rospy.Rate(10)
		#Publica al tópico cmd_vel mensajes tipo Twist
		self.velocity_publisher=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)		

	def circle(self,vel_x,vel_y):
		rospy.loginfo("vel_y: %i Vel_x: %i",vel_y, vel_x)
		vel_msg = Twist()
		vel_msg.linear.x= vel_x
		vel_msg.linear.y=vel_y
		vel_msg.linear.z=0.0
		vel_msg.angular.x=0.0
		vel_msg.angular.y=0.0
		vel_msg.angular.z = 1/2
		self.velocity_publisher.publish(vel_msg)

def adc_to_velocity(adc_value):
	global velocity
	if adc_value < 400 & adc_value > 300:
		velocity = 0
	elif adc_value > 400:
		velocity = (adc_value / 700) * velocity_max
	return velocity

if __name__=='__main__': 
	try:
		viewer = SignalReader()
		viewer.node_init()
		rospy.Subscriber("ultrasound",Range,callback)
		rospy.Subscriber("joystick",String,joy)
		
		while not rospy.is_shutdown():
			
			vel_x = adc_to_velocity(adc_x)
			vel_y = adc_to_velocity(adc_y)

			rospy.loginfo("I also heard vel_x is %i and vel_y is %i", vel_x,vel_y)
			viewer.circle(vel_x,vel_y)
			rospy.sleep(1)

	except rospy.ROSInterruptException:pass			
