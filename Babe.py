# -------------------------------------------------------------------------------------------------#

#Import all the module for the Project

import pyttsx3  #for speaking function

import time #for time

import datetime #to get hour minute thing

import Applications #Use everything in the Application.py

import  Firefox #Use everything in the Firefox.py

import Weather  #Use everything in the Weather.py

import BasicServer #Use everything in the Server.py

import Gmail #Use everything in the Gmail.py

import Youtube #Use eveything in the Youtube.py

import Facebook #Use everything in the Facebook.py

import News #Use everything in the News.py

#------------------------------------------------------------------------------------------------#
#Set up different kind of voice ( 0: male; 1:mature woman; 2:woman but younger than num 1
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#---------------------------------------------------------------------------------------------------#

#this is just a nick name ( convert this you will get the author )
def Me():
    print("010010000100100001001000		010010000100100001001000")
    print("001100110011001100110011		001100110011001100110011")
    print("00110000001100000011000000110000001100000011000000110000")
    print("01001110010011100100111001001110010011100100111001001110")
    print("010000000100000001000000		010000000100000001000000")
    print("001100010011000100110001		001100010011000100110001")
    print("*!* " *10)

#---------------------------------------------------------------------------------------------------#

#Create a function to let her speak
def Speak_Function(text):
    engine.say(text)
    engine.runAndWait()

#---------------------------------------------------------------------------------------------------#

#Create a function to let user write code
def phrase():
        Text_Input = input("Your order: ")
        return Text_Input

#---------------------------------------------------------------------------------------------------#

#Create a funcion to let her recognize admin
def Login_Successful():
    Speak_Function("Hearbroken-Exhausted-Outcast-Numb-Alone-Incomplete")
    Speak_Function("Acknowledged")
    Speak_Function("Welcome Back Sir!")

    print(local_time)
    Speak_Function("it's" + local_time)
    Speak_Function("How may i help you? ")

    Me()
    print("\n#  H30NA1 is waiting for your order ")

#---------------------------------------------------------------------------------------------------#

#create a function to let her open app but based on the choice of the user
def Open_Application():
    while 1:
        App_Name = input("Application Name: \n"
                         "1. NotePad \n"
                         "2. Paint \n"
                         "3. Calculator \n"
                         "4. MS Word \n"
                         "5. MS Excel \n"
                         "6. MS PowerPoint"
                         "7. Ccleaner \n"
                         "8. Visual Studio Code \n" 
                         "9. Visual Studio \n"
                         "10. Virtual Box \n"
                         "99. Exit \n"
                         "Your Order: ")


        if App_Name == "99":
            Speak_Function("Understood Sir!")
            break;
            string = phrase()

        # ---------------------------------------------------------------------------------------------------#

        elif App_Name == "3":
            Speak_Function("Acknowledged Opening Calculator")
            Applications.calculator()

        # -------------------------------------------------------------------------------------------------#

        elif App_Name == "1":
            Speak_Function("Acknowledged Opening Note Pad")
            Applications.notepad()

        # -------------------------------------------------------------------------------------------------#

        elif App_Name == "4":
            Speak_Function("Acknowledged Opening Microsoft Word")
            Applications.msword()

        # -------------------------------------------------------------------------------------------------#

        elif App_Name == "5":
            Speak_Function("Acknowledged Opening Microsoft Excel")
            Applications.msexcel()

        # -------------------------------------------------------------------------------------------------#

        elif App_Name == "6":
            Speak_Function("Acknowledged Opening Microsoft PowerPoint")
            Applications.msppt()

        # -------------------------------------------------------------------------------------------------#

        elif App_Name == "2":
            Speak_Function("Acknowledged Opening Microsoft Paint")
            Applications.mspaint()

        # -------------------------------------------------------------------------------------------------#

        elif App_Name == "7":
            Speak_Function("Acknowledged Opening CCleaner")
            Applications.ccleander()

        # -------------------------------------------------------------------------------------------------#

        elif App_Name == "8":
            Speak_Function("Acknowledged Opening Visual Studio Code")
            Applications.visualcode()

        # -------------------------------------------------------------------------------------------------#

        elif  App_Name == "9":
            Speak_Function("Acknowledged Opening Visual Studio ")
            Applications.visual()

        # -------------------------------------------------------------------------------------------------#

        elif  App_Name == "10":
            Speak_Function("Acknowledged Opening Virtual Box")
            Applications.virtual()

