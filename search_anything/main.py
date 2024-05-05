import pyttsx3
import wikipedia
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    voice=pyttsx3.init()
    speaker.speak("search anything ")
    query=input("searching wikipedia/google: ")
    if query=="exit":
        break
    else:
        result=wikipedia.summary(query,sentences =3)
        print(result)
        voice.say(result)
        voice.runAndWait()
