import tkinter as tk
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
import pandas as pd

websites = []
usernames = []
passwords = []


def add_credentials():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if website == "" or username == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username}\nPassword: {password}"
                                                  f"\nIs it okay to save?")
        if is_ok:
            websites.append(website)
            passwords.append(password)
            usernames.append(username)

            dictionary_password_manager = {"Website":websites, "Emails": usernames, "Password":passwords}
            df_passwords = pd.DataFrame(dictionary_password_manager)
            df_passwords.to_csv("data.csv",mode="a",index=False,header=False)

            website_entry.delete(0, last=tk.END)
            password_entry.delete(0, last=tk.END)





# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

lock = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200,bg="white", highlightthickness=0)
canvas.create_image(100,100,image=lock)

canvas.grid(row=0, column=1)

# website label UI
website_label = tk.Label(text="Website:", fg="black", bg="white")
website_label.grid(row=1, column=0)
website_entry = tk.Entry(width=38,bg="white",fg="black",highlightbackground="white")
website_entry.focus()
website_entry.grid(row=1, column=1,columnspan=2)

# username UI
username_label = tk.Label(text="Email/Username:", fg="black", bg="white")
username_label.grid(row=2, column=0)
username_entry = tk.Entry(width=38,bg="white",fg="black",highlightbackground="white")
username_entry.insert(0,"johnfmckissack@gmail.com")
username_entry.grid(row=2, column=1,columnspan=2)

#password UI
password_label = tk.Label(text="Password:", fg="black", bg="white")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=19,bg="white",fg="black",highlightbackground="white")
password_entry.grid(row=3, column=1)
password_button = tk.Button(text="Generate Password", width=15,highlightbackground="white",highlightthickness=0,command=generate_password)
password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add",width=36,highlightbackground="white",highlightthickness=0,command=add_credentials)
add_button.grid(row=4, column=1,columnspan=2)


window.mainloop()