#-------------------------------------------------------------------------------------------------------#

#Set up time
local_time = time.asctime(time.localtime())
Present_Time = datetime.datetime.now()
Presennt_Hour = Present_Time.hour

#---------------------------------------------------------------------------------------------------------#

#This is where she will introduce herself
Speak_Function("Welcome!")
Speak_Function("My Name is H30NA1")
Speak_Function("I'm programmed to be Voice Assistant for Desktop")
Speak_Function("Now may i ask who are you ?")

#---------------------------------------------------------------------------------------------------------#

#The guest have to input the  name and password for her
User = input("User: ")
Password = input("Password: ")

#If User match, she will trigger the function
if User == "HeoNai" and Password == "H4000N@@@@1":
    Login_Successful()

#if not she will continue to ask the guest to input again
else:
    Speak_Function("Error! Wrong Input ! Preparing ShutDown System")
    Speak_Function("Be Careful ! You only have 4 chances left")
    count = 4

    #We have to use different string, if you use only 1 string( User), she will say double
    User2 = input("User2: ")
    Password2 = input("Password2: ")

    if User2 == "HeoNai" and Password2 == "H4000N@@@@1":
       Login_Successful()
    else:
        while User2 != "HeoNai" or Password2 != "H4000N@@@@1":

            count = int(count) - 1
            Speak_Function("Try Again! You only have " + str(count) + "Chances left")
            User2 = input("User: ")
            Password2 = input("Password2: ")

            if count == 2:
                Speak_Function("Initiating ShutDown System")
                Speak_Function("Now you only have 1 chance left!")
                User3 = input("User(This is you last warning): ")
                Password3 = input("Password(This is you last warning): ")

                if User3 == "HeoNai" and Password3 == "H4000N@@@@1":
                    Login_Successful()
                    break

                else:
                    Speak_Function("Sorry ! But i can't let anyone except my master use me")
                    Speak_Function("Initiate ShutDown System complete")
                    Speak_Function("Login out Now")
                    exit(1)

#-----------------------------------------------------------------------------------------------#

#Create a loop command so it doesn't exit when finish a command
while 1: #while 1 is while true
    string = phrase()  #we create a variable and match it with the function phrase for easy to be triggered out

#----------------------------------------------------------------------------------------------#

    #This is simple time-asking question
    if string == "hello" or string == "hi":
        if Presennt_Hour >= 5 and Presennt_Hour < 13:
            Speak_Function("Morning Sir ! How are you today")

        elif Presennt_Hour >= 13 and Presennt_Hour < 18:
            Speak_Function("Hello Sir! It's already Afternoon ! You need to take a nap")

        elif Presennt_Hour >= 18 and Presennt_Hour <= 22:
            Speak_Function("Good Evening Sir ! Let's Have some fun before go to sleep")

        else:
            Speak_Function("Hello Sir ! It's already late ! You should get some rest")

#-------------------------------------------------------------------------------------------------#

    elif string == "how are you" or string == "Are you OK":
        Speak_Function("I'm feeling like a new person today sir, How about you?")

# -------------------------------------------------------------------------------------------------#

    elif string == "babe are you there" or string == "babe you there":
        Speak_Function("Yes Sir,I'm here! Ready for your order ")

# -------------------------------------------------------------------------------------------------#

    elif string == "what time is it" or string == "tell me the time":
        print(Present_Time)
        Speak_Function(Present_Time)

# -------------------------------------------------------------------------------------------------#

    #This string will let her trigger the library weather.py
    elif string == "weather" or string == "Weather mode":
        Speak_Function("Changing to Weather Mode! Ready for your Order !")
        while 1:
            city = input("City:")
            # ---------------------------------------------------------------------------------------------------------#
            if city =="exit":
                Speak_Function("Understood Sir! ")
                break;
                string = phrase()

            # ---------------------------------------------------------------------------------------------------------#
            else:
                Speak_Function("Updating Weather report")
                Speak_Function("Updating Complete! ")
                report = Weather.Weather_Report(city)

                print(report + "\n")
                Speak_Function(report)

# -------------------------------------------------------------------------------------------------#

    elif string == "Nice Job" or string == "nice" or string == "good" or string == "Good":
        Speak_Function("Thanks Sir !I will contribute more for you")

# -------------------------------------------------------------------------------------------------#

    #This will create a note for the admin and will be triggered back when he log in again
    elif string == "history" or string == "what did i do the last time" or string == "What happened yesterday":
        Speak_Function("Preparing Note")
        Speak_Function("Preparing Complete")
        Applications.readnote()

