# Task 8: Enhanced Rule-based Chatbot

import random
from datetime import datetime

print("🤖 Chatbot: Hello! I am your enhanced chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()   # convert input to lowercase
    
    # Exit condition
    if user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day! 👋")
        break
    
    # Greeting
    elif user_input in ["hi", "hello", "hey"]:
        print("🤖 Chatbot: Hello! How can I help you today?")
    
    # Asking name
    elif "your name" in user_input:
        print("🤖 Chatbot: I’m a simple Python chatbot. You can call me ChatPy!")
    
    # Asking well-being
    elif "how are you" in user_input:
        print("🤖 Chatbot: I’m doing great! Thanks for asking. How about you?")
    
    # Asking time
    elif "time" in user_input:
        now = datetime.now().strftime("%H:%M:%S")
        print(f"🤖 Chatbot: The current time is {now}.")
    
    # Weather responses (simple placeholders)
    elif "weather" in user_input:
        weather_options = ["sunny ☀️", "cloudy ☁️", "rainy 🌧️", "windy 🌬️"]
        weather_today = random.choice(weather_options)
        print(f"🤖 Chatbot: The weather today seems {weather_today}.")
    
    # Telling a joke
    elif "joke" in user_input:
        jokes = [
            "Why did the computer go to the doctor? Because it caught a virus! 😆",
            "Why don’t programmers like nature? It has too many bugs! 🐛",
            "Why did the Python developer go broke? Because he kept using try-except! 😅"
        ]
        print(f"🤖 Chatbot: {random.choice(jokes)}")
    
    # Simple math: addition, subtraction, multiplication, division
    elif any(op in user_input for op in ["+", "-", "*", "/"]):
        try:
            result = eval(user_input)
            print(f"🤖 Chatbot: The answer is {result}")
        except:
            print("🤖 Chatbot: Sorry, I couldn't calculate that. Please enter a valid math expression.")
    
    # Default response
    else:
        print("🤖 Chatbot: Sorry, I don’t understand that. Can you try asking something else?")
