import json
import os

DATA_DIR = r"C:\Users\sorok\Desktop\pet_cw\resources\saved_data"
DATA_FILE = os.path.join(DATA_DIR, "money_keeper_data.json")

""" Saves data into JSON"""
def save_data(balance, salary, subscriptions):
    data = {
        "balance": balance,
        "salary": salary,
        "subscriptions": subscriptions
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

""" Loads data from JSON"""
def load_data():
    if not os.path.exists(DATA_FILE):
        return 0, 0, []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        balance = data.get("balance", 0)
        salary = data.get("salary", 0)
        subscriptions = data.get("subscriptions", [])

        return balance, salary, subscriptions

    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")
        return 0, 0, []