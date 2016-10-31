import spidev
import time
spi = spidev.SpiDev()			# create spi object
spi.open(0, 0)				# open spi port 0, device (CS) 1
spi.mode = 0b11				# 1,1 - 3 bytes read; 0,0 - 4 bytes read
try:
    byteRead = spi.readbytes(1)
    print byteRead
    while True:
        while ( byteRead[0] == 255 ) :
            byteRead = spi.readbytes(1)	       # Read initial byte
        bytesRest = spi.readbytes(2)	       # if not 255 read next 2 bytes
        print byteRead + bytesRest
        value = byteRead[0] * 256 + bytesRest[0]   # get value ignore least sig byte
        print value
	time.sleep(0.1)			# sleep for 0.1 secs
    # end while
except KeyboardInterrupt :
    spi.close()

