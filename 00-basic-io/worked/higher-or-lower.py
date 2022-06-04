import random

def main():
    # greet the user
    print ("Welcome to higher or lower!")
    # set the previous number randomly
    prev_number : int = random.randint(1,13)
    # set the win streak
    win_streak : int = 0

    # repeat forever
    while True:
        # tell user their win streak
        print (f"Your current win streak is {str(win_streak)}.")
        # tell user the last number
        print (f"Last number was {str(prev_number)}. Numbers go from 1-13.")
        # tell user how to play
        print ("Guess if it'll be higher or lower! (1 for higher, 0 for lower) ")
        # get user guess (higher or lower)
        current_guess = int(input(">> "))
        # generate the new number
        cur_number = random.randint(1,13)
        # if the current number > previous number and they guessed higher OR the current number < previous number and they guessed lower, they win.
        if ((cur_number > prev_number) and current_guess == 1) or ((cur_number < prev_number) and current_guess == 0): # win
            print (f"Number is {str(cur_number)}. You won!")
            win_streak += 1
        # otherwise, they lose
        else:
            print (f"Number is {str(cur_number)}. You lost!")
            win_streak = 0
        print("------------------------------------------------------------------------------")
        # set the previous number to be the current number
        prev_number = cur_number

if __name__ == "__main__":
    main()