#Importing Modules
import requests
import json
import pyttsx3
import time
import os

# Main Code
if __name__=="__main__":
    print("--------WELCOME TO THE WEATHER TALKI CREATED BY MUZAMAL ALI--------")
    engine = pyttsx3.init()
    engine.setProperty('rate',150) #Managing the speed of Speak Assistant
    message = "WELCOME TO THE WEATHER TALKI CREATED BY MUZAMAL ALI"
    engine.say(message)
    engine.runAndWait()
    while True:
        message = "PLEASE ENTER THE CITY AND COUNTRY CODE: "
        engine.say(message)
        engine.runAndWait()
        countryCode = input("Enter the country code: ")
        city = input("Enter name of the city: ")
        # Error Handling
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{countryCode}&APPID=ba3c4ef27610a035f7a0144e1b25c55c"
            if(city == "q" or countryCode =="q"):
                break
            else:
                response = requests.get(url)
                dictionary = json.loads(response.text)
                temprature = dictionary['main']['temp']
                temprature = int(temprature) - 273.15
                temprature = round(temprature,2)
                print(f"Temprature of {city} is: {temprature}°C")
                engine.say(f"Temprature of {city} is: {temprature} degree celcius")
                engine.runAndWait()
                time.sleep(3)
                os.system('cls')
        except:
            engine.say("PLEASE ENTER VALID COUNTRY CODE OR CITY")
            engine.runAndWait()
            os.system('cls')