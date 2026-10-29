from datetime import datetime

print("=" * 35)
print("   WELCOME TO MY AI CHATBOT")
print("=" * 35)
print("You can ask me simple questions.")
print("Type 'help' to see options.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif "your name" in user:
        print("Bot: I am CodSoft Chatbot.")

    elif "how are you" in user:
        print("Bot: I am fine! How can I help you?")

    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "help" in user:
        print("Bot: You can ask my name, time, date, or say hello.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Thanks for chatting.")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")
        print("Bot: Try typing 'help'.")

    print()