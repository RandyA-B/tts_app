import pyttsx3


engine = pyttsx3.init() # Creats a tts engine
engine.say("Hello, I am your computer")
engine.runAndWait()