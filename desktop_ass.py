import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import time
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
a=engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>18 and hour<20:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am Robo Madam, Please tell me how may I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print('Recognising...')
        query = r.recognize_google(audio,language='en-in')
        print('User said..',query)
    except Exception as e:
        print(e)
        speak('Say that again please ')
        return 'None'
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query)
            speak('According to wikipedia...')
            print(result)
            speak(result)
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open spotify' in query:
            webbrowser.open('spotify.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = "D:\\new songs"
            song = os.listdir(music_dir)
            print(song)
            songs = random.choice(song)
            os.startfile(os.path.join(music_dir,songs))
        elif 'time' in query:
            the_time=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is{the_time}")
        elif 'open pycharm' in query:
            dir =  "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
            os.startfile(dir)
        elif 'open sublime' in query:
            dir2 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
            os.startfile(dir2)
        elif 'love' in query:
            speak('lol!! stop being stupid')
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'quit' in query:
            speak("Signing off ")
            exit()



