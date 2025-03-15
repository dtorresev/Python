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

global vel
adc_x = 0
adc_y = 0 
value = 0.0

def callback(msg): 
	global value
	value = msg.range
	rospy.loginfo("I heard %f", value)

def joy(info): 
	global adc__x, adc_y
	value = info.data
	str = value.split(",")
	print(str)
	if len(str)==2:
		adc_x_str = (str[0].split(":")[1])
		adc_y_str = (str[1].split(":")[1])
	adc_x = int(adc_x_str)
	adc_y = int(adc_y_str)
	rospy.loginfo("I also heard ADC_X is %i and ADC_Y is %i", adc_x,adc_y)



	#rospy.loginfo("I also heard: %s", value)
		
class SignalReader(object):
	def node_init(self):
		#Inicializar el nodo que publica al tópico de cmd_vel
		rospy.init_node('mueve_tortuga', anonymous=True)
		self.rate = rospy.Rate(10)
		#Publica al tópico cmd_vel mensajes tipo Twist
		self.velocity_publisher=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)		

	def circle(self,vel):
		vel_msg = Twist()
		vel_msg.linear.x= vel
		vel_msg.linear.y=0.0
		vel_msg.linear.z=0.0
		vel_msg.angular.x=0.0
		vel_msg.angular.y=0.0
		vel_msg.angular.z = vel/2
		self.velocity_publisher.publish(vel_msg)

if __name__=='__main__': 
	try:
		viewer = SignalReader()
		viewer.node_init()
		rospy.Subscriber("ultrasound",Range,callback)
		rospy.Subscriber("joystick",String,joy)
		
		while not rospy.is_shutdown():
			if value <= 0.1:
				vel = 0	
			else:
				vel = 1
			print("Value read", value)
			print("Velocity",vel)
			viewer.circle(vel)
			rospy.sleep(1)

	except rospy.ROSInterruptException:pass			
