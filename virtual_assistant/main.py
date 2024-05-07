import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your personal assistent Sir. Please tell me how may I help you")  

print("you can give these commands : ")
print("wikipedia")
print("open youtube")
print("open google")
print("open stack overflow")
print("open facebook")
print("open instagram")
print("open helpline")
print("open hotstar")
print("play music")
print("open code")
print("email to sanskar")
print("\n system")
print("kya baat hai")
print("maan meri jaan")
print("bijli")
print("temporary pyar")
print("ishare tere")
print("arijit singh")
print("love song")
print("lofi song")
print("k")
print("kahani")
print("sad song")
print("sidhu mose wala")
print("arman malik")
print("hardy sandhu")
print("king")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sanskar.c.0824@iibm.in', '$@n$k@r109')
    server.sendmail('sanskar.c.0824@iibm.in', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")   

        elif 'open helpline' in query:
            webbrowser.open("codershelpline.com")   

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")  

        elif 'system'    in query:
            webbrowser.open("https://www.youtube.com/watch?v=h22bQJXTqX0&pp=ygUWc3lzdGVtIGJ5IGVsdmlzaCB5YWRhdg%3D%3D")  

        elif 'kya baat hai' in query:
            webbrowser.open("https://www.youtube.com/watch?v=G0Hx6uN2AJE&pp=ygUMa3lhIGJhYXQgaGFp")  

        elif 'bijli' in query:
            webbrowser.open("https://www.youtube.com/watch?v=NwdQx2P_ytk")

        elif 'ishare tere' in query:
            webbrowser.open("https://www.youtube.com/watch?v=nNxCJ96GyQA") 

        elif 'temporary pyar' in query:
            webbrowser.open("https://www.youtube.com/watch?v=-MgJ8TURS3U") 

        elif 'arijit singh' in query:
            webbrowser.open("https://www.youtube.com/watch?v=lzdQ_b8lzo0") 

        elif 'love song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=0HSDFDENY4w")

        elif 'lofi song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=G8x1nt_8GUo")

        elif 'darshan raval' in query:
            webbrowser.open("https://www.youtube.com/watch?v=V6D-Lh_t0dA")

        elif 'ke' in query:
            webbrowser.open("https://www.youtube.com/watch?v=jRxPHHhnfoI")

        elif 'kahani' in query:
            webbrowser.open("https://www.youtube.com/watch?v=_XBVWlI8TsQ")

        elif 'sad song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=Be2GJpACO7c&pp=ygUJc2FkIHNvbmdz")

        elif 'sidhu' in query:
            webbrowser.open("https://www.youtube.com/watch?v=gWw_CVtjBrQ&pp=ygUac2lkaHUgbW9vc2Ugd2FsYSBwbGF5bGlzdCA%3D")

        elif 'armaan' in query:
            webbrowser.open("https://www.youtube.com/watch?v=VFjKpDgnUrM&pp=ygUVYXJtYWFuIG1hbGlrIHBsYXlsaXN0")

        elif 'sandhu' in query:
            webbrowser.open("https://www.youtube.com/watch?v=jWxCqzYtsZY&pp=ygUMaGFyZHkgc2FuZGh1")

        elif 'king' in query:
            webbrowser.open("https://www.youtube.com/watch?v=wCrIWNEPLQY&pp=ygUNa2luZyBwbGF5bGlzdA%3D%3D")

        elif 'man meri jaan' in query:
            webbrowser.open("https://www.youtube.com/watch?v=VuG7ge_8I2Y&pp=ygUObWFhbiBtZXJpIGphYW4%3D")

        elif 'Trisha ' in query:
            webbrowser.open("https://www.instagram.com/trisha.2210/")

        elif 'Tu Hi Tu ' in query:
            webbrowser.open("https://www.youtube.com/watch?v=8sLS2knUa6Y&pp=ygUjdHUgaGFpIHRvIG11amhlIGZpciBhdXIga3lhIGNoYWhpeWU%3D")

        elif 'play music' in query:
            music_dir = r'C:\Users\ASUS\OneDrive\Desktop\audio'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = r"C:\Users\ASUS\OneDrive\Desktop\python projects\virtual assistent"
            os.startfile(codePath)

        elif 'email to sanskar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "0703krsanskar@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend sanskar bhai. I am not able to send this email")    
