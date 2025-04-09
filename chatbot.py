from customtkinter import *
import google.generativeai as ai
import threading
import time
from test import open_chatbot


API_KEY = ""
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-2.0-flash")
conversation = model.start_chat()


messages =""



def open_cb():
    btn.pack_forget()
    open_chatbot(root)

def clear_chat():
    # time.sleep(1)
    chatbot_chatbox.configure(state="normal")
    chatbot_chatbox.delete(1.0, "end")
    see_message("Chatbot: Chat Cleared...\n\n")
    chatbot_chatbox.configure(state="disabled")

def get_message():
    global messages
    messages = chatbot_entry.get().strip()

    if not messages:
        s=f"Chatbot: Please enter a valid message... "
        see_message(s+"\n\n")
        return
    if messages.lower() == "clear":
        chatbot_entry.delete(0, END)
        chatbot_chatbox.configure(state="normal")
        see_message("Chatbot: Chat clearing ")
        chatbot_chatbox.update()
        time.sleep(1)
        for i in range(3):
            see_message(".")
            chatbot_chatbox.update()
            time.sleep(1)
        clear_chat()
        chatbot_chatbox.configure(state="disabled")
        return
    
    see_message("You: " + messages + "\n\n")
    chatbot_entry.delete(0, END)
    threading.Thread(target=chatbot_response, args=(messages,), daemon=True).start()

def see_message(text):
    chatbot_chatbox.configure(state="normal")
    chatbot_chatbox.insert(END, text)
    chatbot_chatbox.configure(state="disabled")
    chatbot_chatbox.see(END)

def chatbot_response(sms):
    try:
        response = conversation.send_message(sms)
        r=f"Chatbot: {response.text} "
    except Exception as e:
        r = f"Error: {str(e)}. Please try again."
    see_message(r+"\n\n")



root = CTk()

root.geometry("400x500")
root.title("Chat Bot")

btn = CTkButton(root, text="Open Chat Bot", command=open_cb, width=200, height=50)
btn.pack(pady=20)

chatbot_frame = CTkFrame(root, fg_color="light blue", width=400, height=500 )
chatbot_frame.pack(side="top", expand=True, fill="both",)

chatbot_chatbox = CTkTextbox(chatbot_frame, wrap="word", font=("JetBrains Mono", 14), state="normal", width=400, height=400, text_color="white")
chatbot_chatbox.pack(side="top", anchor="w", padx=1, pady=5 )
chatbot_chatbox.insert(1.0, "Chatbot: Hello! Type your message that you want to know... \n\n")
chatbot_chatbox.configure(state="disabled")

chatbot_entry = CTkEntry(chatbot_frame, placeholder_text="Type your message..." , font=("JetBrains Mono", 14), width=285, height=50, fg_color="white", text_color="black")
chatbot_entry.pack( anchor="w", padx=1, pady=0, ipadx=19)
chatbot_entry.bind("<Return>", lambda event: get_message())  

chatbot_send_btn = CTkButton(chatbot_frame, font=("Helvetica", 16, "bold"), text="Send", width=70, height=48, command = get_message,)
chatbot_send_btn.place( x=327+35, y=412+23, anchor="center")

copyrights = CTkLabel(chatbot_frame, text="AliF© ^.^", font=("Calibri", 12), corner_radius=0, width=1, height=1, fg_color="transparent", bg_color="transparent", text_color="#9e9e9e", )
copyrights.place(x=330, y=485, anchor="w") 





root.mainloop()