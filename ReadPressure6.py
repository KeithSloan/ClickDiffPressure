from datetime import datetime

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
threshold = 350
state = 0
try:
    while True:
        resp = spi.readbytes(3)		# read three bytes
        if (resp[0] != 255) :		# Is conversion valid
           value = 256*resp[0] + resp[1]   # Discard least sig i.e. noise
	   print resp
           print value
           if ( value > threshold ) :
              if ( state == 0 ) or (state == 2 ) :
                 t1 = timemillisecs() 
                 print "t1 : "+str(t1)
                 state = 1
           else :
              if ( state == 1 ) :
                 t2 = timemillisecs()
                 print "t2 : "+str(t2)
                 state = 2
                 print "Pulse : "+str(t2-t1)
	time.sleep(0.1)			# sleep for 0.1 secs
    # end while
except KeyboardInterrupt :
    spi.close()
    print

