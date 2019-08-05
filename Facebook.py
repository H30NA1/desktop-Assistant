# -------------------------------------------------------------------------------------------------#

from selenium import webdriver

import pyttsx3

# -------------------------------------------------------------------------------------------------#

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# -------------------------------------------------------------------------------------------------#

def Speak_Function(text):
    engine.say(text)
    engine.runAndWait()

# -------------------------------------------------------------------------------------------------#

def Facebook():
    Speak_Function("which account sir?")
    email = input("Email: ")

    if email == "koscielny1@yahoo.com.vn":
        passwd = "H4000N@@@@1"
        Speak_Function("Understood ! Log into FaceBook")
        url = webdriver.Firefox()
        url.get("https://www.facebook.com/")

        user = url.find_element_by_css_selector("#email")
        user.clear()
        user.send_keys(email)

        user = url.find_element_by_css_selector("#pass")
        user.clear()
        user.send_keys(passwd)

        login_btn = url.find_element_by_id("u_0_2")
        login_btn.click()
        Speak_Function("Log in Complete! Want me to search for you ?")
        choose = input("Your choice: ")

        if choose == "Yes" or choose == "Y":
            while 1:
                word = input("Search about: ")
                search = url.find_element_by_class_name("_1frb")
                search.clear()
                search.send_keys(word)
                search.submit()
                if word == "exit":
                    exit("facebook")
# -------------------------------------------------------------------------------------------------#

