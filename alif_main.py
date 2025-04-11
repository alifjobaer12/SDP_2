from customtkinter import *
from currency_converter import *
from tkinter import *
from PIL import Image
from CTkScrollableDropdown import CTkScrollableDropdown
from tab import open_calculator

import google.generativeai as ai
import threading
import time
from chatbot import open_chatbot



set_appearance_mode("dark")
set_default_color_theme("blue")


def lonch_cal_btn():
    cal_frame = CTkFrame(main_windo, width=400, height=500 )
    cal_frame.pack(side="top", expand=True, fill="both",)
    open_calculator(cal_frame)
    back = CTkButton(cal_frame, text="<-", font=("JetBrains Mono", 26, "bold"), width=40, height=40, command=lambda:cal_frame.destroy())
    back.pack(pady=20)

def lonch_chatbot_btn():
    chat_frame = CTkFrame(main_windo,  width=400, height=500 )
    chat_frame.pack(side="top", expand=True, fill="both",)
    open_chatbot(chat_frame)
    back = CTkButton(chat_frame, text="<-", font=("JetBrains Mono", 26, "bold"), width=40, height=40, command=lambda: chat_frame.destroy())
    back.pack(pady=20)


main_windo = CTk()                                                              
main_windo.geometry("500x650")
main_windo.title("Calculator")

btn = CTkButton(main_windo, text="Open Calculator", font=("Helvetica", 14, "bold"), width=150, height=45, command=lonch_cal_btn)
btn.place(x=250, y=50, anchor="center")

chatbot_btn = CTkButton(main_windo, text="Open ChatBot", font=("Helvetica", 14, "bold"), width=150, height=45, command=lonch_chatbot_btn)
chatbot_btn.place(x=250, y=150, anchor="center")




# open_calculator(main_windo)
main_windo.mainloop()

