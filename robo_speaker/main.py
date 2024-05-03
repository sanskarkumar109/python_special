import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
while True:
    print("Enter the word you want to speak it out by computer")
    s = input()
    speaker.Speak(s)
    if s=="bye":
        speaker.speak("bye bye friends")
        break
    if s=="by":
        speaker.speak("bye bye friends")
        break
    if s=="bi":
        speaker.speak("bye bye friends")
        break
