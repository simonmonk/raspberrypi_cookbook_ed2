
from Adafruit_MotorHAT import Adafruit_MotorHAT
import time

HAT = Adafruit_MotorHAT
stepper_hat = Adafruit_MotorHAT()

stepper = stepper_hat.getStepper(200, 1) # 200 steps/rev, port 1 (M1, M2)

try:
    while True:
        speed = input("Enter stepper speed (rpm) ")
        stepper.setSpeed(speed)  
        steps_forward = input("Steps forward ")
        stepper.step(steps_forward, HAT.FORWARD,  HAT.SINGLE)
        steps_forward = input("Steps reverse ")
        stepper.step(steps_forward, HAT.BACKWARD,  HAT.SINGLE)

finally:
    print("cleaning up")
    stepper_hat.getMotor(1).run(HAT.RELEASE)