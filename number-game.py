# Guessing the correct number game
 
import random

class GuessTheNumber:
    def __init__(self, lower=1, upper=100, attempts=5):
        self.lower = lower
        self.upper = upper
        self.max_attempts = attempts
        self.number_to_guess = random.randint(self.lower, self.upper)
        self.attempts_left = self.max_attempts

    def get_user_guess(self):
        while True:
            try:
                guess = int(input(f"Enter your guess ({self.lower}-{self.upper}): "))
                if self.lower <= guess <= self.upper:
                    return guess
                else:
                    print(f"Please enter a number between {self.lower} and {self.upper}.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    def play(self):
        print("🎯 Welcome to the Guess the Number Game!")
        print(f"I'm thinking of a number between {self.lower} and {self.upper}. You have {self.max_attempts} attempts.")

        while self.attempts_left > 0:
            guess = self.get_user_guess()
            self.attempts_left -= 1

            if guess == self.number_to_guess:
                print("🎉 Congratulations! You guessed the correct number.")
                break
            elif guess < self.number_to_guess:
                print("Too low!")
            else:
                print("Too high!")

            print(f"Attempts left: {self.attempts_left}")

        else:
            print(f"😢 Game over! The number was {self.number_to_guess}.")

    def reset_game(self):
        self.number_to_guess = random.randint(self.lower, self.upper)
        self.attempts_left = self.max_attempts


def main():
    game = GuessTheNumber()

    while True:
        game.play()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye. 👋")
            break
        game.reset_game()


if __name__ == "__main__":
    main()
