from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys


recognizer = speech_recognition.Recognizer()


speaker = tts.init()
speaker.setProperty('rate',150) #This is to set up the speed of the bots speech it can be 300, 200 , 150.

#we gonna have a tudo list

tudo_list = ['Go shopping', 'Clean Room','Record Video']

def create_none():
    global recognizer

    speaker.say("What do you want to your note ?")
    speaker.runAndWait()
    

assistant =  GenericAssistant('intents.json')
assistant.train_model()
