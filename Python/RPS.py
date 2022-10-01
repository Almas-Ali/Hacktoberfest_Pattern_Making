import random
def choices():

    player_choice = input("Enter a choice (rock,paper,scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player,computer):
    print(f"player chose {player} and computer chose {computer}")
    
    if player == computer:
        return "it's a tie"
   
    elif player == "rock":
        if computer == "paper":
            return("computer wins")
        elif computer == "scissors":
            return("player wins")
   
    elif player == "paper":
        if computer == "scissors":
            return("computer wins")
        elif computer == "rock":
            return("player wins")

    elif player == "scissors":
        if computer == "paper":
            return("player wins")
        elif computer == "rock":
            return("computer  wins")    

choices=choices()    
print(check_win( choices["player"], choices["computer"]) )
