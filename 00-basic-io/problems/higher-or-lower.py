import random

# 1: fill in the blanks
# 2: add a while loop to keep playing
# 3: add a win streak counter which resets when the player loses
# 4: make the game keep asking the player to enter their input until they provide a valid answer
# 5: use isinstance to check if input is number or string, and if it's a string which says 'quit', exit the game. otherwise ask for a valid answer.

def main():
    # greet the user
    print ("Welcome to higher or lower!")
    # set the previous number randomly
    prev_number : int = random.randint(1,13)

    # tell user the last number
    print (f"Last number was {str(prev_number)}. Numbers go from 1-13.")
    # tell user how to play
    print ("Guess if it'll be higher or lower! (1 for higher, 0 for lower) ")
    # get user guess (higher or lower)
    
    # generate the current number
    
    # if the current number > previous number and they guessed higher OR the current number < previous number and they guessed lower, they win.
    
    # otherwise, they lose
    
    # set the previous number to be the current number
    

if __name__ == "__main__":
    main()