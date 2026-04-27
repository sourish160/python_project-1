import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import os
import music_Library
import requests
import time

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



def process_command(c):
    # open youtube
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    
    # open google
    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    
    # search on google
    elif "search" in c or "google" in c:
        query = c.replace("search", "").replace("google", "").strip()
    
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What should I search for?")
    
    # open facebook
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    
    # open linkedin
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn")

    # play any music
    elif "play any" in c and "song" in c:
        import random
        if music_Library.music:
            song = random.choice(list(music_Library.music.keys()))
            speak(f"Playing {song}")
            webbrowser.open(music_Library.music[song])
        else:
            speak("Your music library is empty")
    
    # play specific song
    elif c.lower().startswith("play"):
            song = c.lower().split(" ")[1]
            link = music_Library.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")

    
    # Time
    elif "time" in c:
        time_now = datetime.datetime.now().strftime("%I:%M:%S %p")
        speak(f"Right now the time is {time_now}")


    # Calculator
    elif "open calculator" in c:
        speak("Opening Calculator")
        os.system("calc")


    # Exit
    elif "exit" in c or "stop" in c:
        speak("Goodbye! see you later")
        exit()

       

if __name__ == "__main__":
    speak("Initializing Badboy. your personal assistant is ready to serve you.")
    while True:
        
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        
        
        # recognize speech using Google Speech Recognition
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            # print(word)
            if "bad boy" in word.lower():
                speak("Ya? tell me, what can I do for you?")
                # listen for command
                with sr.Microphone() as source:
                    print("badboy is active. Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    
                    process_command(command)

        except Exception as e:
            print("Error:", e)
