import time
import config
import helpers as Helper
import reels,poster,shorts,remover
from instagrapi import Client
import auth
from rich import print
from datetime import datetime, timedelta
import random


Helper.load_all_config()

api = auth.login()

while True:
       
        print("[green] Posting Reel [/green]")
        poster.main(api)
