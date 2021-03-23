import requests
import os
from datetime import datetime

user_api = "f4f0a5439d1dd0c9a2eb878dddfca7bc"
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
#print(api_data)

temp_city =((api_data['main']['temp'])-273.15)
weather=api_data['weather'][0]['description']
wind=api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather)
#print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind ,'kmph')
