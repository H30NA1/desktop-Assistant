# -------------------------------------------------------------------------------------------------#

import pyttsx3
from email.mime.text import MIMEText #This is the library will let her get scrap the gmail page and use the function
import smtplib

# -------------------------------------------------------------------------------------------------#

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# -------------------------------------------------------------------------------------------------#

def Speak_Function(text):
    engine.say(text)
    engine.runAndWait()

# -------------------------------------------------------------------------------------------------#

def Send_Gmail():
    Speak_Function("What's the story sir?")
    message = MIMEText(input("Write everything you want to say: ")) #this will be the message

    Speak_Function("What is the topic sir?")
    message["Subject"] = input("Topic: ") #This will get the "Subject" keyword and attack the input to it

    Speak_Function("Who is target sir?")
    message["To"] = input("Receiver:  ") #This will get the "To" keyword and attack the input to it

    Speak_Function("Can i have your account sir ?")
    message [ "From" ] = input("The email: ") #This will get the "From" keyword and attack the input to it
    passwd = input("The password: ")

    email = smtplib.SMTP('smtp.gmail.com',587) #must use port 587 for her to easy delivery mail without restric
    email.starttls()
    email.login(message["From"], passwd)
    email.sendmail(message["From"], message["To"], message.as_string())

# -------------------------------------------------------------------------------------------------#

def E_BombForOne():
    count = 0
    times_limit = 10

    # -------------------------------------------------------------------------------------------------#
    Speak_Function("What is the message sir ?")
    message = MIMEText(input("Message 1: "))

    Speak_Function("What is the topic Sir? ")
    message [ "Subject" ] = input("Topic 1: ")

    Speak_Function("Who is the target Sir ? ")
    message [ "To" ] = input("Target 1: ")

    Speak_Function("Can i have your account sir? ")
    message [ "From" ] = input("The email: ")
    passwd = input("The password: ")


    # -------------------------------------------------------------------------------------------------#

    Speak_Function("What is the message sir ?")
    message2 = MIMEText(input("Message 2: "))

    Speak_Function("What is the topic Sir? ")
    message2 [ "Subject" ] = input("Topic 2: ")

    message2 [ "To" ] =  message [ "To" ]

    Speak_Function("Can i have your account sir? ")
    message2 [ "From" ] = input("The email: ")
    passwd2 = input("The password: ")

 # -------------------------------------------------------------------------------------------------#

    while count != times_limit:

        email = smtplib.SMTP("smtp.gmail.com:587")
        email.starttls()
        email.login(message [ "From" ] , passwd)
        email.sendmail(message [ "From" ] , message [ "To" ] , message.as_string())

        # -------------------------------------------------------------------------------------------------#

        email2 = smtplib.SMTP("smtp.gmail.com:587")
        email2.starttls()
        email2.login(message2 [ "From" ] , passwd2)
        email2.sendmail(message2 [ "From" ] , message2 [ "To" ] , message2.as_string())

        # -------------------------------------------------------------------------------------------------#
        count += 1

        if count == times_limit:
            break

# -------------------------------------------------------------------------------------------------#

def E_BombForMultiple():
    count = 0
    times_limit = 99

    # -------------------------------------------------------------------------------------------------#
    Speak_Function("What is the message sir ?")
    message = MIMEText(input("Message 1: "))

    Speak_Function("What is the topic Sir? ")
    message [ "Subject" ] = input("Topic 1: ")

    Speak_Function("Who is the target sir? ")
    message [ "To" ] = input("Target 1: ")

    Speak_Function("Can i have your account sir? ")
    message [ "From" ] = input("The email")
    passwd = input("The password: ")

    # -------------------------------------------------------------------------------------------------#

    Speak_Function("What is the second message sir?")
    message2 = MIMEText(input("Message 2: "))

    Speak_Function("What is the topic Sir?")
    message2 [ "Subject" ] = input("Topic 2: ")

    Speak_Function("Who is the target sir? ")
    message2 [ "To" ] = input("Target 2:")
    message2 [ "From" ] = message [ "From" ]

    # -------------------------------------------------------------------------------------------------#


    while count != times_limit:

        email = smtplib.SMTP("smtp.gmail.com:587")
        email.starttls()
        email.login(message [ "From" ] , passwd)
        email.sendmail(message [ "From" ] , message [ "To" ] , message.as_string())
        # -------------------------------------------------------------------------------------------------#

        email2 = smtplib.SMTP("smtp.gmail.com:587")
        email2.starttls()
        email2.login(message2 [ "From" ] , passwd)
        email2.sendmail(message2 [ "From" ] , message2 [ "To" ] , message2.as_string())

        # -------------------------------------------------------------------------------------------------#

        count += 1

        if count == times_limit:
            break

# -------------------------------------------------------------------------------------------------#