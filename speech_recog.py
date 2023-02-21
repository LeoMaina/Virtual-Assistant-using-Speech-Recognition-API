import speech_recognition as sr
from datetime import date
#from gpiozero import LED
from time import sleep
import pyttsx3 as tts
import sys
import threading

#red = LED(17)
#relay1 = LED(14)
#relay2 = LED(15)

r = sr.Recognizer()
speaker = tts.init()
speaker.setProperty("rate", 130)

print("Speak into the mic")

while True:
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic)
            audio = r.listen(mic)
            text = r.recognize_google(audio)
            text = text.lower()
            print(text)

            if "virtual assistant" in text:
                speaker.say("Yes, How can I help you Leonard?")
                speaker.runAndWait()

            if "stop" in text:
                speaker.say("I am shutting down")
                speaker.runAndWait()
                #speaker.stop()
                #root.destroy()
                #sys.exit()

            if "what is the difference between sam and liverpool" in text:
                speaker.say("Hello Leonard, There is no difference because Sam is at position 10 in Fantasy Premier League, and Liverpool is at position 10 in English Premier League Ha Ha Ha")
                speaker.runAndWait()


    except:
        continue

    # if words == "today":
    #     print(date.today())

    # if words == "LED on":
    #     red.on()

    # if words == "LED off":
    #     red.off()

    # if words == "relay one on":
    #     relay1.on()

    # if words == "relay one off":
    #     relay1.off()

    # if words == "relay two on":
    #     relay2.on()

    # if words == "relay two off":
    #     relay2.off()

    # if words == "exit":
    #     print("...")
    #     sleep(1)
    #     print("...")
    #     sleep(1)
    #     print("...")
    #     sleep(1)
    #     print("Goodbye")
    #     break