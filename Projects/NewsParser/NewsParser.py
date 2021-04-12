from bs4 import BeautifulSoup
import requests
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


source = requests.get("https://www.indiatoday.in/news.html").text
soup = BeautifulSoup(source, "lxml")

speak("Here Are Your Top Three News Of The Day")
print("Here Are Your Top Three News Of The Day:")

for headlines in soup.find_all("h3", class_="news-page-feature"):
    for t in headlines.find_all("a", href=True, text=True):
        head = t.text
        link = t["href"]

        print("\n")
        speak(head)
        print(head + ":")
        print(f"https://www.indiatoday.in{link}")

