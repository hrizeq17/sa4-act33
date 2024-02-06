number = 10

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? (Enter 'q' to quit): ")

    if guess.lower() == 'q':
        print(f"The correct number was {number}.")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input. Please enter a number or 'q'.")
        continue

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
