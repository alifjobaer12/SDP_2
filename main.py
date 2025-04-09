from customtkinter import *
from currency_converter import *
from tkinter import *
from PIL import Image
from CTkScrollableDropdown import CTkScrollableDropdown
from test_main import open_calculator
# from customtkinter import *
import google.generativeai as ai
import threading
import time
from test import open_chatbot


set_appearance_mode("dark")
set_default_color_theme('dark-blue')


def lonch_cal_btn():
    cal_frame = CTkFrame(main_windo, width=400, height=500 )
    cal_frame.pack(side="top", expand=True, fill="both",)
    btn.pack_forget()
    chatbot_btn.pack_forget()
    open_calculator(cal_frame)
    back = CTkButton(cal_frame, text="Back", font=("Helvetica", 16, "bold"), width=200, height=50, command=lambda: cal_frame.pack_forget())
    back.pack(pady=20)

def lonch_chatbot_btn():
    chat_frame = CTkFrame(main_windo,  width=400, height=500 )
    chat_frame.pack(side="top", expand=True, fill="both",)
    btn.pack_forget()
    chatbot_btn.pack_forget()
    open_chatbot(chat_frame)
    back = CTkButton(chat_frame, text="Back", font=("Helvetica", 16, "bold"), width=200, height=50, command=lambda: chat_frame.pack_forget())
    back.pack(pady=20)


main_windo = CTk()                                                              
main_windo.geometry("500x600")
main_windo.title("Calculator")

btn = CTkButton(main_windo, text="Open Calculator", font=("Helvetica", 16, "bold"), width=200, height=50, command=lonch_cal_btn)
btn.pack(pady=20)

chatbot_btn = CTkButton(main_windo, text="Open ChatBot", font=("Helvetica", 16, "bold"), width=200, height=50, command=lonch_chatbot_btn)
chatbot_btn.pack(pady=20)




# open_calculator(main_windo)
main_windo.mainloop()

