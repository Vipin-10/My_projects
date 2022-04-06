import random
#Rock, Paper and Scissors Game
# Rock>scissors, scissors>paper, paper>rock
while True:
    user_input= input("Choose one- Rock, Paper and Scissors: ").lower()
    total_choices= ["rock", "paper", "scissors"]
    computer_input= random.choice(total_choices)
    print(f"Computer choose {computer_input}")
    if user_input== computer_input:
        print(f"Both are same, {user_input}. It's a tie")
    elif user_input == "rock":
        if computer_input== "scissors":
            print("User wins!")
        else:
            print("Computer wins!")
    elif user_input == "paper":
        if computer_input == "rock":
            print("User wins!")
        else:
            print("Computer wins!")
    elif user_input== "scissors":
        if computer_input== "paper":
            print("User wins!")
        else:
            print("Computer wins!")

    play_again= input("Wanna play again? yes/no")
    if play_again== "no" :
        break
print("Game over! :)")