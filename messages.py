# Import necessary libraries and modules
import json

from Marvin import main
from brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
from listen import listen
from speak import Say
from task import InputExecution, NonInputExecution
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client

# Load the intents JSON
with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)


# Load your model and other data (similar to Marvin.py)
# ...

# Function to send an email
def send_email(to_email, subject, message, email, password):
    # Email configuration
    from_email = email  # Replace with your Gmail email
    app_password = password  # Replace with your Gmail App Password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Establish a connection to the SMTP server (Gmail's SMTP server)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, app_password)

    # Send the email
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)

    # Close the connection
    server.quit()
    Say("Email sent successfully.")


# Function to send a WhatsApp message
def send_whatsapp_message(to_number, message, sid, token):
    # Your Twilio credentials
    account_sid = 'SKc7dda14b98ef9f9b03d36d0fbfaab7eb'
    auth_token = 'm7xAdcIydvYVb0g06a10glatnjuVlSWN'
    twilio_number = '0705609602'

    client = Client(account_sid, auth_token)

    # Send the WhatsApp message
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=to_number
    )

    from nltk.sem.chat80 import city
    Say("WhatsApp message sent successfully.", city)


# Function to handle voice commands


while True:
    main()
