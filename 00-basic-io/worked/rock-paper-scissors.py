from random import randint

def main():
    names : str = ["paper", "scissor", "stone"]
    ai_guess = randint(0,2)
    print ("Let's play paper, scissor, stone!\nEnter your guess:\n0 - paper\n1 - scissor\n2 - stone")
    game_state = 0 # 0 is draw, 1 is player win, -1 is player loss

    player_guess : int = 0 # change this

    if player_guess == ai_guess:
        game_state = 0
        
    elif (player_guess + 1) % 3 == ai_guess:
        game_state = -1

    else:
        game_state = 1
    
    print (f"You guessed {names[player_guess]}.")
    print (f"The AI guessed {names[ai_guess]}.")

    print ( {-1: "The AI won. 🙁", 0: "It was a draw. 😐", 1: "You won! 😊"}[game_state] )

if __name__ == "__main__":
    main()