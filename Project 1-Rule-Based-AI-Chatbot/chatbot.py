responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "how are you": "I'm just a chatbot, but I'm doing well!",
    "your name": "I am a Rule-Based AI Chatbot.",
    "help": "You can greet me or ask basic questions.",
    "thanks": "You're welcome!"
}

exit_commands = ["bye", "exit", "quit"]

print("Rule-Based AI Chatbot Started!")
print("Type 'bye', 'exit', or 'quit' to stop.")

while True:

    user_input = input("You: ").strip().lower()

    if user_input in exit_commands:
        print("Bot: Goodbye! Have a great day.")
        break

    elif user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello!")
        
    elif user_input in responses:
        print("Bot:", responses[user_input])

    else:
        print("Bot: Sorry, I don't understand that.")