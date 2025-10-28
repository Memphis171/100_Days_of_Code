import tkinter
def button_clicked():
    print("Button was clicked")
    conversion = round(float(miles_value.get())*1.60934,2)
    km_value.configure(text=str(conversion))


window = tkinter.Tk()
window.title("Miles Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

miles_label = tkinter.Label(window, text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

miles_value = tkinter.Entry()
miles_value.grid(column=1, row=0)


km_label = tkinter.Label(window, text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

km_value = tkinter.Label(window, text = "0")
km_value.grid(column=1, row=1)
km_value.config(padx=20, pady=20)

is_equal_to_label = tkinter.Label(window, text="is equal to")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=20, pady=20)

calculate = tkinter.Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)
# calculate.config(padx=20, pady=20)

window.mainloop()