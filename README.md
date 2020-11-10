# Bot-absen / Attendance-bot (experimental)

Attendance bot is a bot that used to manage attendance reports

## Requirement & Installation
Python 3.8 or above

create virtual environment using virtualenv

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the requirement.

```bash
pip install Twilio
pip install Flask
pip install SQLAlchemy
pip install pymysql

```

## Usage

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from twilio.twiml.messaging_response import MessagingResponse
from flask_sqlalchemy import SQLAlchemy
```

## Features
- attendance via whatsapp (only for specific subjects)
- attendance via web with face tracking (for daily attendance)
- attendace via android app (same function as web)
- data report and can be exported to excel

for point 2 until 4 still under development


## License
[MIT](https://choosealicense.com/licenses/mit/)
