# Following-Bot
Creating a small bot that follows people around and is annoying like Dante following around Virgil in Dante's Commedia.
## 1. Introduction
This is my CSE 400 project where I make a following robot that "speak" Dante's words from his Commedia while it follows someone. The code runs four motors on a chassis system on a raspberry pi 4.
## 2. Hardware Used
- Raspberry Pi 4 Model B
- Webcam
- mini external USB stereo speaker
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
- The motors require more power that the raspberry pi cannot provide so the power module has the 9V battery connected through the battery clip connector on a breadboard. The motor drivers GND and 12V power side are then connected to the 5V and GND of the power module.
- The motors are connected to the motor drivers, two motors per motor driver.
- The GND of the motor driver and of the raspberry pi have to be connected so the motor driver has one wire which is connected to the power module GND and then another wire from the motor driver GND to the raspberry pi GND.
- Then the motors are connected to the raspberry pi. The connections I made were purely from the IN1m and IN4 pins without the need for controlling the speed of the motors. Each motor had two pins for forward and backwards control but only forwards was used. 
## 4. Software Used
- OpenCV Color Detection through raspberry pi 4
- Motor control through raspberry pi 4
- Espeak through USB speaker on raspberry pi 4
## 5. Software Setup
- Ran the full python code through the raspberry pi 4.
- Did not require any virtual environment.
- Downloaded Espeak, opencv, and other dependencies for code to run.
# 6. Further Notes
- The power module allows for four motors to be powered effectively with little to no major changes to the code. The reason why the backwards function was not implemented into the project had to do with the fact that it required too much power and I had a deadline to meet. This project could be improved with an added power module to seperate the motors and be able to implement backwards pins.
- I learned that weight was only an issue when the 9V battery had been used for some time and could not power all of them with the power to move but only run when lifted. 

