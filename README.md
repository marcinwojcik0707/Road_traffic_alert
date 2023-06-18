# Road_traffic_alert
Application to alert when traffic on route to work or to home is higher than usual.
- every day at defined time (used schedule library) program analyzes excel file with work schedule and checks which shift the employee will be working on
- if employee is working today and depending what shift was detect, scheduled is time when route have to be checked
- few minutes before travel, connection to google maps api is made and returned current time of travel
- if time of travel is longer than expected, traffic alert message is send to email and telegram aplication

Note that for the application to work properly, the user must create his own file with the .env extension. Enter inside this file code from below and fill in your own data:

API_KEY_MAPS = 
API_KEY_TELEGRAM =  
USER_ID_TELEGRAM = 
HOME_ADDRESS = 
WORK_ADDRESS = 
NORMAL_TIME_OF_TRAVEL = 
EMAIL = 
PASSWORD = 
SMTP_SERVER = 
PORT = 
SSL_ENABLE = 

-----------------
See distancematrix API guide for more information how to configure API_KEY_MAPS. Link: 
https://developers.google.com/maps/documentation/distance-matrix?hl=en

There is tutorial how to get and configurate your telegram KEY and USER_ID:
https://towardsdatascience.com/create-a-simple-bot-with-telegram-that-notifies-you-about-the-progress-of-your-code-69bab685b9db

NORMAL_TIME_OF_TRAVEL is a maximum time in minutes when application will not send you traffic alert message.
Examle of valid HOME_ADDRESS and WORK_ADDRESS: 'Warsaw, Wiejska 4'