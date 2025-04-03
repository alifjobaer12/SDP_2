import google.generativeai as ai
API_KEY = "AIzaSyAY5XATDaHV5irDyRqSIMkv85d21Y31hno"

# Configure the API

ai.configure(api_key=API_KEY)

# Create a new model

model = ai.GenerativeModel("gemini-2.5-pro-exp-03-25")

chat = model.start_chat()

# Start a conversation
print("Chatbot: Hello! Type your message or type 'bye' to exit.")

while True:
    try:
        message = input('You: ').strip()
        
        if not message:
            print("Chatbot: Please enter a valid message.")
            print()
            continue

        if message.lower() == 'bye':
            print('Chatbot: Goodbye!')
            print()
            break
        
        response = chat.send_message(message)
        print(f"Chatbot: {response.text}" )
        print()

    except Exception as e:
        print(f"Error: {str(e)}. Please try again.")
        print()

