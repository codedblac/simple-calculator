import random
from typing import Dict, List


# =========================
# Configuration & Data
# =========================

GREETINGS: List[str] = [
    "Hello!",
    "Hi there!",
    "Hey!",
    "Greetings!",
    "Howdy!",
]




FAREWELLS: List[str] = [
    "Goodbye!",
    "See you later!",
    "Take care!",
    "Bye!",
]

SMALL_TALK: List[str] = [
    "I'm just a bot, but I'm here to help!",
    "What would you like to talk about?",
    "I enjoy chatting with you!",
    "Tell me more about yourself!",
]

QUESTIONS: Dict[str, List[str]] = {
    "how are you": [
        "I'm just a program, but thanks for asking!",
        "Doing great! How about you?",
        "I'm functioning as expected!",
    ],
    "what is your name": [
        "I'm a chatbot created by you!",
        "I don't have a name, but you can call me Bot.",
        "I'm just a simple chatbot.",
    ],
    "what can you do": [
        "I can chat with you!",
        "I can answer simple questions.",
        "I can engage in small talk!",
    ],
}


EXIT_COMMANDS = {"bye", "exit", "quit"}
GREETING_KEYWORDS = {"hello", "hi", "hey", "greetings"}
FAREWELL_KEYWORDS = {"bye", "goodbye", "see you"}


# =========================
# Core Logic
# =========================

def normalize_text(text: str) -> str:
    """
    Normalize user input for easier matching.
    """
    return text.lower().strip()


def contains_keyword(text: str, keywords: set[str]) -> bool:
    """
    Check if any keyword exists in the given text.
    """
    return any(keyword in text for keyword in keywords)


def get_response(user_input: str) -> str:
    """
    Generate a chatbot response based on user input.
    """
    normalized_input = normalize_text(user_input)

    # Greetings
    if contains_keyword(normalized_input, GREETING_KEYWORDS):
        return random.choice(GREETINGS)

    # Farewells
    if contains_keyword(normalized_input, FAREWELL_KEYWORDS):
        return random.choice(FAREWELLS)

    # Predefined questions
    for question, responses in QUESTIONS.items():
        if question in normalized_input:
            return random.choice(responses)

    # Default fallback
    return random.choice(SMALL_TALK)


# =========================
# Application Entry Point
# =========================

def main() -> None:
    """
    Run the chatbot interaction loop.
    """
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if normalize_text(user_input) in EXIT_COMMANDS:
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