# -------------------------------------------------------------------------------------------------#

    elif string == "great" or string == "nice" or string == "fine" or string == "good" or string == "ok" or string == "okay" or string == "alright" or string == "cool":
        Speak_Function("Good to hear that, Sir!")

# -------------------------------------------------------------------------------------------------#

    elif string == "I'm tired"or string == "not so well" or string == "upset" or string == "sleepy":
        Speak_Function("Don't worry Sir! i will light up your mood ")
        Speak_Function("Searching for something can help with " + string)
        Speak_Function("Searching complete")

        if string == "I'm tired":
            Speak_Function("I'm sure this will make you feel energetic again sir")
            Youtube.YTfortired()

        elif string == "not so well":
            Speak_Function("I'm sure this will make you feel better again sir")
            Youtube.YTfornotsowell()

        elif string == "sleepy":
            Speak_Function("I'm sure this will make you feel awake sir")
            Youtube.YTforsleepy()

        elif string == "upset":
            Speak_Function("I'm sure this will ease your anger sir")
            Youtube.YTforupset()

# -------------------------------------------------------------------------------------------------#

    #This will let her trigger the open_Software function
    elif string == "Open Software":
        Speak_Function("Can you tell me the name of that software sir ?")
        Open_Application()

# -------------------------------------------------------------------------------------------------#

    #This will let her trigger the Firefox.py
    elif string == "Open Firefox" or string == "Firefox" or string == "Launch Firefox":

        Speak_Function("Understood!!!")
        Speak_Function("What do you want me to do Sir!")
        while 1:
            job = input("Action: \n"
                        "1: Search \n"
                        "2: Join \n"
                        "99:Exit \n"
                        "Your order: ")
            # ---------------------------------------------------------------------------------------------------------#
            if job == "1":

                Speak_Function("Changing to Search mode! Ready for your order")
                while 1:
                    word = input("Search for: ")
                    if word == "Exit" or word =="finish":
                        Speak_Function("Understood Sir!")
                        break
                        job = input("Action: ")
                    else:
                        Speak_Function("Searching for anything related to " + word)
                        Firefox.search(word)

            # ---------------------------------------------------------------------------------------------------------#
            elif job == "2":
                Speak_Function("Ready for your order! ")

                while 1:
                    word = input("The website: \n"
                                 "1: FaceBook \n"
                                 "2: Gmail \n"
                                 "3: Youtube \n"
                                 "4: Instagram \n" 
                                 "99:Exit \n"
                                 "Your Order: " )
                    # ---------------------------------------------------------------------------------------------------------#
                    if word == "99":
                        Speak_Function("Understood Sir!")
                        break
                        job = input("Action: ")

                    # ---------------------------------------------------------------------------------------------------------#
                    else:
                        if word == "1":
                            Firefox.joinFB()

                        # ---------------------------------------------------------------------------------------------------------#
                        elif word == "2":
                            Firefox.joinGmail()

                        # ---------------------------------------------------------------------------------------------------------#
                        elif word == "3":
                            Firefox.joinYT()

                        # ---------------------------------------------------------------------------------------------------------#
                        elif word == "4":
                            Firefox.joinIS()

            # ---------------------------------------------------------------------------------------------------------#
            elif job == "99":
                Speak_Function("Understood Sir!")
                break;
                string = phrase()

# -------------------------------------------------------------------------------------------------#
    #This is just for entertainment only :)
    elif string == "let's have some fun" or string == "attack mode" or string == "fun time":

        Speak_Function("Understood Sir! Changing to Attack Mode")
        Speak_Function("Who is the target sir")
        while 1:
            ip = input("The user IP: ")
            # ---------------------------------------------------------------------------------------------------------#
            if ip == "exit":
                Speak_Function("Understood Sir")
                break;
                string = phrase()

            # ---------------------------------------------------------------------------------------------------------#
            else:
                Speak_Function("Understood Sir! Searching for " + ip)
                Speak_Function("Searching Complete!")
                Speak_Function("Connecting to " + ip)
                BasicServer.main()

