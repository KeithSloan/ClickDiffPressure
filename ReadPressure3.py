#!/usr/bin/env python

import time
import pigpio

CE0 = 8
MISO = 9

pi = pigpio.pi()
if not pi.connected:
   exit()
h = pi.spi_open(0, 50000, 0b11)
pi.write(CE0, 1) # deselect sensor

try:
   while True:
      pi.write(CE0, 0) # select sensor
      while pi.read(MISO) == 1:
         time.sleep(0.01)
      b, d = pi.spi_read(h, 3) # read three bytes

      pi.write(CE0, 1) # deselect sensor
#      print(b, d)
      print b
      print str(d[0])+" : "+str(d[1])+" : "+str(d[2])
# ignore least significant byte noise as far as this app is concerned
      value = 256*d[0] + d[1]
      print value
      time.sleep(0.1)

except KeyboardInterrupt :
   pass

pi.spi_close(h)
pi.stop()
