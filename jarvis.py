import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk

class AssistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis")
        self.root.geometry('600x600')

       
        # ====start button
        start = Button(self.root, text='START', font=("times new roman", 14), command=self.start_option).place(x=150, y=520)

        # ====close button
        close = Button(self.root, text='CLOSE', font=("times new roman", 14), command=self.close_window).place(x=350, y=520)

    # ==== start assitant
    def start_option(self):
        listener = sr.Recognizer()
        engine = pyttsx3.init()

        # ==== Voice Control
        def speak(text):
            engine.say(text)
            engine.runAndWait()

        # ====Default Start
        def start():
            # ==== Wish Start
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                wish = "Good Morning!"
            elif hour >= 12 and hour < 18:
                wish = "Good Afternoon!"
            else:
                wish = "Good Evening!"
            speak('Hello Sir,' + wish + ' I am Jarvis. Please tell me what can I do for you')
            # ==== Wish End

        # ==== Take Command
        def take_command():
            try:
                with sr.Microphone() as data_taker:
                    print("Say Something")
                    voice = listener.listen(data_taker)
                    instruction = listener.recognize_google(voice)
                    instruction = instruction.lower()
                    return instruction
            except sr.UnknownValueError:
                speak("I did not understand, can you repeat again")
                return take_command()
            except sr.RequestError as e:
                speak("Sorry, there was an error; {0}".format(e))
                return take_command()
            except Exception as e:
                speak("An error occurred: {0}".format(e))
                return take_command()

        # ==== Run command
        def run_command():
            instruction = take_command()
            print(instruction)
            try:
                if 'who are you' in instruction:
                    speak('I am Jarvis')

                elif 'what can you do for me' in instruction:
                    speak('I can play songs, tell time, and help you go with wikipedia')

                elif 'current time' in instruction:
                    time = datetime.datetime.now().strftime('%I: %M')
                    speak('current time is ' + time)

                elif 'open google' in instruction:
                    speak('Opening Google')
                    webbrowser.open('google.com')

                elif 'open youtube' in instruction:
                    speak('Opening Youtube')
                    webbrowser.open('youtube.com')

                elif 'open facebook' in instruction:
                    speak('Opening Facebook')
                    webbrowser.open('facebook.com')

                elif 'open python geeks' in instruction:
                    speak('Opening PythonGeeks')
                    webbrowser.open('pythongeeks.org')

                elif 'open linkedin' in instruction:
                    speak('Opening Linkedin')
                    webbrowser.open('linkedin.com')

                elif 'open gmail' in instruction:
                    speak('Opening Gmail')
                    webbrowser.open('gmail.com')

                elif 'open stack overflow' in instruction:
                    speak('Opening Stack Overflow')
                    webbrowser.open('stackoverflow.com')
                elif 'open camera' in instruction:
                    speak('Opening camera')
                    webbrowser.open('camera.com')
                elif 'shutdown' in instruction:
                    speak('I am shutting down')
                    self.close_window()
                    return False
                else:
                    speak('I did not understand, can you repeat again')
            except Exception as e:
                speak('An error occurred: {0}'.format(e))
            return True

        # ====Default Start calling
        start()

        # ====To run assistance continuously
        while True:
            if run_command():
                run_command()
            else:
                break

    # ==== Close window
    def close_window(self):
        self.root.destroy()

# ==== create tkinter window
root = Tk()

# === creating object for class
obj = AssistanceGUI(root)

# ==== start the gui
root.mainloop()
