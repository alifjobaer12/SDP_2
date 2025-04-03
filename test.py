from customtkinter import *
import google.generativeai as ai



API_KEY = "AIzaSyCKQG_yy-weC61CylnUutQJZvCaRJlsiOI"
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-2.0-flash")
conversation = model.start_chat()


messages =""


def chat():
    global messages

    chatbot_chatbox.configure(state="normal")

    message = chatbot_entry.get().strip()
    chatbot_chatbox.insert(END, f"You: {message}\n\n")
    
    try:
        if not message:
            chatbot_chatbox.insert(END, f"Chatbot: Please enter a valid message. \n\n")

        if message.lower() == 'bye':
            chatbot_chatbox.insert(END, f"Chatbot: Goodbye! \n\n")
    
        response = conversation.send_message(message)
        chatbot_chatbox.insert(END, f"Chatbot: {response.text} \n\n")

    except Exception as e:
        error = f"Error: {str(e)}. Please try again."
        chatbot_chatbox.insert(END, f"Chatbot: {error}\n\n")
        # print("error")
            
    chatbot_entry.delete(0, END)
    chatbot_chatbox.configure(state="disabled")
    




root = CTk()

root.geometry("400x500")
root.title("Chat Bot")


chatbot_frame = CTkFrame(root, fg_color="light blue", width=400, height=500 )
chatbot_frame.pack(side="top", expand=True, fill="both",)



chatbot_chatbox = CTkTextbox(chatbot_frame, font=("JetBrains Mono", 15, "bold"), state="normal", width=400, height=400, text_color="white")
chatbot_chatbox.pack(side="top", anchor="w", padx=1, pady=5 )
chatbot_chatbox.insert(1.0, "Chatbot: Hello! Type your message or type 'bye' to exit. \n\n")
chatbot_chatbox.configure(state="disabled")

chatbot_entry = CTkEntry(chatbot_frame, font=("JetBrains Mono", 15, "bold"), width=320, height=50, fg_color="white", text_color="black")
chatbot_entry.pack( anchor="w", padx=1, pady=0)

chatbot_send_btn = CTkButton(chatbot_frame, font=("Helvetica", 16, "bold"), text="Send", width=70, height=46, command = chat,)
chatbot_send_btn.place( x=327+35, y=412+23, anchor="center")


root.mainloop()