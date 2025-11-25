import random

game_levels = [
    {
        'level': 'easy',
        'option': 1,
        'min_value': 0,
        'max_value': 20
    },
    {
        'level': 'medium',
        'option': 2,
        'min_value': 0,
        'max_value': 50
    },
    {
        'level': 'hard',
        'option': 3,
        'min_value': 0,
        'max_value': 100
    }
]

def select_difficulty():
    optionsText = " ".join([f"{level['option']}-{level['level'].capitalize()}" for level in game_levels])
    
    while True:
        try:
            secim = int(input(f"Please select difficulty level: {optionsText} \n"))
            selectedLevel = next((level for level in game_levels if level['option'] == secim), None)
            if selectedLevel is None:
                print("Invalid selection. Please try again.")
            else:
                print(f"Selected difficulty: {selectedLevel['level']}")
                numberToGuess = random.randint(selectedLevel['min_value'], selectedLevel['max_value'])
                return selectedLevel, numberToGuess
        except ValueError:
            print("Please enter a valid number.")


def guess_number(selectedLevel, numberToGuess):
    counter = 0
    while True:
        counter += 1
        try:
            userGuess = int(input(f"Please make a guess between {selectedLevel['min_value']} and {selectedLevel['max_value']}\n"))
            
            if userGuess == numberToGuess:
                print("Congratulations, You found the correct number!")
                print(f"Correct Number: {numberToGuess}")
                print(f"Your total number of guesses: {counter}")
                break
            elif userGuess < numberToGuess:
                print("Enter a larger number.")
            else:
                print("Enter a smaller number.")
                
        except ValueError:
            print("Please enter a valid number.")

print("Welcome to the Number Guessing Game!")

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    selectedLevel, numberToGuess = select_difficulty()
    guess_number(selectedLevel, numberToGuess)

    while True:
        play_again = input("Do you want to play again? (yes/no or y/n): ").lower()
        if play_again in ["yes", "y"]:
            play_again = "yes"
            break
        elif play_again in ["no", "n"]:
            play_again = "no"
            break
        else:
            print("Invalid input! Please type (yes/no or y/n).")

print("Thanks for playing!")


