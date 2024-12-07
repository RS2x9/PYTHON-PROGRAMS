import pyttsx3
import time
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib   #Simple Mail Transfer Protocol # this library  is used to send email
import email
import signal

def handle_interrupt(sig,frame):
    """Exitng the programp"""
    print("Exiting...")
    exit(0)
signal.signal(signal.SIGINT,handle_interrupt)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')    #Finding voices
engine.setProperty('voice',voices[1].id)     # setting female voice
speech_rate=145     # speaking rate of JARVIS
engine.setProperty('rate',speech_rate)    #setting speaking rate

# now JARVIS will wish according to time
def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Speak function error: {e}")
        print("Sorry, I can't speak right now.")
T_hour=int(time.strftime("%H"))
if T_hour>=0 and T_hour<12:
    speak("HEllo RISHAB good morning")
if T_hour>=12 and T_hour<16:
    speak("HEllo RISHAB Good after-noon")
if T_hour>=16 and T_hour<21:
    speak("HEllo RISHAB good evening")
if T_hour>=21 and T_hour<24:
    speak("HEllo RISHAB")
    
# taking audio input from user  and converting into text
def takecommand():
    r=sr.Recognizer()       #Recognizer is a class helps to recognize audio
    with sr.Microphone() as source:
        print("LIstening....")
        audio=r.listen(source)
        r.pause_threshold=0.3
        r.energy_threshold=400
        query=r.recognize_google(audio,language='en-in')     # 'en-in' is language code for English
    try:
        print("RECOGNIZING....")
        #global query
        #query=r.recognize_google(audio,language='en-in')     # 'en-in' is language code for English
        print(query)
    except Exception :
        speak(Exception)
        speak("Please speak again.")
        #continue
        return "None"  # Indicate no input captured
    return query

# we use the text obtained to perform tasks 
#query=takecommand()
if __name__== "__main__":
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            query=query.replace('wikipedia'," ")    # this will replace the word wikipedia and only our query go in search
            speak("searching wikipedia")
            try:
                results = wikipedia.summary(query,sentences=5)
                speak("According to Wikipedia")
                print(results) ; speak(results)
            except Exception as e:
                print(f"Wikipedia Error: {e}")
                speak(f"Sorry, I couldn't find anything related to:{query}")
            
        elif 'open youtube' in query:
            webbrowser.open(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\youtube.com")
            #this is target path 
            
        elif 'open chrome' in query:
            webbrowser.open(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe") # this is target path of chrome app
            
        elif 'open stackoverflow' in query:
            webbrowser.open(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\stackoverflow.com")
            
        #elif 'jarvis ai' in query:
            #os.startfile(r"C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\JARVIS-AI.py")  # this will start jarvis file again

        elif 'python programs' in query:
            os.startfile(r"C:\Users\hp\Desktop\PYTHON PROGRAMS")   # this is target path of python programs
            
        #elif 'play music in youtube' in query:
            #os.startfile(r"C:\Users\hp\Desktop\PYTHON PROGRAMS")
            
        elif 'the time' in query:
            speak(f"its {time.strftime("%H:%M:%S")}")
            
        elif 'open rs2x9 project' in query:
            os.startfile(r"C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT")
            
        #elif 'open rs2x9 ro706' or 'ro706 rs2x9' in query:
            #os.startfile(r"C:\Users\hp\Desktop\PYTHON PROGRAMS\Ro706-RS2x9")
            
        elif 'open vs code' in query:
            os.startfile(r"C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe")  # this is target path of vs code

        elif 'open python' in query:
            os.startfile(r"C:\Users\hp\AppData\Local\Programs\Python\Python312\pythonw.exe")
        elif 'you are a good' in query:
            speak('Thanks Rishab')
        
        elif 'zira exit' or 'jarvis exit' in query:
            exit(0)
