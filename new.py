import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import requests
import instaloader
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from UI import Ui_MainWindow
import operator
from bs4 import BeautifulSoup
import psutil
import math
from PIL import Image
import wolframalpha




engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1])
engine.setProperty('voice', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Wish
def wish():
    hour = int(datetime.datetime.now().hour)
    cur_time = time.strftime("%I:%M:%S %p")

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning!, Its {cur_time}")
    elif hour >=12 and hour < 18:
        speak(f" Good Afternoon!, Its {cur_time}")
    else:
        speak(f"Good Evening!, Its {cur_time}")

    speak("I am horcrux Sir, how may I help you")

#send email
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("shrux2009@gmail.com", "lostinshruxforever")
    server.sendmail("shrux2009@gmail.com", to, content)
    server.close()

#To search Google
def search_google(search_query):
    search = driver.find_element_by_name("q")
    search.clear()
    search.send_keys(search_query)
    search.send_keys(Keys.RETURN)

#For news Update
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=4815afdb118b4210b0319968cb0b3536"

    main_page = get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"]
    for article in articles:
        head.append(article["title"])
    for i in range(len(day)):
        speak(f"Today's {day[i]} news is: {head[i]}")

#To read PDF
def pdf_reader():
    book = open('Machine_Learning.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages}")
    speak(f"Sir, Please enter the number of page I have to read ")
    pg = int(input("Please enter the number of Page : "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

#convert stats
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    print("%s %s" % (s, size_name[i]))
    return "%s %s" % (s, size_name[i])

#wolframalpha
def compute(question):
    try:
        client = wolframalpha.Client("4XW9PJ-7URT7JXUU8")
        answer = client.query(question)
        output = next(answer.results).text
        # print(output)
        return output
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

        #voice to text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 2
            audio = r.listen(source,timeout=4 )

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {query}\n")

        except Exception as e:
            # print(e) 
            print("Say that again please....")
            return "None"  
        return query.lower()

        
    def run(self):
        # self.TaskExecution()
    
        speak('I am in sleep mode now, tell me if you need anything')
        while True:
            self.query = self.takecommand()
            if "wake up" in self.query or "you there" in self.query:
                self.TaskExecution()



    def TaskExecution(self):
        # wish()
        speak("I am online now")
        while True:
            self.query = self.takecommand()

            if "open notepad" in self.query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open cmd" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyALLWindows()

            elif "play music" in self.query:
                music_dir = "D:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                # print(songs)
                os.startfile(os.path.join(music_dir, rd))

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP Address is {ip}") 

            if "wikipedia" in self.query:
                speak("Searching wikipedia....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open google" in self.query:
                # webbrowser.open("https://www.google.com/")
                PATH = "C:/Users/prathmesh/Desktop/PROJECTS/Voice-Assistant/driver/chromedriver.exe"
                options = Options()
                options.add_argument("start-maximized")
                webdriver = webdriver.Chrome(PATH, options=options)
                webdriver.get("https://www.google.com/")

            elif "search" in self.query:
                try:
                    speak("what should I search?")
                    search_query = self.takecommand()
                    search_google(search_query)
                    speak("search complete")

                except Exception as e:
                    print(e)
                    speak("sorry, I am not able to search")

            elif "open first link" in self.query:
                pyautogui.moveTo(0, 500)
                time.sleep(1)
                pyautogui.click()
                pyautogui.keyDown('tab')
                pyautogui.keyDown('enter')

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open github" in self.query:
                webbrowser.open("www.github.com")

            elif "send whatsapp message" in self.query:
                kit.sendwhatmsg("+919768886622", "Test Successfull", 2, 25)

            elif "play song on youtube" in self.query:
                speak("Sir, what do you want to listen")
                command = self.takecommand()
                kit.playonyt(f"{command}")

            elif "open vs code" in self.query:
                codepath = "C:\\Users\\prathmesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

            elif "send email without subject" in self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand()
                    to = "shrutir3120@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to send this email")

            elif "sleep" in self.query:
                speak("See you later Sir, have a good day")
                break

            elif "close notepad" in self.query:
                speak("Closing notepad...")
                os.system("taskkill /f /im notepad.exe")

            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==17:
                    music_dir = "D:\\music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            # elif "take screenshot" in self.query:
            #     current_time = time.strftime("%d%m%Y")

            #     img = pyautogui.screenshot()
            #     img.save('Screenshot' + current_time + '.jpg')

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt") 

            elif "tell me news" in self.query:
                speak("Please wait Sir, Fetching the latest news")
                news()

            elif "send email" in self.query:
                speak("what should i say")
                self.query = self.takecommand()
                if "send a file" in self.query:
                    email = "shrux2009@gmail.com"
                    password = "lostinshruxforever"
                    send_to_email = "prathameshchaskar2@gmail.com"
                    speak("what is the subject for this email")
                    self.query = self.takecommand()
                    subject = self.query
                    speak("what is the message for this email")
                    self.query2 = self.takecommand()
                    message = self.query2
                    speak("Sir, please enter correct path of the file to the shell")
                    file_location = input("Please enter the path here")
                    speak("Please wait, I am sending email now")

                    msg = MIMEMultipart()
                    msg["From"] = email
                    msg["To"] = send_to_email
                    msg["Subject"] = subject

                    msg.attach(MIMEText(message,'plain'))

                    #setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location,'rb')
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    #Attach the attachment to the MIMEMUltipart object
                    msg.attach(part)

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("Email has been sent!!")

                else:
                    email = "shrux2009@gmail.com"
                    password = "lostinshruxforever"
                    send_to_email = "prathameshchaskar2@gmail.com"
                    message = query

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("Email has been sent!!")

            elif "where i am" in self.query or "where we are" in self.query:
                speak("Wait Sir, Let me check")
                try:
                    ipadd = requests.get('https://api.ipify.org').text
                    print(ipadd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    region = geo_data['region']
                    country = geo_data['country']
                    speak(f"Sir I am not sure, Bute I think we are in {city} city in {region} state of this {country} country")
                except Exception as e:
                    speak("Sorry Sir, Dur to network issue I am not able to fine where we are")
                    pass

            elif "instagram profile" in self.query or "profile on instagram" in self.query :
                speak("Sir, please enter the username correctly")
                name= input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"here is the profile of the user {name}")
                time.sleep(3)
                speak("Sir would you like to download profile picture of this account?")
                condition = self.takecommand()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I am done Sir, Profile picture is saved in our main folder Now I am ready to take next command")
                else:
                    pass
            
            elif "read pdf" in self.query:
                pdf_reader()

            # elif "calculate" in self.query:
            #     r = sr.Recognizer()
            #     with sr.Microphone() as source:
            #         speak("Say What you want to calculate,example: 3 plus 2")
            #         print("listening....")
            #         r.adjust_for_ambient_noise(source)
            #         audio = r.listen(source)
            #     my_string = r.recognize_google(audio)
            #     print(my_string)
            #     def get_operator_fn(op):
            #         return {
            #             '+' : operator.add, #plus
            #             '-' : operator.sub, #minus
            #             'x' : operator.mul, #multiplied by
            #             'divided' : operator.__truediv__,
            #         }[op]

            #     def eval_binary_expr(op1, oper, op2):
            #         op1, op2 = int(op1), int(op2)
            #         return get_operator_fn(oper)(op1,op2)
            #     speak("Your Result is")
            #     speak(eval_binary_expr(*(my_string.split())))

            elif "temperature" in self.query:
                speak("which temperature you want to check")
                self.query = self.takecommand()
                url = (f"https://www.google.com/search?q={self.query}")
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"Current {self.query} is {temp}")

            elif "battery" in self.query or "how much power left" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"Sir our system have {percentage} percent battery")
                if percentage>=75:
                    speak("we have enough power to continue our work")
                elif percentage>=40 and percentage<=75:
                    speak("we should connect our system to charging point to charge our battery")
                elif percentage>=20 and percentage<=40:
                    speak("we don't have enough power to work, please connect to charging point")
                elif percentage<=20:
                    speak("we have very low power,please connect to charging the system will shut down soon")

            elif "system " in self.query:
                cpu_stats = str(psutil.cpu_percent())
                battery_percent = psutil.sensors_battery().percent
                memory_in_use = convert_size(psutil.virtual_memory().used)
                total_memory = convert_size(psutil.virtual_memory().total)
                speak(f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent")
            

            elif "take screenshot" in self.query or "take a screenshot" in self.query or "capture the screen" in self.query:
                speak("By what name do you want to save the screenshot?")
                name = self.takecommand()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                save_name = f"{name}.png"
                img.save(save_name)
                speak("The screenshot has been succesfully captured")

            elif "show me the screenshot" in self.query:
                try:
                    # speak("Which screenshot you want to see?")
                    # ssname= self.takecommand()
                    # filepath = "C:/Users/prathmesh/Desktop/PROJECTS/Voice-Assistant"
                    # img = Image.open('C:/Users/prathmesh/Desktop/PROJECTS/Voice-Assistant/' + ssname + ".png")
                    img = Image.open('C:/Users/prathmesh/Desktop/PROJECTS/Voice-Assistant/' + save_name)
                    img.show()
                    speak("Here it is sir")
                    time.sleep(2)

                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")

            elif "open screenshot" in self.query:
                try:
                    speak("Which screenshot you want to see?")
                    ssname= self.takecommand()
                    # filepath = "C:/Users/prathmesh/Desktop/PROJECTS/Voice-Assistant"
                    img = Image.open('C:/Users/prathmesh/Desktop/PROJECTS/Voice-Assistant/' + ssname + ".png")
                    
                    img.show()
                    speak("Here it is sir")
                    time.sleep(2)

                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")


            elif "find" in self.query:
                speak("what you want to find?")
                question = self.takecommand()
                output = compute(question)
                speak(output)

            elif "search google" in self.query:
                options = Options()
                options.add_argument("start-maximized")
                speak("what should I search?")
                search_query = self.takecommand()
                speak("Okay sir!")
                speak(f"Searching for {search_query}")
                # PATH = "C:/Users/prathmesh/Desktop/PROJECTS/Voice-Assistant/driver/chromedriver.exe"
                driver = webdriver.Chrome('chromedriver', options=options)
                driver.get('https://www.google.com//search?q ='+search_query)
                # search_google(search_query)
                speak("search complete")
                # search = driver.find_element_by_name("q")
                # search.clear()
                # search.send_keys(str(search_query))
                # search.send_keys(Keys.RETURN)

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/prathmesh/Desktop/PROJECTS/Voice-Assistant/gif-1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/prathmesh/Desktop/PROJECTS/Voice-Assistant/gif-2.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)


app = QApplication(sys.argv)
Horcrux = Main()
Horcrux.show()
exit(app.exec_())

