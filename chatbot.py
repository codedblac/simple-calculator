import random

# Predefined responses
greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Howdy!"]
farewells = ["Goodbye!", "See you later!", "Take care!", "Bye!"]
small_talk = [
    "I'm just a bot, but I'm here to help!",
    "What would you like to talk about?",
    "I love chatting with you!",
    "Tell me more about yourself!",
]

questions = {
    "how are you": ["I'm just a program, but thanks for asking!", "Doing great, how about you?", "I'm functioning as expected!"],
    "what is your name": ["I'm a chatbot created by you!", "I don't have a name, but you can call me Bot.", "I'm just a simple chatbot."],
    "what can you do": ["I can chat with you!", "I can answer simple questions.", "I can engage in small talk!"],
}

def get_response(user_input):
    user_input = user_input.lower()
    
    # Check for greetings
    if any(greet in user_input for greet in ["hello", "hi", "hey", "greetings"]):
        return random.choice(greetings)
    
    # Check for farewells
    if any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return random.choice(farewells)

    # Check for questions
    for question in questions:
        if question in user_input:
            return random.choice(questions[question])

    # Default response for small talk
    return random.choice(small_talk)

def main():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()