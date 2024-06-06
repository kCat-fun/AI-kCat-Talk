import requests
import pyttsx3
import time
import os
from dotenv import load_dotenv

load_dotenv()

engine = pyttsx3.init()

url: str = "https://api-mebo.dev/api"
headers = {"content-type": "application/json"}

api_key: str = os.environ['API_KEY']
agent_id: str = os.environ['AGENT_ID']
uid: str = str(time.time())

while True:
    utterance: str = input("あなた    > ")

    item_data = {
        "api_key": api_key,
        "agent_id": agent_id,
        "utterance": utterance,
        "uid": uid,
    }

    r = requests.post(url, json=item_data, headers=headers)

    response = r.json()["bestResponse"]["utterance"]
    print("AI kCat君 > " + response)
    
    engine.say(response)
    engine.runAndWait()
