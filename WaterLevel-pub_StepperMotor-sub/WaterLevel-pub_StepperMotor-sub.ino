

#include <ros.h>
#include <std_msgs/Int32.h>
#include <std_msgs/Float64.h>
#include <Stepper.h>
Stepper Schrittmotor(2048, 3,4,5,6);
int steps;
int sensorpin = A0;
int sensorval = 0;


ros::NodeHandle  nh;


void messageCb( const std_msgs::Float64& msg){
   Schrittmotor.step(msg.data * 1028 / M_PI);
 }
 

ros::Subscriber<std_msgs::Float64> sub("water_maxi_joint1_controller/command", &messageCb);


std_msgs::Int32 str_msg;
ros::Publisher level_sensor("level_sensor", &str_msg);

char SensorVal = sensorval;

void setup()
{ 
  Schrittmotor.setSpeed(20);
  nh.initNode();
  nh.advertise(level_sensor);
  nh.subscribe(sub);
}

void loop()
{ 
  sensorval = analogRead(sensorpin);
  str_msg.data = sensorval;
  level_sensor.publish( &str_msg );
  nh.spinOnce();
  delay(500);
}
