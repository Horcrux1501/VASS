import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1])
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >=12 and hour < 18:
        speak(" good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am crux Sir, how may I help you") 

def takeCommand():
    # It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e) 
        print("Say that again please....")
        return "None"  
    return query.lower()

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("shrux2009@gmail.com", "lostinshruxforever")
    server.sendmail("shrux2009@gmail.com", to, content)
    server.close()

def search_google(search_query):
    search = webdriver.find_element_by_name("q")
    search.clear()
    search.send_keys(search_query)
    search.send_keys(Keys.RETURN)


# def search_link(search_query):
#     search = driver.find_elements_by_tag_name("a")
#     search.clear()
#     search.send_keys(search_query)
#     search.send_keys(Keys.RETURN)



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 6)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open google" in query:
            # webbrowser.open("https://www.google.com/")
            PATH = "C:\Program Files (x86)\chromedriver.exe"
            webdriver = webdriver.Chrome(PATH)
            webdriver.get("https://www.google.com/")

        elif "search" in query:
            try:
                speak("what should I search?")
                search_query = takeCommand()
                search_google(search_query)
                speak("search complete")

            except Exception as e:
                print(e)
                speak("sorry, I am not able to search")

            
        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com/")

        elif "open spotify" in query:
            webbrowser.open("https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM?si=DFqQ3JHUR5SD3hVcyHvb-A")
        
        elif "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"the time is {strtime}")

        elif "open code" in query:
            codepath = "C:\\Users\\prathmesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "shrutir3120@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

