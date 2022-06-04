# import random module
import random

print("-----\N{smiling face with sunglasses}WELCOME TO ROCK PAPER SCISSORS GAME\N{smiling face with sunglasses}-----")
print("Rules of the Game are as follows: \nROCK v/s PAPER = PAPER wins \nPAPER v/s SCISSOR = SCISSOR wins \nROCK v/s SCISSOR = ROCK wins  \n")

while True:
    print("Enter  \n R for Rock \n P for Paper \n S for Scissor \n")
    # take the input from user
    user_input = input("Player Turn:")
    user_input = user_input.upper()

    # checking if user enter valid input
    while (user_input != "P") and (user_input != "S") and (user_input != "R"):
        user_input = input("ERROR,Invalid Input \nEnter Valid Input: ")
        user_input = user_input.upper()

    # Equating the user_input to its right value
    if user_input == "R":
        user_input_value = 'Rock'
    elif user_input == "P":
        user_input_value = 'Paper'
    else:
        user_input_value = 'Scissor'

    # print user input
    print("Player Input is:" + user_input_value)

    # Computer chooses randomly from the game_input list
    print("\nComputer Turn:")
    game_inputs = ["P", "R", 'S']
    comp_input = random.choice(game_inputs)

    # checking if computer enter valid input
    while comp_input == user_input:
        comp_input = random.choice(game_inputs)

    # Equating the comp_input to its right value
    if comp_input == "R":
        comp_input_value = 'Rock'
    elif comp_input == "P":
        comp_input_value = 'Paper'
    else:
        comp_input_value = 'Scissor'

    # print computer input
    print("CPU Input is: " + comp_input_value)

    print("\n-----------RESULT--------------")

    print(f"Player({user_input_value})" + " : " + f"CPU({comp_input_value})")

    # condition for winning
    if ((user_input == "R" and comp_input == "P") or
            (user_input == "P" and comp_input == "R")):
        print("Paper Wins: ", end="")
        result = "Paper"

    elif ((user_input == "R" and comp_input == "S") or
          (user_input == "S" and comp_input == "R")):
        print("Rock Wins: ", end="")
        result = "Rock"
    else:
        print("Scissor Wins: ", end="")
        result = "Scissor"

    # Printing who wins
    if result == user_input_value:
        print("|==| USER WINS |==| \U0001F600")
    else:
        print("|==| CPU WINS |==| \U0001F612")

    # checking if user wants to play again
    print("Do you want to play again? (Y/N)")
    play_again = input()
    play_again = play_again.upper()

    # if user input n Game stops
    if play_again == 'N':
        break


print("\nThanks for playing ROCK PAPER SCISSORS GAME\N{smiling face with sunglasses}")
