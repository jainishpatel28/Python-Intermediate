from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# take data from the entries put it in file, and after clicking Add wipe out the data from the form.
# use of file and delete function for wipe out

def add_entries():
    first_entry = website_entry.get()
    second_entry = username_entry.get()
    third_entry = password_entry.get()
    new_data = {
        first_entry: {
            "email": second_entry,
            "password": third_entry
        }
    }

    if len(first_entry) == 0 or len(third_entry) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=first_entry,
                                       message=f"These are the details entered: \nEmail: {second_entry}"
                                               f"\nPassword: {third_entry} \nIs it ok to save?")

        if is_ok:
            '''JSON file initializing and storing data, catching exceptions Error and read data into dictionaries.'''

            try:
                with open("storage.json", "r") as file:
                    # Reading old data:
                    data = json.load(file)
            except FileNotFoundError:
                with open("storage.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # updating old data with new data:
                data.update(new_data)
                with open("storage.json", "w") as file:  # need to open in write mode
                    # saving updated data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_to_search = website_entry.get()
    try:
        with open("storage.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website_to_search in data:
            email = data[website_to_search]["email"]
            password_p = data[website_to_search]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password_p}")
        else:
            messagebox.showinfo(title=website_to_search, message=f"No Details for {website_to_search} Exist." )

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pic)
canvas.grid(row=0, column=1)

# Label
website = Label(text="Website:")
website.grid(row=1, column=0)

username = Label(text="Email/Username:")
username.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "xyz@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
gene_pass = Button(text="Generate Password", command=generate_password)
gene_pass.grid(row=3, column=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

add = Button(text="Add", width=36, command=add_entries)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
