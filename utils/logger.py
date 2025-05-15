import json
import os
import datetime

DATA_DIR = r"C:\Users\sorok\Desktop\pet_cw\resources\saved_data"
DATA_FILE = os.path.join(DATA_DIR, "money_keeper_data.json")

def write_log():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    balance = data.get("balance", 0)
    date = datetime.datetime.now()

    log = {
        "balance":balance,
        "date":date
    }

    return log