# -------------------------------------------------------------------------------------------------#

    #Everytime we want to log out , she will ask for a note
    elif string == "Bye" or string == "Break" or string == "Log off" or string == "Night babe ":
        Speak_Function("Understood Sir! Do you want to take note of something for later use ?")
        choose = input("Your choice: \n"
                       "1: Yes \n"
                       "2: No \n"
                       "Your order: ")
        # ---------------------------------------------------------------------------------------------------------#
        if choose == "1":
            Applications.writenote()
            Speak_Function("Is that all sir")
            choice = input("Your Choice: \n"
                           "1: Yes \n"
                           "2: No \n"
                           "Your Order: ")

         # ---------------------------------------------------------------------------------------------------------#
            if choice == "2":
                Applications.appendnote()
                exit(0)

            # ---------------------------------------------------------------------------------------------------------#
            elif choice == "1":
                exit(0)

        # ---------------------------------------------------------------------------------------------------------#
        elif choose == "2":
            Speak_Function("Understood Sir! See You Again")
            exit(0)

# -----------------------------------------------------------------------------------------------#--

    elif string == "gmail" or string == "Gmail":
        Speak_Function("Understood! Do you want me to send message for you?")
        choose = input("Your choice: \n"
                       "1: Yes \n"
                       "2: No \n"
                       "Your order: ")

        # ---------------------------------------------------------------------------------------------------------#
        if choose == "1":
            Speak_Function("Which type sir: ")
            while 1:
                type = input("Type of the email: \n  1: Spam \n"
                                                 "2: Normal \n"
                                                 "99:Exit \n"
                                                 "Your Order: ")

                # ---------------------------------------------------------------------------------------------------------#
                if type == "2":
                    Gmail.Send_Gmail()

                # ---------------------------------------------------------------------------------------------------------#
                elif type == "1":
                    Speak_Function("Which kind sir: ")
                    kind = input("1: One \n"
                                 "2: Multiple \n"
                                 "99:Exit \n"
                                 "Your Order: ")

                    # ---------------------------------------------------------------------------------------------------------#
                    if kind == "1":
                        Gmail.E_BombForOne()
                        # ---------------------------------------------------------------------------------------------------------#
                    elif kind == "2":
                        Gmail.E_BombForMultiple()
                        # ---------------------------------------------------------------------------------------------------------#
                    elif kind == "99":
                        type = input("Type of the email \n 1: Spam \n"
                                                         "2: Normal \n"
                                                         "99:Exit  \n"
                                                         "Your Order: ")

                        # ---------------------------------------------------------------------------------------------------------#
                else:
                    Speak_Function("Understood Sir")
                    break;
                    string = phrase()

        # ---------------------------------------------------------------------------------------------------------#
        #If user don't want to automate send, she will open Gmail website for user
        elif choose == "2":
            Firefox.joinGmail()

# -----------------------------------------------------------------------------------------------#--

    #She will trigger the Youtube.py
    elif string == "youtube" or string == "Youtube":
        Speak_Function("Understood ! Do you want me to search the video for you sir ?")
        types = input("Your choice: \n"
                      "1: Yes \n"
                      "2: No \n"
                      "Your Order: ")

        # ---------------------------------------------------------------------------------------------------------#
        if types == "1":
            while 1:
                Speak_Function("Understood ! Can you tell me the name of the video ")
                name = input("Name of the video: ")
                # ---------------------------------------------------------------------------------------------------------#
                if name == "exit" or name == "finish":
                    Speak_Function("Understood Sir")
                    break
                    string = phrase()

                    # ---------------------------------------------------------------------------------------------------------#
                else:
                    Speak_Function("Understood ! Opening Youtube with result of" + name)
                    Youtube.YTSearch(name)

        # ---------------------------------------------------------------------------------------------------------#
        elif type == "2":
             Firefox.joinYT()

# -----------------------------------------------------------------------------------------------#--
    #She will trigger the Facebook.py
    if string == "facebook" or string == "FaceBook":
        Speak_Function("Understood Sir! Do you want me to log in Facebook for you ")
        choose = input("Your choice: \n"
                       "1: Yes \n"
                       "2: No \n"
                       "Your Order: ")
        # ---------------------------------------------------------------------------------------------------------#
        if choose == "1":
            Facebook.Facebook()

        # ---------------------------------------------------------------------------------------------------------#
        elif choose == "2":
            Speak_Function("Understood! Opening Face Book")
            Firefox.joinFB()

# -----------------------------------------------------------------------------------------------#--

    #She will trigger the News.py
    elif string == "update me":
        Speak_Function("Understood Sir! Here are all the new today ")
        News.GetNews()

# -----------------------------------------------------------------------------------------------#--

