import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")

miles = tk.Label(text="Miles").grid(column=2,row=0)

miles_num = tk.Entry()
miles_num.grid(column=1,row=0)


equal = tk.Label(text="is equal to").grid(column=0,row=1)
result = tk.Label(text="0")
result.grid(column=1,row=1)
km = tk.Label(text="km").grid(column=2,row=1)

def km_ml():
   miles = float(miles_num.get())
   result.config(text=str(miles/1.60934))

calc_btn = tk.Button(text="Calculate",command=km_ml).grid(column=1,row=2)

window.mainloop()