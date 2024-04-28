# # ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# # ---------------------------- SEARCH ------------------------------- #


def find_password():
    website = entry_website.get()
    try:
        with open("password.json", "r") as file:
            data = json.load(file)
            # print(data[website])
            if website in data:
                d = data[website]
                print(d["password"])
                messagebox.askokcancel(
                    title="Message", message=f"\nWebsite: {website}\n password: {d['password']}\n")
            else:
                print("No details for the website exist")

    except json.JSONDecodeError:
        messagebox.showwarning(
            title="Message", message=f"No data file found!!!")


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    l = [random.choice(letters) for _ in range(random.randint(8, 10))]
    s = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    n = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password = "".join(l+s+n)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# # ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = entry_website.get()

    email = entry_email_uname.get()
    password = entry_password.get()

    # Try and exception
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    print(new_data)

    if ((len(website) == 0 or len(password) == 0)):
        messagebox.askokcancel(
            title="ERROR", message=f"Please don't left any field empty")
    else:
        # is_ok = messagebox.askokcancel(
        #     title=website, message=f"These are the details entered: \nEmail: {email}\n password: {password}\n Is is ok to save?")
        # if is_ok:
        # with open("password.txt", mode="a") as file:
        #     file.write(f"{entry_website.get()} | {entry_email_uname.get()} | {entry_password.get()}\n")
        #     entry_website.delete(0, END)
        #     entry_password.delete(0, END)

        # DAY 30
        try:
            with open("password.json", "r") as file:
                data = json.load(file)
        # raise JSONDecodeError("Expecting value", s, err.value) from None json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
        except FileNotFoundError or json.JSONDecodeError:
            with open("password.json", "w") as file:
                file.write('''{}''')
        finally:

            with open("password.json", "r") as file1:
                data = json.load(file1)
                data.update(new_data)

            with open("password.json", "w") as file2:
                json.dump(data, file2, indent=4)


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="EW")

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=save_pass)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")


mainloop()
