# Following-Bot
Creating a small bot that follows people around and is annoying like Dante following around Virgil in Dante's Commedia.
## 1. Introduction
This is my CSE 400 project where I make a following robot that "speak" Dante's words from his Commedia while it follows someone. The code runs four motors on a chassis system on a raspberry pi 4. This code uses distance information received through an ultrasonic sensor through an arduino uno connected to the raspberry pi 4.
## 2. Hardware Used
- Raspberry Pi 4 Model B
- Arduino Uno
- Webcam
- mini external USB stereo speaker
- Ultrasonic Sensor HC-SR04
- 2x L298N DC Motor Controller
- 4x DC Motors
- breadboard power module
- 9V battery clip connector with 2.1mm plug
- portable battery
- 9V battery
## 4.Hardware Setup
The Raspberry Pi is the heart and soul of the project. 
- The pi has USB connections by the webcam, arduino uno, and the speaker.
- The portable battery is connected only to the raspberry pi.
- The ultrasonic sensor is connected to the arduino uno.
- The motors require more power that the raspberry pi cannot provide so the power module has the 9V battery connected through the battery clip connector on a breadboard. The motor drivers GND and 12V power side are then connected to the 5V and GND of the power module.
- The motors are connected to the motor drivers, two motors per motor driver.
- The GND of the motor driver and of the raspberry pi have to be connected so the motor driver has one wire which is connected to the power module GND and then another wire from the motor driver GND to the raspberry pi GND.
- Then the motors are connected to the raspberry pi. The connections I made were purely from the IN1, IN2, IN3, and IN4 pins without the need for controlling the speed of the motors. Each motor had two pins for forward and backwards control. 
## 4. Software Used
- OpenCV Color Detection through raspberry pi 4
- arduino ide for distance calculations 
- motor control through raspberry pi 4
## 5. Software Setup


