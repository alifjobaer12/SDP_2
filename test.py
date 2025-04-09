

from customtkinter import *
import google.generativeai as ai
import threading





def open_chatbot(root):

    API_KEY = "AIzaSyCKQG_yy-weC61CylnUutQJZvCaRJlsiOI"
    ai.configure(api_key=API_KEY)
    model = ai.GenerativeModel("gemini-2.0-flash")
    conversation = model.start_chat()


    messages =""

    def get_message():
        global messages
        messages = chatbot_entry.get().strip()

        if not messages:
            s=f"Chatbot: Please enter a valid message... "
            see_message(s)
            return

        see_message("You: " + messages)
        chatbot_entry.delete(0, END)
        threading.Thread(target=chatbot_response, args=(messages,), daemon=True).start()

    def see_message(text):
        chatbot_chatbox.configure(state="normal")
        chatbot_chatbox.insert(END, text + "\n\n")
        chatbot_chatbox.configure(state="disabled")
        chatbot_chatbox.see(END)

    def chatbot_response(sms):
        try:
            response = conversation.send_message(sms)
            r=f"Chatbot: {response.text} "
        except Exception as e:
            r = f"Error: {str(e)}. Please try again."
        see_message(r)



    # btn.pack_forget()

    chatbot_frame = CTkFrame(root, fg_color="light blue", width=400, height=500 )
    chatbot_frame.pack(side="top", expand=True, fill="both",)

    chatbot_chatbox = CTkTextbox(chatbot_frame, wrap="word", font=("JetBrains Mono", 14), state="normal", width=400, height=400, text_color="white", fg_color="black")
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





# root = CTk()
# root.geometry("400x500")
# root.title("Chat Bot")

# open_chatbot()

# btn = CTkButton(root, text="Open Chatbot", command=open_chatbot)
# btn.pack(pady=20)


# root.mainloop()