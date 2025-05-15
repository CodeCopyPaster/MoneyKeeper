from .local_save import load_data, save_data
from database.db_connect import connection
from database.requests import log_data

balance, salary, subscriptions = load_data()


def update_balance_label(balance_label):
    balance_label.config(text=f"YOUR BALANCE: {balance} ₽")


def add_money(amount, balance_label):
    global balance
    if amount.isdigit():
        balance += int(amount)
        update_balance_label(balance_label)
        save_data(balance, salary, subscriptions)
    log_data(connection)


def spend_money(amount, balance_label):
    global balance
    if amount.isdigit():
        cost = int(amount)
        if cost <= balance:
            balance -= cost
            update_balance_label(balance_label)
            save_data(balance, salary, subscriptions)
    log_data(connection)


def set_salary(amount, balance_label):
    global salary, balance
    if amount.isdigit():
        salary = int(amount)
        balance += salary
        update_balance_label(balance_label)
        save_data(balance, salary, subscriptions)
    log_data(connection)


def subscribe(cost, balance_label):
    global balance, subscriptions
    if cost.isdigit():
        cost = int(cost)
        if cost <= balance:
            balance -= cost
            subscriptions.append(cost)
            update_balance_label(balance_label)
            save_data(balance, salary, subscriptions)
    log_data(connection)