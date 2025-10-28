import tkinter
def button_clicked():
    print("Button was clicked")
    new_text = input.get()
    my_label.config(text = new_text)

window = tkinter.Tk()
window.title("My First GUI Program!")
window.minsize(width=500, height=300)
#add padding to your widgets
window.config(padx=20, pady=20)


#Label
my_label = tkinter.Label(window, text="I am a label.", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
#when you hover over pack there aren't any arguments that are showing up
#this is because there is this **kw


#button
button = tkinter.Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)

#button
new_button = tkinter.Button(text="Don't Click Me!", command=button_clicked)
new_button.grid(column=2, row=0)


#entry
input = tkinter.Entry()
input.grid(column=3, row=2)

window.mainloop()
