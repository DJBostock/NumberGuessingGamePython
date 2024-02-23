from random import randint

game_is_on = True
attempts_hard = 5
attempts_easy = 10


def set_attempts():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty[0] == 'e':
        return attempts_easy
    else:
        return attempts_hard


def set_goal_number():
    return randint(1, 100)


while game_is_on:
    print("Welcome to the Number Guessing Game.")
    print("I'm thinking of a number between 1 and 100.")

    goal_number = set_goal_number()
    remaining_attempts = set_attempts()

    correct_guess_made = False

    while not correct_guess_made and remaining_attempts > 0:
        print(f"Remaining attempts: {remaining_attempts}")
        new_guess = int(input("Make a guess: "))
        if new_guess == goal_number:
            print(f"That is correct! The number was {goal_number}.")
            correct_guess_made = True
        elif new_guess > goal_number:
            print("Too high")
        else:
            print("Too low")
        remaining_attempts -= 1

    if not correct_guess_made and remaining_attempts <= 0:
        print("You lose.")

    play_again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
    if play_again[0] == 'n':
        game_is_on = False
        print("Thank you for playing.")
    else:
        for _ in range(3):
            print("\n")
