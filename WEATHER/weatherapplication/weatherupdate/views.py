from datetime import datetime 
from django.http import HttpResponse 
from django.shortcuts import render 
import requests 
  
 # Create your views here. 
  
def index(request): 
     try: 
         if request.method == 'POST': 
             # Variables 
             city_name = request.POST.get('city') 
             API_KEY = 'f7ba43244f7d09c5b98830abcd423bf8' 
  
             # Adding variables into API 
             url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},tj&APPID={API_KEY}&units=metric' 
  
             response = requests.get(url).json() 
  
             # Getting current date and time 
             current_time = datetime.now() 
             formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p") 
  
             # Putting all data in a dictionary 
             city_weather_update = { 
                 'city': city_name, 
                 'description': response['weather'][0]['description'], 
                 'icon': response['weather'][0]['icon'], 
                 'temperature': 'Temperature: '+ str(response['main']['temp']) + ' C', 
                 'country_code': response['sys']['country'], 
                 'wind': 'Wind: '+ str(response['wind']['speed']) + ' KM/H', 
                 'humidity': 'Humidity: '+ str(response['main']['humidity']) + ' %', 
                 'time': formatted_time 
             } 
         else: 
             city_weather_update = {} 
  
         context = {'city_weather_update': city_weather_update} 
         return render(request, 'weatherupdates/home.html', context) 
      
     except: 
         return render(request, 'weatherupdates/404.html')