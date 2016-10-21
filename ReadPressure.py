import spidev
import time
spi = spidev.SpiDev()			# create spi object
spi.open(0, 1)				# open spi port 0, device (CS) 1
try:
    while True:
        resp = spi.readbytes(2)		# read two bytes
	print resp
	time.sleep(0.1)			# sleep for 0.1 secs
    # end while
except KeyboardInterrupt :
    spi.close()

