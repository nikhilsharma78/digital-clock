import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")
def time():
    string = strftime("%H:%M:%S \n %p%D")
    label.config(text=string)
    label.after(1000,time)    

label = tk.Label(root,font=("arial",50,"bold"),background="black",foreground="lime")
label.pack(anchor="center")

time()

root.mainloop()