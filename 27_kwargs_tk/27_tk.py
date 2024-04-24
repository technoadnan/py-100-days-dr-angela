import tkinter as tk

window = tk.Tk()
window.title("My first GUI program")

my_label = tk.Label(text="New text")
my_label.pack()

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
    # my_label.config(new_text)

button = tk.Button(text="Click me",command=button_clicked)
button.pack()


input = tk.Entry(width=10)
input.pack()
print(input.get())



window.mainloop()
