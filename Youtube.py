# -------------------------------------------------------------------------------------------------#
import webbrowser

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

def YTSearch(word):
    url = "https://www.youtube.com/results?search_query="
    webbrowser.open_new_tab(url+word)

# -------------------------------------------------------------------------------------------------#

def YTfortired():
    url = "https://www.youtube.com/watch?v=c7rCyll5AeY"
    webbrowser.open_new_tab(url)

# -------------------------------------------------------------------------------------------------#

def YTforsleepy():
    url = "https://www.youtube.com/watch?v=8A2t_tAjMz8&list=RDePpPVE-GGJw&index=10"
    webbrowser.open_new_tab(url)

# -------------------------------------------------------------------------------------------------#

def YTforupset():
    url = "https://www.youtube.com/watch?v=V2hlQkVJZhE&list=RDePpPVE-GGJw&index=18"
    webbrowser.open_new_tab(url)

# -------------------------------------------------------------------------------------------------#

def YTfornotsowell():
    url = "https://www.youtube.com/watch?v=rRzxEiBLQCA"
    webbrowser.open_new_tab(url)

# -------------------------------------------------------------------------------------------------#