from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys


recognizer = speech_recognition.Recognizer()


speaker = tts.init()
speaker.setProperty('rate',200) #This is to set up the speed of the bots speech it can be 300, 200 , 150.

#we gonna have a tudo list

tudo_list = ['Go shopping', 'Clean Room','Record Video']

def create_none():
    global recognizer

    speaker.say("What do you want to your note ?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a filename!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognise_google(audio)
                filename = filename.lower()
            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand! Please try again!")
            speaker.runAndWait()
def add_tudo():
    global recognizer

    speaker.say("What to do, do you want to add?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition() as mic:

                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognizer_google(audio)
                item =  item.lower()

                tudo_list.append(item)

                done = True

                speaker.say(f"I added {item} to the to do list!")

                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand! Please try again!")
            speaker.runAndWait()

def show_tudos():

    speaker.say("The items on your to do list are the following")

    for item in tudo_list:
        speaker.say(item)
    speaker.runAndWait()


def greetings():
    speaker.say("What can I do for you?")
    speaker.runAndWait()

def quit():

    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)

mappings = {
    "greeting" : greetings,
    "create_note": create_none,
    "add_tudo" : add_tudo,
    "show_tudo" : show_tudos,
    "exit": quit
}
                


    

assistant =  GenericAssistant('intents.json', intent_methods = mappings)
assistant.train_model()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic)

            message = recognizer.recognizer_google(audio)

            message = message.lower()

        assistant.request(message)


    except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            # speaker.say("I did not understand! Please try again!")
            # speaker.runAndWait()
