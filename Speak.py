import pyttsx3 # pip install pyttsx3
import json
from pathlib import Path

# Speak Function
def Say(text):

    engine = pyttsx3.init()

    # Load data from JSON files
    try:
        Data = json.loads(Path("settings.json").read_text())

        Speak_Rate = Data['Speak']['Rate']
        Speak_Volume = Data['Speak']['Volume']
        Speak_Voice = Data['Speak']['Voice']

    except:
        Speak_Rate = 125
        Speak_Volume = 1.0
        Speak_Voice = 0


    """ RATE"""
    rate = engine.getProperty('rate')
    engine.setProperty('rate', Speak_Rate)

    """VOLUME"""
    volume = engine.getProperty('volume')
    engine.setProperty('volume', Speak_Volume)

    """VOICE"""
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[Speak_Voice].id)

    engine.say(text)
    engine.runAndWait()

