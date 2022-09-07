# flashcards.py
# import the json module from python3
import json

#open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    # print(data)

total_questions = len(data["cards"])

# calculate score as a current running total instead of score out of total number of questions
current_total = 0
current_score = 0
round_number = 0

print("""
Welcome to the Flashcard CLI game!
""")

# function to go to another round of the game
def another_round(play_again):
    if play_again.lower() == "y":
        print("You've chosen to play again. Have fun!")
        return True
    else:
        print(f"""You've chosen to quit, or you've given an incorrect input.
You played {round_number} rounds and achieved a score of {current_score}/{current_total}.
{evaluation(current_score, current_total)}
Goodbye!
""")

        return False

# function to evaluate performance
def evaluation(current_score, current_total):
    if current_score / current_total < 0.5:
        return "You need practice..."
    elif current_score / current_total >= 0.5 and current_score < current_total:
        return "Good work."
    else:
        return "Amazing, you got them all correct!"

# while loop to keep going until the player wants to quit
while True:
    round_number += 1
    print(f"This is round #{round_number}!")
    print(f"There are {total_questions} questions in this round.")
    print("")
    for i in data["cards"]:
        current_total += 1
        guess = input(i["q"] + " > ")
        # print(i)

        if guess.lower() == i["a"].lower():
            current_score += 1
            print(f"Correct! Your current score is: {current_score}/{current_total}")
            print("")
        else:
            print(f'Incorrect!, The correct answer was {i["a"]}')
            print(f"Your current score is: {current_score}/{current_total}")
            print("")
    play_again = input("Would you like to play another round? [enter y/n]: ")
    print("")
    
    if another_round(play_again) == False:
        break
    





