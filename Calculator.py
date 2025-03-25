from customtkinter import *
from tkinter import *
from PIL import Image


calculate_windo = CTk()
calculate_windo.title("Calculator")
calculate_windo.geometry("295x500")
# calculate_windo.resizable(height=False, width=False)

calculator_fram = CTkFrame(calculate_windo, fg_color="white")
calculator_fram.pack(side="top", expand=True, fill="both")

input_box = CTkTextbox(calculator_fram, height=80,width=300, state="disabled")
input_box.grid( columnspan=10, pady=5)

num_c = CTkButton(calculator_fram, width=60, height=60 , text="C")
num_c.grid(row=1, column=1, padx=5, pady=5)
num_open_brackt = CTkButton(calculator_fram, width=60, height=60 , text="(")
num_open_brackt.grid(row=1, column=2, padx=5, pady=5)
num_close_brackt = CTkButton(calculator_fram, width=60, height=60 , text=")")
num_close_brackt.grid(row=1, column=3, padx=5, pady=5)

num_1 = CTkButton(calculator_fram, width=60, height=60 , text="1")
num_1.grid(row=2, column=1, padx=5, pady=5)
num_2 = CTkButton(calculator_fram, width=60, height=60, text="2")
num_2.grid(row=2, column=2, padx=5, pady=5)
num_3 = CTkButton(calculator_fram, width=60, height=60, text="3")
num_3.grid(row=2, column=3, padx=5, pady=5)
num_4 = CTkButton(calculator_fram, width=60, height=60, text="4")
num_4.grid(row=3, column=1, padx=5, pady=5)
num_5 = CTkButton(calculator_fram, width=60, height=60, text="5")
num_5.grid(row=3, column=2, padx=5, pady=5)
num_6 = CTkButton(calculator_fram, width=60, height=60, text="6")
num_6.grid(row=3, column=3, padx=5, pady=5)
num_7 = CTkButton(calculator_fram, width=60, height=60, text="7")
num_7.grid(row=4, column=1, padx=5, pady=5)
num_8 = CTkButton(calculator_fram, width=60, height=60, text="8")
num_8.grid(row=4, column=2, padx=5, pady=5)
num_9 = CTkButton(calculator_fram, width=60, height=60, text="9")
num_9.grid(row=4, column=3, padx=5, pady=5)
num_0 = CTkButton(calculator_fram, width=60, height=60, text="0")
num_0.grid(row=5, column=2, padx=5, pady=5)
num_eq = CTkButton(calculator_fram, width=60, height=60, text="=")
num_eq.grid(row=5, column=3, padx=5, pady=5)

num_plus = CTkButton(calculator_fram, width=60, height=130, text="+")
num_plus.grid(row=4, column=4,rowspan=2, padx=5, pady=5)
num_minus = CTkButton(calculator_fram, width=60, height=60, text="-")
num_minus.grid(row=3, column=4, padx=5, pady=5)
num_mul = CTkButton(calculator_fram, width=60, height=60, text="*")
num_mul.grid(row=2, column=4, padx=5, pady=5)
num_div = CTkButton(calculator_fram, width=60, height=60, text="/")
num_div.grid(row=1, column=4, padx=5, pady=5)




calculate_windo.mainloop()