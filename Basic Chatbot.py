import random
import datetime

def chatbot():
    # Time-based greeting
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning!"
    elif hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    
    print(f"Chatbot: {greeting} I'm your friendly chatbot. Type 'bye' to exit.")
    
    # Predefined reply sets
    greetings = ["hi", "hello", "hey"]
    replies_greeting = ["Hi there!", "Hello!", "Hey!", "Nice to see you!"]

    how_are_you = ["how are you", "how r u", "how's it going"]
    replies_feeling = ["I'm great, thanks for asking!", "Doing well, and you?", "Feeling awesome today!"]

    bye_words = ["bye", "goodbye", "see you", "exit"]
    replies_bye = ["Goodbye!", "See you soon!", "Take care!", "Bye bye!"]

    # Chat loop
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input in greetings:
            print("Chatbot:", random.choice(replies_greeting))
        
        elif user_input in how_are_you:
            print("Chatbot:", random.choice(replies_feeling))
        
        elif user_input in bye_words:
            print("Chatbot:", random.choice(replies_bye))
            break
        
        else:
            print("Chatbot: Hmm... I didn’t quite get that. Could you rephrase?")

# Run chatbot
chatbot()
