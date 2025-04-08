import tkinter as tk
from tkinter.ttk import Label
from PIL import Image, ImageTk
from tkinter import ttk, PhotoImage


def add_salary_window():
    """
        Func to enter salary
    :return:
    """

    #global salary_window
    salary_window = tk.Toplevel(root)
    salary_window.title("Add salary")
    salary_window.geometry("400x300")

    label_info = tk.Label(salary_window,text="Input here ur salary per month")


def create_add_window():
    """
        Func create new window with 2 buttons to add salary/money
    :return: none
    """

    def combine_set_salary():
        add_window.destroy()
        add_salary_window()


    add_window = tk.Toplevel(root)
    add_window.title("Add money")
    add_window.geometry("200x200")

    salary_btn = ttk.Button(
        add_window,
        text="Set salary",
        command=combine_set_salary
    )
    salary_btn.pack(pady=10)


    get_money_btn = ttk.Button(
        add_window,
        text="Getting money",
        command=lambda: print("Нажата кнопка 2")
    )
    get_money_btn.pack(pady=10)



def main_window():
    """
        Func for  main window
    :return:
    """
    global root
    root = tk.Tk()
    root.title("Money Keeper")
    root.geometry("440x600")
    root.resizable(width=False, height= False)


    bg_image = Image.open("../resources/pics/bg_image.png")
    bg_photo = ImageTk.PhotoImage(bg_image)


    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    add_button = ttk.Button(
        root,
        text="Add",
        command= create_add_window
    )
    add_button.pack(pady=20)
    add_button.place(x=110, y=450)

    spend_btn = ttk.Button(
        root,
        text="Spend"
        # command=
    )
    spend_btn.pack(pady=20)
    spend_btn.place(x=220,y=450)

    root.mainloop()


if __name__ == '__main__':
   main_window()




    