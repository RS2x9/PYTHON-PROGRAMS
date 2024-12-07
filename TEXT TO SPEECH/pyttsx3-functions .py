import pyttsx3    #this module converts text to sound

engine = pyttsx3.init('sapi5')
''' Specify engine for Windows: On Windows systems, pyttsx3 can utilize
the built-in Speech Application Programming Interface (SAPI5).
By specifying engine='sapi5' during initialization,
you're essentially telling pyttsx3 to use SAPI5 for Text-to-Speech tasks        '''

voices = engine.getProperty('voices')    # we Get available voices

engine.setProperty('voice', voices[1].id)    # we have set voice
'''    when we use voices[0].id then man voice will come .     '''

rate = 140          # Words per minute  # this is speed of speaking 
engine.setProperty('rate', rate)  # we have set speed of speaking 

#  Volume (range 0.0 to 1.0):
volume = 0.9      
engine.setProperty('volume', volume)

text_to_speak = "hahaha"
engine.say(text_to_speak)
engine.runAndWait()  # processes the sound 

