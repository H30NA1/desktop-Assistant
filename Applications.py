#-------------------------------------------------------------------------------------------------#
import os   #Let her use the operating system so that she can open any application in the windows

import pyttsx3
#-------------------------------------------------------------------------------------------------#

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#-------------------------------------------------------------------------------------------------#

def Speak_Function(text):
    engine.say(text)
    engine.runAndWait()

#-------------------------------------------------------------------------------------------------#

def calculator():
    os.startfile("C:\Windows\System32\calc.exe") #set the direction to the file

#-------------------------------------------------------------------------------------------------#

def notepad():
    os.startfile("C:\Windows\System32\\notepad.exe")

#-------------------------------------------------------------------------------------------------#

def msword():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word")

#-------------------------------------------------------------------------------------------------#

def msexcel():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel")

#-------------------------------------------------------------------------------------------------#

def msppt():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint")

#-------------------------------------------------------------------------------------------------#

def mspaint():
    os.startfile("C:\Windows\System32\mspaint.exe")

#-------------------------------------------------------------------------------------------------#

def ccleander():
    os.startfile("D:\CClea.5.41.Build.6446\ccleaner\CCleaner.exe")

#-------------------------------------------------------------------------------------------------#

def visual():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2015")

#-------------------------------------------------------------------------------------------------#

def visualcode():
    os.startfile("D:\MicrosoftVSCode\Code.exe")

#-------------------------------------------------------------------------------------------------#

def virtual():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Oracle VM VirtualBox\Oracle VM VirtualBox")

#-------------------------------------------------------------------------------------------------#
#The reason i use 2 history is because if Speak_Function(history) only will speak 2 times
def readnote():
    note = open("history.txt","r") #r is for read
    history = note.readable()

    history2 = note.read()
    Speak_Function("Last time you have noted down this")
    Speak_Function(history2)
    print(history2)
    note.close()


#-------------------------------------------------------------------------------------------------#

def writenote():
    Speak_Function("Preparing Note")
    Speak_Function("Preparing Complete")
    note = open("history.txt","w") #w is for Write

    note.writable()
    Speak_Function("Ready for you to write Sir")
    history = input("Your note: ")

    note.write(history)
    note.close()

#-------------------------------------------------------------------------------------------------#

def appendnote():
    note = open("history.txt","a") #a is for append
    note.writable()

    history = input("Extra thing:")

    note.write("\r" + history)
    note.close()

#-------------------------------------------------------------------------------------------------#