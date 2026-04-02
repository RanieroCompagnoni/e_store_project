import requests
from typing import Tuple

BASE_URL = "http://127.0.0.1:8000"

def get_balance(username:str)->float:
    return requests.get(f"{BASE_URL}/user/{username}/balance").json()["balance"]

def ask_credentials() ->Tuple[str,str]:
    username = input("Inserisci username: ").strip()
    password = input("Inserisci password: ").strip()
    return username, password

def get_inventory() -> None:
    print("Store Inventory: ")
    inventory =  requests.get(f"{BASE_URL}/inventory").json()
    for item in inventory:
        print(f"{item["name"]} : {item["quantity"]} at price {item["price"]}")

def make_purchase(username: str, password: str, item_name: str, quantity : int) -> None:
    payload = {
        "username": username,
        "password": password,
        "item_name": item_name,
        "quantity": quantity
    }
    data = requests.post(f"{BASE_URL}/purchase", json=payload).json()
    print("Purchase successful!" if data.get("success") else "Purchase failed!")
    print(data.get("message"))

def run_client():
    print("Welcome to E-store (client/server) user interface")
    username , password = ask_credentials()

    while True:
        balance = get_balance(username)
        print(f"Your balance:{balance}")

        get_inventory()

        choice = input("Enter item to buy or 'quit' to exit : ").strip()
        if choice.lower()=="quit":
            print("Thank you for using the E-Store Client!")
            break
            
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
    
        make_purchase(username, password, choice, quantity)

if __name__=="__main__":
    run_client()