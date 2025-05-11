import tkinter as tk
from tkinter.ttk import Label
from PIL import Image, ImageTk
from tkinter import ttk, Entry
from utils.utils import (
    add_money,
    set_salary,
    spend_money,
    subscribe,
    balance,
    update_balance_label
)

"""" Digit validator """
def validate_number(new_value):
    return new_value == "" or new_value.isdigit()

""" Func to add subscription """
def subs_mon_window():
    global subs_window

    subs_window = tk.Toplevel(root)
    subs_window.title("Add subscription")
    subs_window.geometry("140x150")
    subs_window.resizable(width=False, height=False)

    vcmd = (subs_window.register(validate_number)), '%P'
    Label(subs_window, text="Введите стоимость подписки:").pack()

    number_entry = Entry(subs_window, validate='key', validatecommand=vcmd)
    number_entry.pack(pady=10)

    """"||| Add subscription button |||"""
    spend_money_btn = ttk.Button(
        subs_window,
        text="Set subs",
        command=lambda: subscribe(number_entry.get())
    )
    spend_money_btn.pack(pady=10)
    spend_money_btn.place(x=10,y=100)

""""========== Window for add spending =========="""
def spend_mon_window():
    global spend_window

    spend_window = tk.Toplevel(root)
    spend_window.title("Add spending")
    spend_window.geometry("140x150")
    spend_window.resizable(width=False,height=False)

    vcmd = (spend_window.register(validate_number)), '%P'
    Label(spend_window, text="Введите трату:").pack()

    number_entry = Entry(spend_window, validate='key', validatecommand=vcmd)
    number_entry.pack(pady=10)

    """"||| Add spend money button |||"""
    spend_money_btn = ttk.Button(
        spend_window,
        text="Set spending",
        command=lambda: spend_money(number_entry.get(), balance_label)
    )
    spend_money_btn.pack(pady=10)
    spend_money_btn.place(x=10,y=100)

""""========== Window for adding money to balance =========="""
def add_money_window():
    global add_mon_window

    add_mon_window = tk.Toplevel(root)
    add_mon_window.title("Add money")
    add_mon_window.geometry("140x150")
    add_mon_window.resizable(height=False, width=False)

    vcmd = (add_mon_window.register(validate_number), '%P')

    Label(add_mon_window, text="Введите число:").pack(pady=5)

    money_entry = Entry(add_mon_window, validate='key', validatecommand=vcmd)
    money_entry.pack(pady=5)

    """||| Add money button |||"""
    add_money_btn = ttk.Button(
        add_mon_window,
        text="Add money",
        command=lambda: add_money(money_entry.get(), balance_label)
    )
    add_money_btn.pack(pady=10)


""""========== Window for adding salary =========="""
def add_salary_window():
    global salary_window

    salary_window = tk.Toplevel(root)
    salary_window.title("Add salary")
    salary_window.geometry("140x150")
    salary_window.resizable(width=False,height=False)

    vcmd = (salary_window.register(validate_number)), '%P'
    Label(salary_window, text="Введите зарплату:").pack()

    number_entry = Entry(salary_window, validate='key', validatecommand=vcmd)
    number_entry.pack(pady=10)

    """"||| Add salary button |||"""
    add_salary_btn = ttk.Button(
        salary_window,
        text="Set salary",
        command=lambda: set_salary(number_entry.get())
    )
    add_salary_btn.pack(pady=10)
    add_salary_btn.place(x=10,y=100)

""""========== Window to create window with add money =========="""
def create_add_window():
    global add_window, bg_add_image


    def combine_set_salary():
        add_window.destroy()
        add_salary_window()

    def combine_add_money():
        add_window.destroy()
        add_money_window()


    add_window = tk.Toplevel(root)
    add_window.title("Add money")
    add_window.geometry("200x200")
    add_window.resizable(width=False,height=False)

    try:
        bg_add_image = Image.open("../resources/pics/bg_add_image.jpg")
        bg_add_image = ImageTk.PhotoImage(bg_add_image)

        bg_add_label = tk.Label(add_window, image=bg_add_image)
        bg_add_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        bg_add_label = tk.Label(add_window, bg="lightgray")
        bg_add_label.place(x=0,y=0,relwidth=1,relheight=1)

    """"||| Add salary button |||"""
    salary_btn = ttk.Button(
        add_window,
        text="Set salary",
        command=combine_set_salary

    )
    salary_btn.pack(pady=10)

    """"||| Add money button |||"""
    get_money_btn = ttk.Button(
        add_window,
        text="Getting money",
        command=combine_add_money

    )
    get_money_btn.pack(pady=10)

""""========== Window to create window with spend money =========="""


def create_spend_window():
    global spend_window, bg_spend_image

    spend_window = tk.Toplevel(root)
    spend_window.title("Spend money")
    spend_window.geometry("200x200")
    spend_window.resizable(width=False, height=False)

    try:
        bg_image = Image.open("../resources/pics/bg_spend_image.jpg")
        bg_photo = ImageTk.PhotoImage(bg_image)


        bg_spend_image = bg_photo

        bg_label = tk.Label(spend_window, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        #print(f"Error loading image: {e}")
        bg_label = tk.Label(spend_window, bg="lightgray")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)


    buttons_frame = tk.Frame(spend_window)
    buttons_frame.pack(pady=20)

    def combine_spend():
        spend_window.destroy()
        spend_mon_window()

    def combine_subs():
        spend_window.destroy()
        subs_mon_window()

    """"||| Spend money button |||"""
    spend_btn = ttk.Button(
        buttons_frame,
        text="Add spending",
        command=combine_spend
    )
    spend_btn.pack(pady=10)

    """"||| Add subscription button |||"""
    set_subscription_btn = ttk.Button(
        buttons_frame,
        text="Add subs",
        command=combine_subs
    )
    set_subscription_btn.pack(pady=10)


""""========== Main window for app =========="""
def main_window():


    global root
    root = tk.Tk()
    root.title("Money Keeper")
    root.geometry("440x600")
    root.resizable(width=False, height= False)



    bg_image = Image.open("../resources/pics/bg_image.png")
    bg_photo = ImageTk.PhotoImage(bg_image)


    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    """||| Balance Label |||"""
    global balance_label
    balance_label = tk.Label(
        root,
        text=f"YOUR BALANCE: {balance} ₽",
        font=("Arial", 16),
        bg="white"
    )
    balance_label.pack(pady=20)
    balance_label.place(x=100,y=80)

    add_button = ttk.Button(
        root,
        text="Add",
        command= create_add_window

    )
    add_button.pack(pady=20)
    add_button.place(x=110, y=450)

    spend_btn = ttk.Button(
        root,
        text="Spend",
        command= create_spend_window

    )
    spend_btn.pack(pady=20)
    spend_btn.place(x=220,y=450)

    root.mainloop()


if __name__ == '__main__':
   main_window()




    