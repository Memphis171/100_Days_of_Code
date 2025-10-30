# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter as tk
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg="white")

lock = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200,bg="white", highlightthickness=0)
canvas.create_image(100,100,image=lock)

canvas.grid(row=0, column=1)

# website label UI
website_label = tk.Label(text="Website:", fg="black", bg="white")
website_label.grid(row=1, column=0)
website_entry = tk.Entry(width=38,bg="white",highlightthickness=0)
website_entry.grid(row=1, column=1,columnspan=2)

# username UI
username_label = tk.Label(text="Email/Username:", fg="black", bg="white")
username_label.grid(row=2, column=0)
username_entry = tk.Entry(width=38,bg="white",highlightthickness=0)
username_entry.grid(row=2, column=1,columnspan=2)

#password UI
password_label = tk.Label(text="Password:", fg="black", bg="white")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=19,bg="white",highlightthickness=0)
password_entry.grid(row=3, column=1)
password_button = tk.Button(text="Generate Password", width=15,highlightbackground="white",highlightthickness=0)
password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add",width=36,highlightbackground="white",highlightthickness=0)
add_button.grid(row=4, column=1,columnspan=2)


window.mainloop()