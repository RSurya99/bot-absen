# Attendance Bot using Twilio Whatsapp

Attendance bot is a bot that used to manage attendance reports. This bot created using Flask, MySQL, and Twilio.

## Environment
Python 3.8 or above

## Installation

- Create virtualenv and run this command
    ```bash
    pip install requirements.txt
    ```

- Create the database and configure it in `App.py`
- Set the app to debug mode and run it
- For development, use ngrok to deploy it temporary and copy the url
- Paste the url in your twilio project and `App.py`

## Features
- attendance via whatsapp (only for registered user in database)