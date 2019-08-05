# -------------------------------------------------------------------------------------------------#
import webbrowser   #Let her auto open default website

from selenium import webdriver  #Let her auto use firefox for login and send email

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

def search(word):
    url = "https://duckduckgo.com/"
    webbrowser.open_new_tab(url+word)

# -------------------------------------------------------------------------------------------------#

def Advance_search(word):
    url = "https://duckduckgo.com/"
    webbrowser.open_new_tab(url + word)

    word2 = word
    url2 = ("https://www.facebook.com/search/top/?q="+ word2 +"&epa=SEARCH_BOX" )
    webbrowser.open_new_tab(url2)

    word3 = word
    url3 = ("https://www.instagram.com/" + word3)
    webbrowser.open_new_tab(url3)

    word4 = word
    url4 = ("https://www.linkedin.com/pub/dir/" + word4)
    webbrowser.open_new_tab(url4)

# -------------------------------------------------------------------------------------------------#

def joinFB():
    url = "https://www.facebook.com/"
    webbrowser.open_new_tab(url)

# -------------------------------------------------------------------------------------------------#

def joinYT():
    url = "https://www.youtube.com/"
    webbrowser.open_new_tab(url)

# -------------------------------------------------------------------------------------------------#

def joinIS():
    url = "https://www.instagram.com/"
    webbrowser.open_new_tab(url)

# -------------------------------------------------------------------------------------------------#

def joinGmail():
    url = "https://www.google.com/intl/vi/gmail/about/"
    webbrowser.open_new_tab(url)

# -------------------------------------------------------------------------------------------------#

