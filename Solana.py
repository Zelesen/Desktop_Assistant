from cProfile import label


from multiprocessing.dummy.connection import Listener


from time import time


from timeit import Timer


import winsound


from xml.dom.minidom import Document


import speech_recognition as sr


import pyttsx3


import pywhatkit


import datetime


import wikipedia


import pyjokes


import webbrowser


import os


import pyautogui


import requests


from bs4 import BeautifulSoup


import speedtest


from PyQt5 import QtWidgets, QtCore, QtGui


from PyQt5.QtCore import QTimer, QTime, QDate, Qt


from PyQt5.QtGui import QMovie


from PyQt5.QtCore import *


from PyQt5.QtGui import *


from PyQt5.QtWidgets import *


from PyQt5.uic import loadUiType


from solanaui import Ui_SOLANA


import sys


#voices and properties....


engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 180)


#greetings...


def greet():
    

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:

        talk("good morning!")


    elif hour>=12 and hour<18:

        talk("good afternoon!")


    else:

        talk("good evening!")
    
    talk("i am SOLANA...how may i help you? ")


#weather


def temperature():
    
    
    search = "temperature in ulhasnagar"

    url = f"https://www.google.com/search?q={search}"

    r = requests.get(url)

    data = BeautifulSoup(r.text,"html.parser")

    temp = data.find("div", class_="BNeawe").text

    talk(f"current {search} is {temp}")


#important talk engine....


def talk(text):

    engine.say(text)

    engine.runAndWait()


#for interface...


class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()  


#important the whole AI configeration and running....


    def run(self):


        while True:

            talk("SOLANA currently offline... say start or wake up")
            self.query = self.take_command()

            if 'wake up' in self.query or 'awake' in self.query or 'start' in self.query :

                talk('i am online...ready to take commands')

                self.run_SOLANA()

            elif 'goodbye' in self.query:

                talk('goodbye sir...')

                sys.exit()



#taking command from user in order to generate query or command....


    def take_command(self):

      listener = sr.Recognizer()

      with sr.Microphone() as source:            
            
        print('Hearing >>>')

        listener.pause_threshold= 1

        listener.energy_threshold = 200

        voice = listener.listen(source)
        
        try:   
            
            self.query = listener.recognize_google(voice)
            
                  
    
        except Exception as e:
    
               return "none"
        
    
        self.query = self.query.lower()
    
        return self.query


#the whole command terminal or funtions that can be executed using SOLANA AI assistant....

    
    def run_SOLANA(self):
         
        greet()

#infinite loop.....
        

        while True:
                                    

            self.query = self.take_command()                         
            
