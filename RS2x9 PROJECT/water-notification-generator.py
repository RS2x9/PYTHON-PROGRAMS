                      # WATER -NOTIFICATION - GENERATOR - PROJECT

import time
import pyttsx3
# wecan schedule time when we want to get notification through task schedular in windows
# now
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
            title="Please drink water",
            message =" This is the time to drink water",     # This message wil be displaying
            app_icon=r"C:\Users\hp\Downloads\glass.ico",     # This icon will be showing   
            timeout=5       # the message will be displaying for 5 seconds
        )
        engine=pyttsx3.init()
        engine.setProperty('voice',engine.getProperty('voices')[1].id)
        engine.setProperty('rate',140)
        
        command="hey Sagar This is the Time to drink water"
        engine.say(command) ; engine.runAndWait()
        time.sleep(30*60) # timelapse to dispaly the messaage again and again is in seconds
        
''' to run this code after closing this program i,e we want to run app in the background
type in cmd pythonw.exe <program path>       '''
# if you want to stop this program running in background: kill  python.exe in task manager
