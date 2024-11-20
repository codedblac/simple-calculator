secret_number = 9
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly.")
        break
else:
    print(f"Sorry, you've exceeded the guess limit. The secret number was {secret_number}.")