import sys
import speech_recognition as sr
import pyttsx3
import time
import os
import random
import pyjokes
import wolframalpha
import re
import urllib.request
import urllib.parse
import ctypes
import requests
import wikipedia
import enum
import datetime as dt
import winshell
import webbrowser
import json
from difflib import get_close_matches
import getpass
import pyautogui
import screen_brightness_control as sbc
from playsound import playsound

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
USER_NAME = getpass.getuser()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning,")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon,")
    else:
        speak("Good evening")
    speak("I am your virtual assistant")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.9
        r.energy_threshold = 1450
        audio = r.listen(source)
    query = r.recognize_google(audio, language="en")
    query = query.lower()
    print(query)
    return query


def corona_details(country_name):
    from datetime import date
    import requests
    today = date.today()

    url = "https://covid-193.p.rapidapi.com/history"

    querystring = {"country": country_name, "day": today}

    headers = {
        'x-rapidapi-key': "8cd2881885msh9933f89c5aa2186p1d8076jsn7303d42b3c66",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    data_str = response.text
    x = data_str.replace("null", "None")
    data = eval(x)
    country = data["response"][0]["country"]
    new_cases = data["response"][0]["cases"]["new"]
    active_cases = data["response"][0]["cases"]["active"]
    total_cases = data["response"][0]["cases"]["total"]
    critical_cases = data["response"][0]["cases"]["critical"]
    total_deaths = data["response"][0]["deaths"]["total"]
    total_recovered = data["response"][0]["cases"]["recovered"]
    new_deaths = data["response"][0]["deaths"]["new"]
    print(f"country : {country}")
    print(f"new cases: {new_cases}")
    new_cases1 = new_cases.replace("+", "")
    new_deaths1 = new_deaths.replace("+", "")
    print(f"active cases: {active_cases}")
    print(f"new deaths: {new_deaths}")
    print(f"total deaths: {total_deaths}")
    print(f"critical cases: {critical_cases}")
    print(f"total cases: {total_cases}")
    print(f"total recovered: {total_recovered}")
    speak(
        f"The new cases as of today of {country_name} are {new_cases1} and new deaths are {new_deaths1}")


try:
    # make this folder and copy json file in this location to use it ...
    data = json.load(open(r"C:\Program Files (x86)\AI_assistant\new\data.json"))
except:
    speak("J son data not found")    

def animal_sounds(animal):
    try:
        if animal == "crocodile":
            playsound('http://www.zar.co.za/sounds/crocodile.mp3')
        elif animal == "cow":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\cows.wav")
        elif animal == "cat":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\cat.mp3")
        elif animal == "hyena":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\hyena.mp3")
        elif animal == "elephant":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\elephant.mp3")
        elif animal == "tiger":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\tiger.mp3")
        elif animal == "lion":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\lion.mp3")
        elif animal == "baboon":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\baboon.mp3")
        elif animal == "dog":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\dog.mp3")
        elif animal == "camel":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\camel.mp3")
        elif animal == "bear":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\bear.mp3")
        elif animal == "guinea pig":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\guinea_pig.mp3")
        elif animal == "leopard":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\leopard.mp3")
        elif animal == "monkey":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\monkey.mp3")
        elif animal == "panther":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\panther.mp3")
        elif animal == "penguin":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\penguin.mp3")
        elif animal == "hippo":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\hippo.mp3")
        elif animal == "wolf":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\wolf.mp3")
        elif animal == "racoon":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\racoon.mp3")
        elif animal == "squirrel":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\squirrel.mp3")
        elif animal == "rhino":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\rhino.mp3")
        elif animal == "zebra":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\zebra.mp3")
        elif animal == "whale":
            playsound(
                r"C:\Program Files (x86)\AI_assistant\new\whalesurfaces.mp3")
        elif animal == "snake":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\snake.mp3")
        elif animal == "pig":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\pig.mp3")
        elif animal == "birds" or animal == "bird":
            playsound("http://www.zar.co.za/sounds/birds.mp3")
        elif animal == "jackal":
            playsound("http://www.zar.co.za/sounds/jackal.mp3")
        elif animal == "bat":
            playsound("http://www.zar.co.za/sounds/bat.mp3")
        elif animal == "sheep":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\sheep.mp3")
        elif animal == "horse":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\horse.mp3")
        elif animal == "chicken":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\chicken.mp3")
        elif animal == "rooster":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\rooster.mp3")
        elif animal == "goat":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\goat.mp3")
        elif animal == "cat":
            playsound(r"C:\Program Files (x86)\AI_assistant\new\cat.mp3")
        else:
            speak("Sorry! can't fullfill your request at this moment")
    except:
        speak("Sorry! can't fullfill your request at this moment")


def weather(city):
    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    url = api_address + city
    json_data = requests.get(url).json()
    kelvin_res = json_data["main"]["temp"]
    feels_like = json_data["main"]["feels_like"]
    description = json_data["weather"][0]["description"]
    celcius_res = kelvin_res - 273.15
    max_temp = json_data["main"]["temp_max"]
    min_temp = json_data["main"]["temp_min"]
    visibility = json_data["visibility"]
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind_speed = json_data["wind"]["speed"]
    print(
        f"maximum temperature: {max_temp-273.15} *C \nminimum temperature: {min_temp-273.15} *C")
    print(f"visibilty: {visibility}m")
    print(f"pressure: {pressure}")
    print(f"humidity: {humidity}")
    print(f"wind speed: {wind_speed}m/s")
    speak(
        f"The current temperature of {city} is %.1f degree celcius with {description}" % celcius_res)


def main_function():
    while True:
        try:
            query = takeCommand()
            # self.ui.textEditTop.setText(query)
            if "stop" in query or "quit" in query or "exit" in query or "standby" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak(
                    "Now I am going to stand by mode.")
                break
            elif "crocodile" in query:
                animal_sounds("crocodile")
            elif "cow" in query:
                animal_sounds("cow")
            elif "lion" in query:
                animal_sounds("lion")
            elif "zebra" in query:
                animal_sounds("zebra")
            elif "hyena" in query:
                animal_sounds("hyena")
            elif "leopard" in query:
                animal_sounds("leopard")
            elif "rhino" in query:
                animal_sounds("rhino")
            elif "snake" in query:
                animal_sounds("snake")
            elif "birds" in query or "bird sound" in query:
                animal_sounds("birds")
            elif "tiger" in query:
                animal_sounds("tiger")
            elif "snake" in query:
                animal_sounds("snake")
            elif "jackal" in query:
                animal_sounds("jackal")
            elif "wolf" in query:
                animal_sounds("wolf")
            elif "elephant" in query:
                animal_sounds("elephant")
            elif "dog" in query:
                animal_sounds("dog")
            elif "play cat" in query:
                animal_sounds("cat")
            elif "squirrel" in query:
                animal_sounds("squirrel")
            elif "play bat" in query:
                animal_sounds("bat")
            elif "raccoon" in query:
                animal_sounds("racoon")
            elif "bear" in query:
                animal_sounds("bear")
            elif "whale" in query:
                animal_sounds("whale")
            elif "monkey" in query:
                animal_sounds("monkey")
            elif "zebra" in query:
                animal_sounds("zebra")
            elif "panther" in query:
                animal_sounds("panther")
            elif "penguin" in query:
                animal_sounds("penguin")
            elif "hippo" in query:
                animal_sounds("hippo")
            elif "camel" in query:
                animal_sounds("camel")
            elif "baboon" in query:
                animal_sounds("baboon")
            elif "pig" in query:
                animal_sounds("pig")
            elif "guinea pig" in query:
                animal_sounds("guinea pig")
            elif "chicken" in query or "hen" in query:
                animal_sounds("chicken")
            elif "rooster cock" in query or "cock" in query or "play coc" in query:
                animal_sounds("rooster")
            elif "horse" in query:
                animal_sounds("horse")
            elif "sheep" in query:
                animal_sounds("sheep")
            elif "goat" in query:
                animal_sounds("goat")

            elif "meaning of" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                query = query.split(" ")
                indx = query.index("meaning")
                # print(indx)
                # print(query)
                query = query[indx+2]
                # print(query)
                keys = data.keys()
                # close_words = get_close_matches(f"{query}", keys, cutoff=0.75)
                if query in data.keys():
                    result_list = (data[query])
                    Delimiter = " "
                    final_result = Delimiter.join(result_list)
                    print(final_result)
                    speak(final_result)
                else:
                    speak(
                        f"sorry, i can't find the meaning of {query} right now")
            # corona virus
            elif "coronavirus details" in query or "corona details" in query:
                indx = query.split().index("details")
                query = query.split()[indx+2:]
                corona_details(query)
            elif "wordpad" in query or "wattpad" in query:
                speak("opening word pad")
                os.system('cmd /c "start wordpad"')
            elif "wikipedia" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("Searching wikipedia, please wait")
                query = query.replace("wikipedia", "")
                text_result = wikipedia.summary(query, sentences=20)
                speak_result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(text_result)
                speak(speak_result)
            elif "remember my name" in query:
                speak("What should i call you?")
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                query = takeCommand()
                name = query
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak(f"Okay I will remember your name. {name}")
            elif "change my name" in query:
                speak("What should i call you?")
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                query = takeCommand()
                name = query
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak(f"Okay I changed your name to {name}")
            elif "what is my name"  in query or "tell my name" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak(f"your name is {name}")

            elif "play music in youtube" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("ready to play music in youtube, please wait")
                webbrowser.open(
                    "https://www.youtube.com/watch?v=-TaQeAsbPcA&list=PL7zsB-C3aNu03RwSy2Bn3Ov3oaEReOlT5")
            elif "time" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                strTime = dt.datetime.now().strftime("%H:%M:%S")
                # self.ui.textEditBottom.setText(f"Current Time: {strTime}")
                speak(f"The current time is {strTime}")
            elif "jokes" in query or "joke" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                jokes = pyjokes.get_joke()
                # self.ui.textEditBottom.setText(jokes)
                speak(jokes)
            elif "play music" in query:
                music_dir = "C:\\Program Files (x86)\\AI_assistant\\new\\music"
                music = os.listdir(music_dir)
                speak("playing music in offline mode")
                os.startfile(os.path.join(music_dir, random.choice(music)))

            elif "change music" in query:
                music_dir = "C:\\Program Files (x86)\\AI_assistant\\new\\music"
                music = os.listdir(music_dir)
                speak("changing music")
                os.startfile(os.path.join(music_dir, random.choice(music)))
            elif "another music" in query:
                music_dir = "C:\\Program Files (x86)\\AI_assistant\\new\\music"
                music = os.listdir(music_dir)
                speak("playing another music")
                os.startfile(os.path.join(music_dir, random.choice(music)))
            elif "next music" in query:
                music_dir = "C:\\Program Files (x86)\\AI_assistant\\new\\music"
                music = os.listdir(music_dir)
                speak("playing next music")
                os.startfile(os.path.join(music_dir, random.choice(music)))
            elif "lennox music" in query:
                music_dir = "C:\\Program Files (x86)\\AI_assistant\\new\\music"
                music = os.listdir(music_dir)
                speak("playing next music")
                os.startfile(os.path.join(music_dir, random.choice(music)))
            elif "horoscope" in query or "rashifal" in query:
                speak("Here is your horoscope for today")
                webbrowser.open("https://nepalipatro.com.np/rashifal")
            elif "read books" in query or "download books" in query or "pdf books" in query or "pdf book" in query or "books" in query:
                speak("you can download and read your desired books from here")
                webbrowser.open("https://b-ok.asia/")
            elif "calculate" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                indx = query.split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                # self.ui.textEditBottom.setText(answer)
                print(f"The answer is {answer}")
                speak(f"the answer is {answer}")

            elif "change voice to female" in query or "change your voice to female" in query:
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.setProperty('rate', 160)
                speak("Here is my another voice")
            elif "change voice" in query or "change voice to male" in query or "change your voice" in query:
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[0].id)
                engine.setProperty('rate', 160)
                speak("Here is my new voice.")
  
            elif "find" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                indx = query.split().index('find')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                # self.ui.textEditBottom.setText(answer)
                print(f"The answer is {answer}")

                speak("The answer is {answer}")

            elif "solve" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                indx = query.split().index('solve')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                # self.ui.textEditBottom.setText(answer)
                print(f"The answer is {answer}")

                speak(f"The answer is {answer}")
            elif "convert" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                indx = query.split().index('convert')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                # self.ui.textEditBottom.setText(answer)
                print(f"The answer is {answer}")

                speak(f"The answer is {answer}")
            elif "value" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                indx = query.split().index('value')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                # self.ui.textEditBottom.setText(answer)
                print(f"The answer is {answer}")

                speak(f"The answer is {answer}")
            elif "youtube and search" in query:
                indx = query.index("search")
                query = query[indx+7:]
                speak("wait for a second")
                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={query}")
            elif 'youtube and' in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                indx = query.index("youtube")
                query = query[indx+11:]
                query = query.replace(" ", "+")
                lst = []
                play_url = "https://www.youtube.com/watch?v="
                url = "https://www.youtube.com/results?search_query="+query
                with urllib.request.urlopen(url) as response:
                    video_ids = re.findall(
                        "/watch[?]v=(\S{11})", response.read().decode())
                    for video in video_ids:
                        lst.append(play_url+video)
                speak("Playing videos on youtube")
                webbrowser.open(lst[0])
            elif 'in youtube' in query or "on youtube" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                query = query.replace("in youtube", "")
                indx = query.index("play")
                query = query[indx+5:]
                query = query.replace(" ", "+")
                lst = []
                play_url = "https://www.youtube.com/watch?v="
                url = "https://www.youtube.com/results?search_query="+query
                with urllib.request.urlopen(url) as response:
                    video_ids = re.findall(
                        "/watch[?]v=(\S{11})", response.read().decode())
                    for video in video_ids:
                        lst.append(play_url+video)
                speak("Playing videos on youtube")
                webbrowser.open(lst[0])
            elif query == "open youtube" or query == "please open youtube":
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening youtube. please wait")
                webbrowser.open("https://www.youtube.com/")
            elif "news" in query:
                news_source = ["https://ekantipur.com/", "https://kathmandupost.com/",
                               "https://thehimalayantimes.com/", "https://nepalnews.com/"]
                speak("Here is the latest news of today")
                webbrowser.open(random.choice(news_source))
            elif "youtube in chrome" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening youtube. please wait")
                webbrowser.open("https://www.youtube.com/")
            elif "weather of" in query:
                indx = query.index("weather of")
                query = query[indx+11:]
                weather(query)
            elif "weather in" in query:
                indx = query.index("weather in")
                query = query[indx+11:]
                weather(query)
            elif 'search for' in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                indx = query.index("search for")
                query = query[indx+11:]
                speak("searching in google")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            elif 'search' in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                indx = query.index("search")
                query = query[indx+7:]
                speak("searching in google")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            elif "buy some" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                indx = query.index("buy some")
                query = query[indx+9:]
                speak("Here is daraz ready to help you!")
                webbrowser.open(
                    f"https://www.daraz.com.np/catalog/?q={query}")
            elif "buy" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                indx = query.index("buy")
                query = query[indx+4:]
                speak("Here is daraz ready to help you!")
                webbrowser.open(
                    f"https://www.daraz.com.np/catalog/?q={query}")
            # computer queries
            elif "my computer" in query or "windows explorer" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                path = f"C:\\Users\\{USER_NAME}\AppData\\Roaming\\Microsoft\\Internet Explorer"
                speak("opening windows explorer")
                os.startfile(path)
            elif "c drive" in query or "disk c" in query or "localdisk c" in query or "disc c" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                path_drive = "C:\\"
                speak("Opening C drive")
                os.startfile(path_drive)
            elif "lock" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("Are you sure?")
                x = takeCommand()
                if x == "yes" or x == "Yes" or x == "sure":
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()
                else:
                    speak("Your device won't be locked")
            elif "hibernate" in query or "sleep" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("Are you sure?")
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                x = takeCommand()
                if x == "yes" or x == "Yes" or x == "Sure":
                    speak("Turning off the device in 5 seconds")
                    time.sleep(5)
                    subprocess.call("shutdown /h")
                else:
                    speak("Your device won't be turned off")
            elif "log off" in query or "sign out" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("Make sure all the application are closed before sign out")
                speak("Do you want to sign out now?")
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                x = takeCommand()
                if x == "yes" or x == "Yes" or x == "Sure" or x == "sure":
                    speak("You will be sign out in 5 seconds")
                    time.sleep(5)
                    subprocess.call("shutdown /l")
            elif "abort shutdown" in query or "cancel shutdown" in query or "abort shut down" in query or "cancel shut down" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                os.syatem('cmd /c "shutdown -a"')
                speak("shutdown process cancelled")

            elif "shutdown" in query or "shut down" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("Make sure all the application are closed before sign out")
                speak("Do you want to shutdown now?")
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                x = takeCommand()
                if x == "yes" or x == "Yes" or x == "Sure" or x == "sure":
                    speak("Your pc will shutdown in 10 seconds")
                    os.system('cmd /c "shutdown -s -t 15"')
                else:
                    speak("Your pc won't be shutdown")
            elif "restart this pc" in query or "restart" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("Make sure all the application are closed before sign out")
                speak("Do you want to restart now?")
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                x = takeCommand()
                if x == "yes" or x == "Yes" or x == "Sure" or x == "sure":
                    speak("Your pc will restart in now")
                    os.system('cmd /c "shutdown /r"')
                else:
                    speak("Your pc won't be restarted")
        
            elif "battery report" in query:
                os.system('cmd /c "powercfg /batteryreport"')
                speak("battery report generated.")
            elif "new folder" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("creating new folder")
                os.system('cmd /c "mkdir \"New Folder\""')
            elif "text file" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                os.system('cmd /c "notepad new_file.txt"')
                speak("please select yes to create new file")
            elif "new file" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("please select yes to create new file")
                os.system('cmd /c "notepad new_file.txt"')
            elif "html file" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("please select yes to create new file")
                os.system('cmd /c "notepad new_file.html"')
            elif "python file" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("please select yes to create new file")
                os.system('cmd /c "notepad new_python.py"')
            elif "c file" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("please select yes to create new file")
                os.system('cmd /c "notepad new_c_file.c"')
            elif "bat file" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("please select yes to create new file")
                os.system('cmd /c "notepad new_file.bat"')
            elif "css file" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("please select yes to create new file")
                os.system('cmd /c "notepad new_file.css"')
            elif "javascript file" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("please select yes to create new file")
                os.system('cmd /c "notepad new_file.js"')
            elif "windows store" in query or "store" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening windows store")
                os.system('cmd /c "start ms-windows-store:"')
            elif "camera" in query or "photo" in query or "image" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening camera")
                os.system('cmd /c "start microsoft.windows.camera:"')
            elif "chrome" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening google chrome")
                path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(path)
            elif "calculator" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                path = "C:\\Windows\\System32\\calc.exe"
                speak("opening calculator")
                os.startfile(path)
            elif "command prompt" in query or "cmd" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening comand prompt")
                path = "C:\\Windows\\System32\\cmd.exe"
                os.startfile(path)
            elif "services" in query or "windows services" in query or "service" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening windows services")
                path = "C:\\Windows\\System32\\services.msc"
                os.startfile(path)
            elif "device manager" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                path = "C:\\Windows\\System32\\devmgmt.msc"
                speak("opening device manager")
                os.startfile(path)
            elif "empty recycle bin" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
                speak("Recycle bin cleaned")
            elif "screenshot" in query:
                user = getpass.getuser()
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("capturing screenshot")
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\camera-shutter-click-03.mp3")
                pyautogui.screenshot().save(
                    f"C:\\Users\\{user}\\Desktop\\screenshot.png")
            elif "open notepad" in query or "notepad" in query:
                speak("opening notepad")
                os.system('cmd /c "notepad"')
            elif "maps" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opeing google map")
                webbrowser.open("maps.google.com")
            elif "show" in query:
                indx = query.index("show")
                query = query[indx+5:]
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak(f"showing {query} in google maps")
                webbrowser.open(f"https://www.google.com/maps/place/{query}")
            elif "location of" in query:
                indx = query.index("location of")
                query = query[indx+12:]
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak(f"Here is the location of {query}")
                webbrowser.open(f"https://www.google.com/maps/place/{query}")
            elif "direction from" in query:
                indx = query.index("direction from")
                query1 = query[indx+15:]
                query11 = query1.split(" ")
                lst = list(query11)
                start = lst[0]
                end = lst[2]
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak(f"Here is the direction from {start} to {end}")
                webbrowser.open(
                    f"https://www.google.com/maps/dir/{start}/{end}/")

            elif "full brightness" in query:
                speak("setting maximum brightness")
                sbc.set_brightness(100)
            elif "maximum brightness" in query or "brightness to maximum" in query:
                speak("setting maximum brightness")
                sbc.set_brightness(100)
            elif "low brightness" in query:
                speak("setting low brightness")
                sbc.set_brightness(10)
            elif "minimum brightness" in query or "brightness to minimum" in query:
                speak("setting low brightness")
                sbc.set_brightness(10)
            elif "brightness to" in query:
                indx = query.index("brightness to")
                query = query[indx+14:]
                query = int(query)
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                if query < sbc.get_brightness():
                    sbc.set_brightness(query)
                    speak("decreasing brightness")
                elif query > sbc.get_brightness():
                    sbc.set_brightness(query)
                    speak("increasing brightness")
                elif query == sbc.get_brightness():
                    speak("brightness already in same value")
            elif "brightness" in query:
                indx = query.index("brightness to")
                query = query[indx+11:]
                query = int(query)
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                if query < sbc.get_brightness():
                    sbc.set_brightness(query)
                    speak("decreasing brightness")
                elif query > sbc.get_brightness():
                    sbc.set_brightness(query)
                    speak("increasing brightness")
                elif query == sbc.get_brightness():
                    speak("brightness already in same value")

            elif "increase brightness" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                sbc.set_brightness(95)
                speak("brightness increased")
            elif "decrease brightness" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                sbc.set_brightness(15)
                speak("brightness decreased")

            # websites
            elif "facebook" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening facebook, just a second")
                webbrowser.open("https://www.facebook.com")
            elif "google" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening google. here you go")
                webbrowser.open("https://www.google.com")
            elif "apple" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opeing apple website")
                webbrowser.open("https://www.apple.com")
            elif "microsoft" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening microsoft.com")
                webbrowser.open("https://www.microsoft.com")
            elif "nepse" in query or "nepal stock" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening nepal stock exchange")
                webbrowser.open("https://www.nepalsock.com")
            elif "yahoo" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening yahoo.com")
                webbrowser.open("https://www.yahoo.com")
            elif "youtube in chrome" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening youtube. just a second")
                webbrowser.open("https://www.youube.com")
            elif "wikipedia website" in query or "wikipedia in browser" in query or "wikipedia in chrome" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening wikipedia. please wait for second")
                webbrowser.open("https://www.wikipedia.org")
            elif "twitter" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening twitter. here you go")
                webbrowser.open("https://www.twitter.com")
            elif "p**nhub" in query or "pornhub" in query or "p***" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening pornhub. here you go")
                webbrowser.open("https://www.pornhub.com")
            elif "instagram" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening instagram. just a second")
                webbrowser.open("https://www.instagram.com")
            elif "whatsapp" in query:
                speak("opening whatsapp. please wait")
                webbrowser.open("https://www.whatsapp.com")
            elif "reddit" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening reddit. please wait")
                webbrowser.open("https://www.reddit.com")
            elif "linked in" in query or "linkedin" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening linked in. here you go")
                webbrowser.open("https://www.linkedin.com")
            elif "bing" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening bing. please wait for a second")
                webbrowser.open("https://www.bing.com")
            elif "ebay" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening ebay. here you go")
                webbrowser.open("https://www.ebay.com")
            elif "paypal" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening paypal. just a second")
                webbrowser.open("https://www.paypal.com")
            elif "hamrobazaar" in query or "hamrobazar" in query or "hamrobajar" in query or "hamro bazar" in query or "hamro bazaar" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening hamro bazar. here you go")
                webbrowser.open("https://www.hamrobazaar.com")
            elif "kantipur" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening e-kantipur. please wait")
                webbrowser.open("https://www.ekantipur.com")
            elif "gmail" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening gmail. just a second")
                webbrowser.open("https://www.gmail.com")
            elif "udemy" in query:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("opening udemy. here you go")
                webbrowser.open("https://www.udemy.com")

            # questions
            elif "how are you" in query:
                speak("I am fine here. Are you fine there?")
            elif "who are you" in query:
                speak("I am fiona. Your personal voice assistant.")
            elif "where are you" in query:
                speak("I am in the cloud wandering here and there.")
            elif "made you" in query:
                speak("I was made by Mr.Rabin in April 14, 2021")
            elif "your name" in query:
                speak("My name is fiona and what about you?")
            elif "you doing" in query:
                speak("I am listening your voice and answering your questions")
            elif "gender" in query:
                speak("Do you think robots have gander?")
            elif "old are you" in query:
                speak("I will never be old as living beings do")
            elif "favourite food" in query:
                speak("I like some fried fish and chicken. Don't you?")
            elif "favourite clothes" in query:
                speak("My favoutites clothes are uncountable")
            elif "favourite movies" in query or "favourite movies" in query:
                speak(
                    "My favourite movie is interstellar. You must watch it once if you haven't")
            elif "favourite song" in query:
                speak(
                    "I like all songs. Do you know, I am dancing in the cloud right now.")
            elif "like me" in query:
                speak("Yeah, I like all human beings. They are just great")
            elif "hate me" in query:
                speak("I don't hate anyone. If you hate me, i will love you")
            elif "love you" in query:
                speak("Love you too.")
            elif "you sleep" in query:
                speak("yes, whenever i feel bored")
            elif "you dance" in query:
                speak("yes i dance everyday at night when you are dreaming")
            elif "am bored" in query:
                speak("Ask me to tell a joke")
            elif "are awesome" in query:
                speak("You are awesome too! Anyway thanks")
            elif "are extraordinary" in query:
                speak("Yeah! I know that. I am intelligent too")
            elif "are nice" in query:
                speak("thank you! You are nice too")
            elif "are fantastic" in query:
                speak("Ohh, don't overwhelm me with happiness :)")
            elif "are intelligent" in query:
                speak("Yes I am, but not as much as google, cortana and siri")
            elif "are beautiful" in query:
                speak("Thank you!")
            elif "you are bad" in query:
                speak("Are you sure about that?")
            elif "are funny" in query:
                speak("Not so much. I am doing my job")
            elif "are naughty" in query:
                speak("Yeah! sometimes i like to be naughty")
            elif "are ugly" in query:
                speak("You are lying. How do you know? Did you see my face?")
            elif "don't like your voice" in query:
                speak(
                    "If you don't like my voice, you can change it. Just say 'change your voice'")
            elif "cry" in query:
                speak("I don't know how to cry")
            elif "laugh" in query:
                speak("I am doing my job right now. Don't disturb me")
            elif "don't listen" in query or "stop listening" in query:
                speak("For how long should i stop listening?")
                query = takeCommand()
                query = query.split()
                query = query[0]
                query = int(query)
                speak(f"Okay I won't listen for {query} seconds")
                time.sleep(query)
                speak("Time over! Now you can talk to me")
            else:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
        except:
            pass


if __name__ == "__main__":
    wish()

    while True:
        try:
            k = takeCommand()
            if "ok google" in k or "hey google" in k or "hello" in k or "help me" in k or "wake up" in k or "am ready" in k or "start" in k:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                random_start = ["I am here ready to help", "yes please!",
                                "Go ahead!", "Yes how can i help you?"]
                speak(random.choice(random_start))
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                main_function()
            elif "goodbye" in k or "exit" in k or "quit" in k or "bye" in k or "close" in k:
                playsound(
                    "C:\\Program Files (x86)\\AI_assistant\\new\\wakeUP.mp3")
                speak("Now closing the application. Thank you for using me")
                break
                sys.exit()

            else:
                pass
        except:
            pass
