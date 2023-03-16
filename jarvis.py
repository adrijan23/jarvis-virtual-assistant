import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import matplotlib
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

MASTER= "Adrian"

# Speak func will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
# This func will wish you based on time now
def wishMe():
    hour=int(datetime.datetime.now().hour)
    print(hour)

    if hour >=0 and hour<12:
        speak("Good morning "+ MASTER)
    elif hour>=12 and hour<18:
        speak("Good afternoon "+ MASTER)
    else:
        speak("Good evening "+ MASTER)

    speak("I am Jarvis. How may I help you?")
#This func will take command from the mic
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-us')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query=None
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('adrijan.radjevic@gmail.com', 'password')
    server.sendmail("rv02@gmail.com",to,content)
    server.close()


# Main program starts here
def main():
    speak("Initializing Jarvis...")
    wishMe()
    query=takeCommand()

    # Logic for executing tasks per the query
    if 'wikipedia' in query.lower():
        speak("Searching Wikipedia")
        query=query.replace('wikipedia','')
        results=wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        url="youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        url="google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open facebook' in query.lower():
        url="facebook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Adrijan Radjevic\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))

    elif 'the time' in query.lower():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER}, the time is {strTime}")

    elif 'pycharm' in query.lower():
        pycharm_path="C:\\Users\\Adrijan Radjevic\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(pycharm_path)
    elif 'email to my friend' in query.lower():
        try:
            speak("What should I send")
            content=takeCommand()
            to="reljavranjes02@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)

main()