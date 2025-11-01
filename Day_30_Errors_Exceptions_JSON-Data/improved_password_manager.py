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
import json

websites = []
usernames = []
passwords = []


def add_credentials():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "email": username,
            "password": password,
        }
    }
    def clear_entries():
        website_entry.delete(0, last=tk.END)
        password_entry.delete(0, last=tk.END)
    def update_existing_data():
        # this is how you write to a json file. use json.dump(). indent = 4 makes it easier for us to read
        with open("data.json", "r") as file:
            data = json.load(file)
            # the read file  is transformed into a python dictionary by json.load and
            # is then updated with the new data using [file variable].update([updated info variable in dict format])
            data.update(new_data)
        with open("data.json", "w") as file:
            # to update the json file with the updated info you need to reopen the  file in write mode and then json.dump()
            # the info in there to change the file
            json.dump(data, file, indent=4)
    def create_new_file():
        with open("data.json", "w") as new_file:
            json.dump(new_data, new_file, indent=4)

    if website == ""  or password == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username}"
                                                              f"\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            try:
                update_existing_data()
            except FileNotFoundError:
                create_new_file()
            finally:
                clear_entries()

def search_credentials():
    try:
        website = website_entry.get()
        with open("data.json", "r") as file:
           credentials = json.load(file)
        email = credentials[website]["email"]
        password = credentials[website]["password"]
        messagebox.showinfo(title=website, message=f"Here are your login credentials.\nEmail: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showerror("Error", "You do not have any saved passwords")
    except KeyError:
        messagebox.showerror("Error", "You have not saved a password for this website")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

lock = tk.PhotoImage(file="../Day_29_Password-Manager_GUI/logo.png")
canvas = tk.Canvas(width=200, height=200,bg="white", highlightthickness=0)
canvas.create_image(100,100,image=lock)

canvas.grid(row=0, column=1)

# website label UI
website_label = tk.Label(text="Website:", fg="black", bg="white")
website_label.grid(row=1, column=0)
website_entry = tk.Entry(width=19,bg="white",fg="black",highlightbackground="white")
website_entry.focus()
website_entry.grid(row=1, column=1)

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

search_button = tk.Button(text="Search",width=15,highlightbackground="white",highlightthickness=0,command=search_credentials)
search_button.grid(row=1, column=2)

window.mainloop()