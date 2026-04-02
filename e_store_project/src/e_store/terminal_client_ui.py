import requests
from typing import Tuple

BASE_URL = "http://127.0.0.1:8007"

def get_balance(username:str)->float:
    return requests.get(f"{BASE_URL}/user/{username}/balance").json()["balance"]

def ask_credentials() ->Tuple[str,str]:
    username = input("Inserisci username: ").strip()
    password = input("Inserisci password: ").strip()
    return username, password

def run_client():
    print("Welcome to E-store (client/server) user interface")
    username , password = ask_credentials()

    while True:
       balance = get_balance(username)
        
    pass