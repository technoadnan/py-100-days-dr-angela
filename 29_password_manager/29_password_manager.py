# # ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
# # ---------------------------- VARIABLES ------------------------------- #
data_dict = {}

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #

# # ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    with open("password.txt", mode="a") as file:
        file.write(f"{entry_website.get()} | {entry_email_uname.get()} | {entry_password.get()}\n")
        entry_website.delete(0, END)
        entry_password.delete(0, END)

# def save_pass():
#     data_dict[entry_website.get()] = [entry_email_uname.get(), entry_password.get()]
#     print(data_dict)



# # ---------------------------- UI SETUP ------------------------------- # 
 

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
 
canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)
 
label_website=Label(text="Website:")
label_website.grid(column=0, row=1)
 
entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)


entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")

 
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)
 
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")
 
generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3, sticky="EW")
 
add_btn = Button(text="Add", width=35, command=save_pass)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
 




mainloop()