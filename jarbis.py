import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning punit")
    elif hour>=12 and hour<18:
        speak("good afternoon punit")
    else:
        speak("good night punit")
    speak(" i m cypher ,how can i help you ? ")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        # print(f"You said: {query}\n")
    except:
        print("say that again please...")
        return 'none'
    return query 

wishme()
if 1:
    query = takeCommand().lower()
    #searching in wikipedia
    if 'wikipedia' in query:
        speak("searching wikipedia...")
        query  = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    
    elif 'open google' in query:
        webbrowser.open('google.com')
    
    elif 'play music' in query:
        music_dir = 'location'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir time is {strTime}")
    
    elif 'hello' in query:
        response = ['hello sir','hello punit','hiii sir']
        speak(random.choice(response))
    
    elif 'how are you' in query or 'whats up' in query or 'how r u' in query:
        stmsg = ['i m fine sir','kind a smart','full of energy']
        speak(random.choice(stmsg))
    
    elif 'quit' in query or 'bye polo' in query or 'buy polo' in query:
        speak('quitting sir')
    else:
        speak(" again")