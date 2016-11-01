from datetime import datetime

def initTable() :
   Table = [[0 for y in range(5)] for x in range(6)]
   Table [0] [0] = "A"
   Table [0] [1] = "E"
   Table [0] [2] = "I"
   Table [0] [3] = "O"
   Table [0] [4] = "U"
   Table [1] [0] = "B"
   Table [1] [1] = "F"
   Table [1] [2] = "J"
   Table [1] [3] = "P"
   Table [1] [4] = "V"
   Table [2] [0] = "C"
   Table [2] [1] = "G"
   Table [2] [2] = "K"
   Table [2] [3] = "Q"
   Table [2] [4] = "W"
   Table [3] [0] = "D"
   Table [3] [1] = "H"
   Table [3] [2] = "L"
   Table [3] [3] = "R"
   Table [3] [4] = "X"
   Table [4] [2] = "M"
   Table [4] [3] = "S"
   Table [4] [4] = "Y"
   Table [5] [2] = "N"
   Table [5] [3] = "T"
   Table [5] [4] = "Z"

def timemillisecs():
    dt = datetime.now()
    return (dt.second*1000+dt.microsecond/1000 )

import spidev
import time
import sys
from datetime import datetime
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
           else :			# Signal is LOW
              if ( state == 1 ) :
                 t2 = timemillisecs()
                 print "t2 : "+str(t2)
		 count += 1
                 state = 2
                 print "Pulse : "+str(t2-t1)
	      if ( state == 2 ) :
		 t3 = timemillisecs()
		 if ((t3 - t2) > timeout ) :
		    print "TIME OUT : Count "+str(count)
		    state = 0
		    count = 0
	time.sleep(0.1)			# sleep for 0.1 secs
    # end while
except KeyboardInterrupt :
    spi.close()
    print

