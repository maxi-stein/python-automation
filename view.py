import tkinter as tk
from tkinter import filedialog
import sn_generator as sn

file_path = ""

def generate_serials():
    sn.generate(file_path)

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(("Excel files","*.xlsx;*.xls"),))
    if file_path:
        generate_btn.config(state="normal")

window = tk.Tk()
window.geometry("350x150")
window.title("Serial Number Generator")
window.config(background="#313438")

open_btn = tk.Button(window,
                    text="Select a File",
                    command=select_file,
                    font=("Roboto",19,"bold"),
                    bg="#000000",
                    fg="#00FA00")

generate_btn = tk.Button(window,text="Generate",
                   command=generate_serials,
                   font=("Roboto",19,"bold"),
                   bg="#000000",
                   fg="#00FA00",
                   activebackground="#000000",
                   activeforeground="#00FF00",
                   state="disabled")

open_btn.pack(pady=15)
generate_btn.pack(pady=10)


window.mainloop()
