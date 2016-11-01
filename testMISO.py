import time
import RPi.GPIO as GPIO
MISOpin = 9
CSpin = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(MISOpin, GPIO.IN)
GPIO.setup(CSpin,GPIO.OUT)
GPIO.output(CSpin, GPIO.HIGH)
#GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.wait_for_edge(23, GPIO.FALLING)
try:
    while True:
        sdo = GPIO.input(MISOpin)	# SDO/MISO is high whilst converting
  	print sdo
    	time.sleep(0.1)			# sleep for 0.1 secs
    # end while
except KeyboardInterrupt :
    GPIO.cleanup()
    exit
