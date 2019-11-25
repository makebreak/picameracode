# picameracode
code for picamera on raspberry pi

You add the service file to start at boot time on the raspberry's Linux OS.
The python script recordVideoPi.py will run when triggered by a sensor (here I was using a particle cloud sensor named "quit"), then light up LED lights on the circuit board, start and stop video recording, and store the recording in a folder on Google drive.
