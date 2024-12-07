# this program is not working correctly

from gtts import gTTS
from playsound import playsound
# setting the language
language="en"
text="Hello world .This is Kumar, a big fan of narayan"
print(text)
# lang is used to specify language
# slow is used to make speech slow or not
# tld is used to specify accent
speech=gTTS(text=text,lang=language,slow=True,tld="com.au")
# saving the speech in mp3 file
speech.save("textToSpeech.mp3")
playsound("textToSpeech.mp3")
