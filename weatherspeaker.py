import requests
import os
import json
import win32com.client as wincom

city = input("Enter the name of the city")
url = f"https://api.weatherapi.com/v1/current.json?key=your key&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.SpVoice")
text = "The current weather in {city} is {w} degrees"
speak.Speak(text)