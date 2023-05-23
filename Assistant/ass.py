import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning my boss")
    elif hour>=12 and hour<18:
        speak("Good Afternoon  ")
    else:
        speak("good Evening ")

    speak(" what can i do for you  :")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        print(" please repeat again u wanna do ...")
        speak(" please repeat again u wanna do ...")
        return "NONE"
    return query
if __name__ == "__main__": 
 wishMe()
 while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('Searchingv..')
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query,sentences=2)
        speak('According to wikipedia')
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'search' in query:
        query=query.replace("search","")
        webbrowser.open(query)


    elif 'open telegram' in query:
        webbrowser.open("www.telegram.com")


 
     