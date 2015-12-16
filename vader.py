from time import sleep
import RPi.GPIO as GPIO
import PiFm2 as PiFm

def init_env():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(0)
	GPIO.setup(12,GPIO.OUT)

def eyes_on():
	GPIO.output(12,1)

def eyes_off():
	GPIO.output(12,0)

def power_darkside():
	eyes_on()
	PiFm.playMp3("./pifmlib/sounds/Darkside.mp3")
	eyes_off()

def breathing():
	eyes_on()
	PiFm.playMp3("./pifmlib/sounds/Vadrbrth.mp3")
	eyes_off()

def dont_make_destroy():
	eyes_on()
	PiFm.playMp3("./pifmlib/sounds/Dontmake.mp3")
	eyes_off()

def dont_fail():
	eyes_on()
	PiFm.playMp3("./pifmlib/sounds/Dontfail.mp3")
	eyes_off()

def dont_comeback():
	eyes_on()
	PiFm.playMp3("./pifmlib/sounds/Comeback.mp3")
	eyes_off()

init_env()
#AudioTest
'''
sleep(4)
power_darkside()
sleep(0.25)
breathing()
sleep(0.25)
dont_make_destroy()
sleep(0.25)
dont_fail()
'''
