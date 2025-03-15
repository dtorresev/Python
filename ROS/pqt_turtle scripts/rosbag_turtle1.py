#!/usr/bin/env python
#Importar librerías de ROS
import rospy 
#Importar mensajes tipo Twist de geometry_msgs
from geometry_msgs.msg import Twist
import subprocess
import os
twist = Twist()
filename = '/home/student/2024-09-23-15-23-48.bag'

def init():
	global rate
	rospy.init_node('rosbag_move', anonymous=True)
	rate = rospy.Rate(5)


if __name__=='__main__':  
	try:
		init()
		FNULL = open(os.devnull, 'w')
		process1 = subprocess.Popen(['rosbag', 'play', filename], stdout=FNULL, stderr=subprocess.STDOUT)
		while not rospy.is_shutdown():
			rate.sleep()
	except rospy.ROSInterruptException:pass	
	finally:
		FNULL.close()
		process1.terminate()  # Ensure the subprocess is terminated on exit
		
