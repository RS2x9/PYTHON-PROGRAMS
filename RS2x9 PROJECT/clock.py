import time
from plyer import notification
import pyttsx3
tstamp=time.strftime('%H:%M:%S')
thour=int(time.strftime("%H"))
tmin=int(time.strftime("%M"))
tsec=int(time.strftime("%S"))
text_speech=pyttsx3.init()  # later in programs we will be using: text_speech as engine 
thour>=0
def speak(audio):
    rate=135
    text_speech.setProperty('rate',rate)
    notification.notify(
            title="What's the time now",
            message =f" its {thour} hour {tmin} minutes {tsec}s seconds",     # This message wil be displaying
            #app_icon=r"C:\Users\hp\Downloads\glass.ico",     # This icon will be showing   
            timeout=5
            )
    text_speech.say(audio) ; text_speech.runAndWait()
if thour<3:
    print(f"{thour}:{tmin}:{tsec}Am \n mmm its going to be morning now")
    speak(f"its {thour} hour {tmin} minutes {tsec}s seconds a m")
    
elif (thour>=3 and thour<12) and (tmin<=59 or tsec<=59):
    print(f"{thour}:{tmin} :{tsec}AM \n GOOD MORNING")
    speak(f"its {thour} hour {tmin} minutes {tsec}s seconds  GOOD MORNING")
elif (thour>=12 and thour <16) and (tmin<=59 or tsec<=59) :
    print(f"{thour}:{tmin}:{tsec}PM \n GOOD AFTERNOON")
    speak(f"its {thour} hour {tmin} minutes {tsec}s seconds P M  GOOD AFTERNOON")
    
elif (thour>=16 and thour <20) and (tmin<=59 or tsec<=59) :
    print(f"{thour}:{tmin}:{tsec}PM \n GOOD EVENING")
    speak(f"its {thour} hour {tmin} minutes {tsec}s seconds P M  GOOD EVENING")
    
elif (thour>=20 and thour <24) and (tmin<=59 or tsec<=59) :
    print(f"{thour}:{tmin}:{tsec}PM \n ")
    speak(f"its {thour} hour {tmin} minutes {tsec} seconds P M feeling coouull  ")
