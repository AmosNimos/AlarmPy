from time import sleep
import pyttsx3

delay = 60*20;
repeatDelay = 2;
repeatTime=4;
while True:
	repeat=0;
	sleep(delay);
	while repeat<repeatTime:
		sleep(repeatDelay);
		engine = pyttsx3.init();
		engine.say("Take a break! Go drink water!");
		engine.runAndWait();
		repeat+=1;
