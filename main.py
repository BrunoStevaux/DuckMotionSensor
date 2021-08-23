import RPi.GPIO as gp
import time
import subprocess

gp.setmode(gp.BOARD)
gp.setup(11, gp.IN)

while True:
	if gp.input(11):
		subprocess.run("omxplayer --no-keys duck.mp3 &", shell = True, capture_output=True)
		while(gp.input(11)): # Wait for signal to turn off. 
			pass
		time.sleep(6)