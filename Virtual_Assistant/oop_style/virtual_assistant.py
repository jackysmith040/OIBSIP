"""
programme: Virtual Assistant
date: 14th February 2024
@author: fafali
"""

import speech_recognition as sr
import pyttsx3
import os
import pywhatkit as pwk
import datetime
import pyautogui
from time import sleep

class SpeechEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate',  160)
        self.engine.setProperty('volume',  1.0)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

class CommandList:
    def __init__(self):
        self.commands = {
            'youtube': 'Relax and chill, opening youtube',
            'time': 'It is currently',
            'commands': 'Here are the available commands',
            'screenshot': 'Taking a screenshot',
            'volume_up': 'Increasing volume',
            'volume_down': 'Decreasing volume',
            'shutdown': 'Shutting down the computer',
            'restart': 'Restarting the computer',
            'sleep': 'Putting the computer to sleep',
            'greeting': 'Hello, how can I assist you today?'
        }

    def get_commands(self):
        return self.commands

class VirtualAssistant:
    def __init__(self):
        self.speech_engine = SpeechEngine()
        self.command_list = CommandList()
        

    def listen_for_commands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
        except Exception as e:
            print("An unexpected error occurred.")
            return ""


    def get_commands(self):
        return self.commands
    
    
    def say_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        message = f"{self.command_list.get_commands()['time']} {current_time}"
        print(message)
        self.speech_engine.say(message)
        

    def say_commands(self):
        commands = ', '.join(self.command_list.get_commands().keys())
        message = f"{self.command_list.get_commands()['commands']}: {commands}"
        print(message)
        self.speech_engine.say(message)
        

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        message = 'Screenshot taken and saved.'
        print(message)
        self.speech_engine.say(message)
        

    def increase_volume(self):
        pyautogui.press('volumeup')
        message = 'Volume increased.'
        print(message)
        self.speech_engine.say(message)
        

    def decrease_volume(self):
        pyautogui.press('volumedown')
        message = 'Volume decreased.'
        print(message)
        self.speech_engine.say(message)
        

    def schedule_shutdown(self):
        pwk.shutdown(20)
        message = 'Shutdown scheduled.'
        print(message)
        self.speech_engine.say(message)
        

    def cancel_shutdown(self):
        pwk.cancel_shutdown()
        message = 'Shutdown canceled.'
        print(message)
        self.speech_engine.say(message)
        

    def restart_computer(self):
        os.system('shutdown /r /t   1')
        message = 'Computer restarting.'
        print(message)
        self.speech_engine.say(message)
        

    def put_computer_to_sleep(self):
        os.system("rundll32.exe powrprof.dll,SetSuspendState   0,1,0")
        message = 'Computer going to sleep.'
        print(message)
        self.speech_engine.say(message)
        

    def greet_user(self):
        message = self.command_list.get_commands()['greeting']
        print(message)
        self.speech_engine.say(message)
        

    def perform_wiki_search(self, query):
        info = pwk.info(query,   3, True)
        message = f'Searching Wikipedia for "{query}"'
        self.speech_engine.say(message)
        print(message)
        print(info)
        print('Network so it might take some time....')
        self.speech_engine.say(info)
        sleep(12)

    def perform_youtube_search(self, query):
        pwk.playonyt(query)
        message = f'Searching YouTube for "{query}"'
        print(message)
        print('Network so it might take some time....')
        self.speech_engine.say(message)
        sleep(12)

    def perform_web_search(self, query):
        pwk.search(query)
        message = f'Searching the web for "{query}"'
        print(message)
        print('Network so it might take some time....')
        self.speech_engine.say(message)
        sleep(12)

    
    
    def perform_commands(self, text):
        command_actions = {
            'time': lambda: self.say_time(),
            'list': lambda: self.get_commands(),
            'commands': lambda: self.say_commands(),
            'wikipedia': lambda: self.say_this(self.command_list.get_commands()['wikipedia']) and self.perform_wiki_search(text),
            'youtube': lambda: self.perform_youtube_search(text),
            'search': lambda: self.perform_web_search(text),
            'screenshot': lambda: self.take_screenshot(),
            'volume up': lambda: self.increase_volume(),
            'volume down': lambda: self.decrease_volume(),
            'shut down': lambda: self.schedule_shutdown(),
            'cancel': lambda: self.cancel_shutdown(),
            'restart': lambda: self.restart_computer(),
            'sleep': lambda: self.put_computer_to_sleep(),
            'hello': lambda: self.greet_user(),
        }

        for command, action in command_actions.items():
            if command in text:
                action()
                break
     

    def run(self):
        while True:
            print('Listening, please speak louder\n')
            self.speech_engine.say('Listening, please speak louder')
            command = self.listen_for_commands()
            if command:
                if 'exit' in command or 'stop' in command:
                    print('\nGoodbye, thank you for your time and patience. Love you')
                    self.speech_engine.say('Goodbye, thank you for your time and patience. Love you')
                    break
                else:
                    self.perform_commands(command)
                    sleep(4)
                    print('\nDone. How can I help you today?\n\n')
                    self.speech_engine.say('Done. How can I help you today?')
            else:
                print('\nSorry cant hear.  Please speak clearly\n')
                self.speech_engine.say('Sorry, I couldn\'t hear you. Please speak clearly.')
                sleep(2)

if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.run()
