import time
import datetime
from gtts import gTTS
from playsound import playsound

###GENRATE AUDIO
#tts = gTTS('PLEASE CONTACT SCHOOL NOW!');
#tts.save('data/audio.mp3');


now = datetime.datetime.now();
print(now);
alarm = [];

alarm.append(now.replace(hour=9, minute=9, second=0, microsecond=0));
alarm.append(now.replace(hour=10, minute=17, second=0, microsecond=0));
alarm.append(now.replace(hour=11, minute=25, second=0, microsecond=0));
alarm.append(now.replace(hour=13, minute=25, second=0, microsecond=0));
alarm.append(now.replace(hour=14, minute=33, second=0, microsecond=0));
alarm.append(now.replace(hour=15, minute=33, second=0, microsecond=0));

###Test
#alarm.append(now.replace(hour=15, minute=now.minute+1, second=0, microsecond=0));

### set a bool for each alarm.
#i=0;
#didplay = [];
#while i < len(alarm):
	#didplay.append(False);
	#i+=1;

while True:
	i=0;
	#update now
	now = datetime.datetime.now();
	while i < len(alarm):
		if(alarm[i].hour==now.hour and alarm[i].minute == now.minute):
			playsound('data/loose2.wav');
			print("ALARM! n."+str(i));
			print(now);
			###Debug
			#print(str(alarm[i].hour)+":"+str(alarm[i].minute)+" IS "+str(now.hour)+":"+str(now.minute))
			### Turn off alarm
			#didplay[i]=True;
		time.sleep(4);
		i+=1;

