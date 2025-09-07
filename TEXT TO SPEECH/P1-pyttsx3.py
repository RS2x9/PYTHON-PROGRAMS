import pyttsx3
text_speech=pyttsx3.init()           #init() is used to initiate pyttsx3
answer=input('Enter something: ')
text_speech.say(answer)         # say() converts text to voice
text_speech.runAndWait()        # runndWait()  :it processes the voice commands
