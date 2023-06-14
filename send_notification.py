import requests
from os import environ
from dotenv import load_dotenv
from collections import namedtuple
from send_email_context_manager import EmailContextManager

def send_telegram_message(message: str):
    load_dotenv()
    api_key = environ.get('API_KEY_TELEGRAM')
    userID = environ.get('USER_ID_TELEGRAM')
    # Create url
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    # Create json link with message
    data = {'chat_id': userID, 'text': message}
    # POST the message
    requests.post(url, data)

def send_email(text, subject):
    load_dotenv()
    reciver = environ.get('EMAIL')
    TEXT = text
    SUBJECT = subject
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT) 
    Credentials = namedtuple('credentials', 'username password')
    credentials = Credentials(environ.get('EMAIL'), environ.get('PASSWORD'))
    smtp_server = environ.get('SMTP_SERVER')
    port = environ.get('PORT')
    ssl_enable = environ.get('SSL_ENABLE')
    with EmailContextManager(smtp_server, port, ssl_enable, credentials) as server:
        server.login(credentials.username, credentials.password)
        server.sendmail(credentials.username, reciver, message.encode('utf-8'))
