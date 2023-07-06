import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,True)
