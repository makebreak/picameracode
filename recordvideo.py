#!/usr/bin/env python3

import picamera, datetime, time
from time import strftime
 
#date to string
date1 = datetime.datetime.now()
datestring = date1.strftime("%m-%d-%Y-%H:%M")

#make file
my_file = open(datestring+'.h264', 'wb')

#take video
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording(datestring+'.h264')
camera.wait_recording(10)
camera.stop_recording()

# At this point my_file.flush() has been called, but the file has
# not yet been closed
my_file.close()
