import os

import re

import time

class Config(object):

    # Get a bot token from botfather

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5261216654:AAG46xTHOKrqxlNaOtH07bHOhFwWDjqXJK8")

    # Get from my.telegram.org (or @UseTGXBot)

    API_ID = int(os.environ.get("API_ID", "19275737"))

    # Get from my.telegram.org (or @UseTGXBot)

    API_HASH = os.environ.get("API_HASH", "bdc37def5a44bc6a182db72d61a48192")

    

    

    # Database URL from https://cloud.mongodb.com/

    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://7559935673:7559935673@cluster0.3sajg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    # Your database name from mongoDB

    DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "LUCIFER V2.0"))

    # ID of users that can use the bot commands

    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "1126321077").split())

    # To save user details (Usefull for getting userinfo and total user counts)

    # May reduce filter capacity :(

    # Give yes or no

    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()

    # Go to https://dashboard.heroku.com/account, scroll down and press Reveal API

    # To check dyno status

    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

    # OPTIONAL - To set alternate BOT COMMANDS

    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")

    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")

    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")

    CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
    
    SESSION = os.environ.get("SESSION_STRING", "BQBXTxuK8ToKyWJ5kTYrXrDtx737whbhNw2OwdzDjvRbK66a0gVZ5him4JqvtUyNei_MNV694Q37giRvDHo74dw88mbXi8MxcmC6dWHoEWOceTSEGpFbFltytMqxRGtF0GyLz4IPF8Y8IOJLHlv5ac4rFsxd7BwHXGLS80o4OckuZELF1G68KbOo3rvJopzhAtE5QsGOWUUldKO3_ArOCsAkFuXzoo4mo5mk13ywMj5DWUnGn0Z30hsBLC7Ov-eamOe1yQjs4jAT-21N035sFmIOUDG5YZF1cGoaWMoNUvjlPYTTzq4HPzofbIWMvQyFsO8KLYAR8_tROmA_aBrV0I1hQyJLtQA")
   
    CHAT = os.environ.get("CHAT", "-1001545727220")

    LOG_GROUP = os.environ.get("LOG_GROUP", "-1001612651497")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None

    ADMIN = os.environ.get("ADMINS", "1126321077")

    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    
   
    

    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")

    # To record start time of bot

    BOT_START_TIME = time.time()




    STREAM_URL = os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")


    
   

   
  
