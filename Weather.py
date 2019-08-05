#-------------------------------------------------------------------------------------------------#
import pyowm #Let her gather the weather report all around the world

#-------------------------------------------------------------------------------------------------#
owm = pyowm.OWM('a3ac1a7d13422b804a326029769907f2') #The Weather API

#-------------------------------------------------------------------------------------------------#

def Get_Weather(city):
    global Information,\
           weather,\
           status,\
           temperature,\
           humidity

    Information = owm.weather_at_place(city)
    weather = Information.get_weather()
    status = weather.get_status()
    temperature = weather.get_temperature('celsius')['temp']
    humidity = weather.get_humidity()

#-------------------------------------------------------------------------------------------------#

def Weather_Report(city):
   global status
   global temperature
   global humidity

   Get_Weather(city)

   return "The weather in "+city+\
          "\n. Paris now is "+status+\
          "\nIt has the temperature of "+str(temperature)+" degree Celsius "+\
          "\n and with the humidity of "+str(humidity)+" %"


#-------------------------------------------------------------------------------------------------#