#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int32


# füllstandsensor checken
def level():
    rospy.init_node("level", anonymous=True) 
    rospy.Subscriber("level_sensor", Int32, callback)
    rospy.spin()

#wenn füllstand sensor wert x erreicht, fülle nach ; ist wert y überschritte, fahre zurück
def callback(data):
    rospy.loginfo("Level is %f" + data.data)

    level_sensor = data

    if (level_sensor < 0 and level_sensor > 180 ):
         pass#Command =  0.78
    if (level_sensor > 360 ):
         pass#Command =  -0.78
    else : 
         pass#Command = 0.0


def refill():
    pub = rospy.Publisher('water_maxi_joint1_controller/Command', Float32, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown(): # veröffendliche den Command wert
        refilled = callback#Command
        pub.publish(refilled)
        rate.sleep()


def main():
    level()
    refill()

if __name__=="__main__":
    main()