import os, pyowm

owm = pyowm.OWM(os.environ['OPENWEATHER_API_KEY'])
observation = owm.weather_at_place(os.environ['CITY_NAME'])
weather= observation.get_weather()

print "source=openweathermap, city=\""+os.environ['CITY_NAME']+"\", description=\""+str(weather.get_detailed_status())+"\", temp="+str(weather.get_temperature(unit='celsius').values()[0])+", humidity="+str(weather.get_humidity())