# Function
import datetime

from nltk.sem.chat80 import city

from listen import listen
from speak import Say
import requests

from weather import get_location, get_weather

# Define the get_latest_news function for news retrieval
NEWS_API_KEY = 'd555b4b9679646ccbbc51e59f1cc1913'


def get_latest_news():
    url = f'https://newsapi.org/v2/top-headlines?country=US&apiKey={"d555b4b9679646ccbbc51e59f1cc1913"}'
    response = requests.get(url)
    news_data = response.json()
    if 'articles' in news_data:
        articles = news_data['articles']
        for article in articles:
            title = article['title']
            description = article['description']
            Say(f"Title: {title}", city)
            Say(f"Description: {description}", city)


# 2 Types
# 1 - Non Input
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time, city)


def Date():
    date = datetime.date.today()
    Say(date, city)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day, city)


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()


# 2 - Input

def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("who is", "").replace("wikipedia", "").replace("what is", "").replace("about", "")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result, name)

    elif "google" in tag:
        query = str(query).replace("google", "").replace("search", "")
        import pywhatkit
        pywhatkit.search(query)

    elif "news" in tag:
        get_latest_news()

    elif "weather" in tag:
        city = get_location()
        api_key = "36aaa00e51fa8a07bf5e7c29524ad68e"
        weather_data = get_weather(api_key, city)

        if weather_data:
            weather_report = f"Current weather in {city}: {weather_data['main']}, {weather_data['description']}."
            weather_report += f" Temperature: {weather_data['temperature']}°C. Humidity: {weather_data['humidity']}%."
            Say(weather_report, city)

        else:
            Say("Failed to retrieve weather data for your location.", city)

    elif "email" in tag:
        Say("Please provide your email address.")
        email = listen()
        Say("Please provide the recipient's email address.")
        recipient = listen()
        Say("Please provide the email subject.")
        subject = listen()
        Say("Please provide the email message.")
        message = listen()
        import yagmail

        def send_email(recipient, subject, message, sender_email, sender_password):
            try:
                yag = yagmail.SMTP(sender_email, sender_password)
                yag.send(
                    to=recipient,
                    subject=subject,
                    contents=message
                )
                yag.close()
                print("Email sent successfully")
            except Exception as e:
                print("An error occurred while sending the email:", str(e))


    elif "whatsapp" in tag:
        Say("Please provide the recipient's WhatsApp number.")
        recipient = listen()
        Say("Please provide the WhatsApp message.")
        message = listen()
        from twilio.rest import Client

        def send_whatsapp_message(recipient, message, twilio_sid, twilio_token):
            try:
                client = Client(twilio_sid, twilio_token)
                from_whatsapp_number = "your_twilio_whatsapp_number"
                to_whatsapp_number = f"whatsapp:{recipient}"
                client.messages.create(body=message, from_=from_whatsapp_number, to=to_whatsapp_number)
                print("WhatsApp message sent successfully")
            except Exception as e:
                print("An error occurred while sending the WhatsApp message:", str(e))

