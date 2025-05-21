import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")

    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 0

        print("\nI'm thinking of a number between 1 and 100.")

        while True:
            try:
                guess = int(input("Take a guess: "))
                attempts += 1
            except ValueError:
                print("Please enter a valid number.")
                continue

            if guess < 1 or guess > 100:
                print("Your guess is out of bounds! Please guess a number between 1 and 100.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    guess_the_number()
