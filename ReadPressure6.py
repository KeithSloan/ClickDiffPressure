import spidev
import time
spi = spidev.SpiDev()			# create spi object
spi.open(0, 0)				# open spi port 0, device (CS) 1
spi.mode = 0b11				# 1,1 - 3 bytes read; 0,0 - 4 bytes read
try:
    while True:
        resp = spi.readbytes(3)		# read three bytes
        if (resp[0] != 255) :		# Is conversion valid
           value = 256*resp[0] + resp[1]   # Discard least sig i.e. noise
	   print resp
           print value
	time.sleep(0.1)			# sleep for 0.1 secs
    # end while
except KeyboardInterrupt :
    spi.close()

