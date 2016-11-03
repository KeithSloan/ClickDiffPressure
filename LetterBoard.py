from datetime import datetime

def initTable() :
   global Table
   Table = [[0 for y in range(5)] for x in range(6)]
   Table [0] [0] = "A for Apple"
   Table [0] [1] = "E for Echo"
   Table [0] [2] = "I for India"
   Table [0] [3] = "O for October"
   Table [0] [4] = "U for Uniform"
   Table [1] [0] = "B for Beta"
   Table [1] [1] = "F for Fox"
   Table [1] [2] = "J for Juno"
   Table [1] [3] = "P for Papa"
   Table [1] [4] = "V for Victor"
   Table [2] [0] = "C for Charle"
   Table [2] [1] = "G for Gary"
   Table [2] [2] = "K for King"
   Table [2] [3] = "Q for Quebec"
   Table [2] [4] = "W for Water"
   Table [3] [0] = "D for Delta"
   Table [3] [1] = "H for Hotel"
   Table [3] [2] = "L for Lima"
   Table [3] [3] = "R for Romeo"
   Table [3] [4] = "X for Xray"
   Table [4] [2] = "M for Mother"
   Table [4] [3] = "S for Seirra"
   Table [4] [4] = "Y for Yankie"
   Table [5] [2] = "N for November"
   Table [5] [3] = "T for Tango"
   Table [5] [4] = "Z for Zulu"

def initLED():
# Slot 2 pins
  global LRpin,LYpin,LGpin,RRpin,RYpin,RGpin
  LRpin = 13
  LYpin = 19
  LGpin = 14
  RRpin = 17
  RYpin = 26
  RGpin = 15
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LRpin, GPIO.OUT)
  GPIO.setup(LYpin, GPIO.OUT)
  GPIO.setup(LGpin, GPIO.OUT)
  GPIO.setup(RRpin, GPIO.OUT)
  GPIO.setup(RYpin, GPIO.OUT)
  GPIO.setup(RGpin, GPIO.OUT)

def indicateVertScan():
    GPIO.output(LGpin,GPIO.HIGH)
    GPIO.output(RGpin,GPIO.HIGH)
    GPIO.output(LRpin,GPIO.LOW)
    GPIO.output(RRpin,GPIO.LOW)
    global mode
    mode = 0

def indicateHorzScan():
    GPIO.output(LRpin,GPIO.HIGH)
    GPIO.output(RRpin,GPIO.HIGH)
    GPIO.output(LGpin,GPIO.LOW)
    GPIO.output(RGpin,GPIO.LOW)
    global mode
    mode = 1

def timemillisecs():
    dt = datetime.now()
    return (dt.second*1000+dt.microsecond/1000 )

import spidev
import time
import sys
from datetime import datetime
import subprocess 
import RPi.GPIO as GPIO
initLED()
spi = spidev.SpiDev()			# create spi object
spi.open(0, 0)				# open spi port 0, device (CS) 1
spi.mode = 0b11				# 1,1 - 3 bytes read; 0,0 - 4 bytes read# State 0 - Low Value
# State 1 - High Value
# State 2 - Low Value looking for timeout
debug = len(sys.argv) 
threshold = 350
timeout = 1500
state = 0
count = 0
initTable()
indicateVertScan()
try:
    while True:
        resp = spi.readbytes(3)		# read three bytes
        if (resp[0] != 255) :		# Is conversion valid
           value = 256*resp[0] + resp[1]   # Discard least sig i.e. noise
           if (debug == 2) :
	      print resp
              print value
           if ( value > threshold ) : 	# Signal is HIGH
              if ( state == 0 ) or (state == 2 ) :
                 t1 = timemillisecs() 
                 print "t1 : "+str(t1)
                 state = 1
		 if ( mode == 0 ) :
    		    GPIO.output(LGpin,GPIO.LOW)
		 else :
    		    GPIO.output(LRpin,GPIO.LOW)

           else :			# Signal is LOW
              if ( state == 1 ) :
                 t2 = timemillisecs()
                 print "t2 : "+str(t2)
		 count += 1
                 state = 2
                 print "Pulse : "+str(t2-t1)
         	 if ( mode == 0 ) :
    		    GPIO.output(LGpin,GPIO.HIGH)
		 else : 
    		    GPIO.output(LRpin,GPIO.HIGH)
	      if ( state == 2 ) :
		 t3 = timemillisecs()
		 if ((t3 - t2) > timeout ) :
		    print "TIME OUT : Count "+str(count)
                    if ( mode == 0 ) :	# End VertScan
			y = count - 1
			indicateHorzScan()
		    else : 		# End HorzScan
			x = count - 1
                        l = Table[x][y]
		  	festival = subprocess.Popen(["festival","--tts"], stdin=subprocess.PIPE, universal_newlines=True)
			festival.communicate(l)	
			print"Letter Selected : "+l
			indicateVertScan()
		    state = 0
		    count = 0
	time.sleep(0.1)			# sleep for 0.1 secs
    # end while
except KeyboardInterrupt :
    GPIO.cleanup()
    spi.close()
    print

