import cv2
import numpy as np
import os
import time
import threading
import RPi.GPIO as GPIO
import random

# GPIO Setup

mode=GPIO.getmode()

GPIO.cleanup()
Forward = 26 
Forward2 = 16
Forward3 = 25
Forward4 = 23


GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward3, GPIO.OUT)
GPIO.setup(Forward4, GPIO.OUT)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Forward2, GPIO.OUT)



# Text-to-Speech (async)

def speak_async(text):
    def _speak():
        os.system('espeak "' + text + '" --stdout | aplay 2> /dev/null')
    threading.Thread(target=_speak, daemon=True).start()

# Yellow Color Detection

def detect_yellow_objects(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((20, 20), np.uint8))

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 20:
            x, y, w, h = cv2.boundingRect(contour)
            return (x + w // 2, y + h // 2)
    return None

# Motor Logic

def move_forward():
    GPIO.output(Forward3, GPIO.HIGH)
    GPIO.output(Forward4, GPIO.HIGH)
    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Forward2, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(1)

def stop_motors():
    GPIO.output(Forward3, GPIO.LOW)
    GPIO.output(Forward4, GPIO.LOW)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Forward2, GPIO.LOW)

def turn_right():
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Forward2, GPIO.HIGH)
    GPIO.output(Forward3, GPIO.HIGH)
    GPIO.output(Forward4, GPIO.LOW)
    print("Moving right")
    time.sleep(0.5)

def turn_left():
    GPIO.output(Forward, GPIO.HIGH)
    GPIO.output(Forward2, GPIO.LOW)
    GPIO.output(Forward3, GPIO.LOW)
    GPIO.output(Forward4, GPIO.HIGH)
    print("Moving left")
    time.sleep(0.5)

# Object-Following Logic

last_spoken_time = 0
speak_delay = 8  # seconds

def follow_yellow_object(object_center, frame_width):
    global last_spoken_time

    if object_center is not None:
        object_x, object_y = object_center
        frame_center_x = frame_width // 2
        print(frame_center_x)
        print(frame_width)
        
        if object_x < frame_center_x - 40:
            turn_left()
        elif object_x > 150:
            turn_right()
        else:
            move_forward()
            current_time = time.time()
            if current_time - last_spoken_time > speak_delay:
                phrases = [
                "In   weeping ,and   in   misery, accursed   spirit, may   you   stay. I   know   you   for   all   your  filth.",
                "Master, where are Phlegethon, and Lethe?, About the one, you're silent, and you say the other ,  is made into a river,   by , this,  rain",
                "Please question him ,  about the things you ,think I need to know.   For I cannot, such pity ,fills my heart.",
                "Master, you who overcome all things ,   all but the obstinate fiends,  who sallied , forth against us , at the threshold of the game",
                "Have mercy on me, whatever you are, whether shade , or living man!",
                "You are my teacher and my author. You are the one from whom alone I took",
                "What does this mean? And that other fire, what does it answer? And who are they who made it?"
                ]
                spoken = random.choice(phrases)
                speak_async(spoken)
                last_spoken_time = current_time


        
    else:
        stop_motors()


# Camera Setup

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize for speed
        #frame = cv2.resize(frame, (320, 240))

        object_center = detect_yellow_objects(frame)
        follow_yellow_object(object_center, frame.shape[1])

        cv2.imshow('Yellow Object Detection', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

except KeyboardInterrupt:
    print("Interrupted.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    stop_motors()
    GPIO.cleanup()
    print("Clean exit.")