#made SOLANA as a hotword to execute every command....             
            

            if "SOLANA" in self.query or "SOLANA" in self.query:

                self.query= self.query.replace("SOLANA" or "SOLANA", "")                            
                
                #conversations....can add more
                

                if 'hello' in self.query or 'hi' in self.query :

                    talk('hi sir... ')
                                        
                                        
                elif 'how are you' in self.query :

                    talk('i am fine sir...hope you are the same')
                                        
                                        
                elif 'what are you doing' in self.query :

                    talk('trying to be a helpful assistant sir..')
                
                
                elif 'tell me about yourself' in self.query :

                    talk('i am SOLANA...An AI assistant created by aman...i was created on september 2023...its my job to assist you on every point sir... ')
                
                elif 'are you okay' in self.query or 'you ok' in self.query :

                    talk('i am doing great sir...')
                
                elif 'tell me what all can u do' in self.query or 'what all things can you do' in self.query or 'what can you do' in self.query:

                    talk('i can do anything you want....i can open browser or search anything or tell you jokes or weather and many more stuffs..')


                #os basic...
                
                
                elif 'shutdown' in self.query :

                    talk("shutting down pc...")

                    os.system("shutdown /s /t 1")
                
                
                elif 'restart' in self.query :

                    talk('restarting pc...')

                    os.system("shutdown /r /t 1")
            
                
                elif 'logout' in self.query :

                    talk("logging out")

                    os.system("shutdown -l")
            
                
                elif 'close' in self.query :

                    talk('windows closed...')

                    pyautogui.keyDown('alt')

                    pyautogui.press('f4')

                    pyautogui.keyUp('alt')
                
                
                #volume
                
                
                elif 'volume up' in self.query :

                    pyautogui.press("volumeup")
                
                
                elif 'volume down' in self.query :

                    pyautogui.press("volumedown")
                
                
                elif 'mute' in self.query :

                    pyautogui.press("volumemute")
                
                
                #ip
                
                
                elif 'ip address' in self.query :
                
                    from requests import get
                    
                    ip = get('https://api.ipify.org').text

                    talk(f"your ip address is {ip}")
                
                
                #web 
                
                
                elif 'play' in self.query :

                    song = self.query.replace('play', '')

                    talk('playing '+ song)

                    pywhatkit.playonyt(song)
                    
                
                elif 'information about' in self.query :

                    talk('searching wikipidea...')

                    person = query.replace('inforation about', '')

                    info = wikipedia.summary(person , sentences=2)

                    talk('According to wikipidea...'+ info)
                
                
                elif 'search in google' in self.query or 'search on google' in self.query :

                    query = self.query.replace("search in google" or "search on google", "")

                    webbrowser.open(f"https://www.google.com/search?q={query}")
                
                
                elif 'time' in self.query or 'todays time' in self.query:

                    time = datetime.datetime.now().strftime('%I:%M %p')

                    talk('current time is '+ time)
                
                
                elif 'joke' in self.query or 'tell me a joke' in self.query or 'make me happy' in self.query:

                    fun=pyjokes.get_joke()

                    talk(fun)
                
                
                elif 'open youtube' in self.query :

                    talk('opening youtube...')

                    webbrowser.open('youtube.com')
                
                
                elif 'open google' in self.query :

                    talk('opening google..')

                    webbrowser.open('google.com')
                
                
                elif 'open wikipidea' in self.query :

                    talk('opening wikipidea..')

                    webbrowser.open('wikipidea.com')
                
                
                elif 'open instagram' in self.query :

                    webbrowser.open('instagram.com')
                
                
                elif 'open whatsapp' in self.query :

                    webbrowser.open('web.whatsapp.com')
                
                
                elif 'open twitter' in self.query :

                    webbrowser.open('twitter.com')
            
                
                elif 'open linkedin' in self.query :

                    webbrowser.open('linkedin.com')
                
                
                elif 'open gmail' in self.query :

                    talk("Opening Gmail..")

                    webbrowser.open('gmail.com')
                
                
                elif 'open facebook' in self.query :

                    talk("Opening Facebook..")

                    webbrowser.open('facebook.com')
                
                
                elif 'open calculator' in self.query :

                    talk("Opening calculator..")

                    os.system("calc.exe")
                
                
                elif 'open notepad' in self.query :

                    talk("Opening notepad...")

                    os.system("notepad.exe")
                
                
                elif 'open wordpad' in self.query :

                    talk("Opening wordpad...")

                    os.system("wordpad.exe")
                    
                
                elif 'screenshot' in self.query or 'take screenshot' in self.query:


                    img = pyautogui.screenshot()

                    img.save("screenshot.jpg")

                    talk("Screenshot captured..")

                    os.startfile("screenshot.jpg")                     
                
                
                #weather/location

                elif 'where we are' in self.query or 'where am i' in self.query :

                    talk('wait sir...let me check')
                    
                    try:

                        ipadd = requests.get('https://api.ipify.org').text

                        url = 'https://get.geojs.io/v1/ip/geo/' +ipadd+ '.json'

                        geo_requests = requests.get(url)

                        geo_data = geo_requests.json()


                        city = geo_data['city']

                        country = geo_data['country']

                        talk(f'sir i am not sure, but i think we are in {city} city of {country} country ')

                    except Exception as e :

                        talk('sorry sir due to network issue... i can find where we are')

                        pass

                
                
                elif 'temperature' in self.query or 'what is the temperature' in self.query :

                    temperature()
                
                
                elif 'internet speed' in self.query :

                    st= speedtest.Speedtest()

                    dl= st.download()

                    up= st.upload()

                    talk(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
                
                
                elif 'sleep' in self.query :

                    talk("ok sir...wake me up if you need help...")


                    break
  
#maintread function called again...


startExecution = MainThread()


#interface 


class Main(QMainWindow):
    

#setup of interface....    
    

    def __init__(self):
        
        super().__init__()

        self.ui = Ui_SOLANA()

        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.startTask)
        
        
#lookout of interface and starting of gif image when clicked.....    
    
    def startTask(self):
        

        self.ui.movie = QtGui.QMovie("C:/Users/Mafia/OneDrive/Documents/projects/AI/hackathon project/NANOTECH.gif")

        self.ui.label.setMovie(self.ui.movie)

        self.ui.movie.start()

        startExecution.start()
         
    
        
#application startup

app = QApplication(sys.argv)

SOLANA =  Main()

SOLANA.show()

exit(app.exec_())

 