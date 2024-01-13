from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)


# Label Creation
miles = Label(text="Miles", font=("Arial", 18, "normal"))
miles.grid(column=2, row=0)

equal = Label(text="is equal to", font=("Arial", 18, "normal"))
equal.grid(column=0, row=1)

km = Label(text="Km", font=("Arial", 18, "normal"))
km.grid(column=2, row=1)

result = Label(text="0", font=("Arial", 20, "bold"))
result.grid(column=1, row=1)



# Entry Creation
input = Entry(width=20)
input.grid(column=1, row=0)


# Button Creation
def on_command():   
    miles_entered = float(input.get())
    final = round(miles_entered * 1.690, 2)
    result["text"] = f"{final}"

button = Button(text="Calculate", command=on_command)
button.grid(column=1, row=2)






window.mainloop()
