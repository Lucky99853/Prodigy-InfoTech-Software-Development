import random

print("=" * 45)
print("       GUESS THE NUMBER GAME")
print("=" * 45)

# Generate a random number
secret_number = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number {secret_number} correctly.")
            print(f"It took you {attempts} attempts to win.")
            break

    except ValueError:
        print("Please enter a valid number.")
