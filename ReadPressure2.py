import spidev
import time
import RPi.GPIO as GPIO
MISOpin = 9
CSpin = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(MISOpin, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(CSpin, GPIO.OUT)
GPIO.output(CSpin,GPIO.LOW)
spi = spidev.SpiDev()			# create spi object
spi.open(0, 0)				# open spi port 0, device (CS) 1
spi.mode = 0b11				# 1,1 - 3 bytes read; 0,0 - 4 bytes read
try:
    while True:
        sdo = GPIO.input(MISOpin)	# SDO/MISO is high whilst converting
  	print sdo
        if ( sdo == 1 ) :
		time.sleep(0.1)
        else :
             resp = spi.readbytes(3)		# read three bytes
             value = 256*resp[0] + resp[1]   # Discard least sig i.e. noise
	     print resp
             print value
             time.sleep(0.1)			# sleep for 0.1 secs
    # end while
except KeyboardInterrupt :
    GPIO.cleanup()
    spi.close()
