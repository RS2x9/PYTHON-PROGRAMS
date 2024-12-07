#Module
import speech_recognition as sr
import pyttsx3 
import time 


#main code
engine = pyttsx3.init()
# engine.setProperty('voice', engine.getProperty('voices')[1].id)
def speak(text):
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    # Function to speak text
    engine.say(text)
    engine.runAndWait()
    
class recognize_speech:
    def __init__(self):
        self.r = sr.Recognizer()
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.r.pause_threshold = 1
            audio = self.r.listen(source)

        try:
            print("Recognizing...")
            query = self.r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query
    
     

if __name__ == "__main__":
    obj = recognize_speech()
    while True:
        query = obj.listen()
        speak(query)
    