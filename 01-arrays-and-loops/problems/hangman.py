import random

from numpy import place

def main():
    # set up the game
    word_bank : list = []
    with open("1-1000.txt", "r") as f:
        for ln in f:
            word_bank.append(ln.strip())

    word_index : int = random.randint(0,len(word_bank))
    real_word : str = word_bank[word_index]
    placeholder : str = "_" * len(real_word) # this is a special use of the function * with str
    guessed : list = []
    lives : int = 10
    guess : str = ""
    continue_game = True
    continue_input = ""

    while continue_game:
        pass # you can delete this line
        # tell the player how many lives they have remaining

        # tell the player to input a single letter between A and Z; make them try again if it's not between A and Z or has a length > 1        

        # if they got it right, tell them they got it right
        # else, tell them they got it wrong and take one life

        # go through each character of the placeholder
        # if the player guess was the same as the real 
        # NOTE: you can't change a string directly in Python (e.g. string[0] = 'a') is not valid
        # so you will have to use slice syntax or a loop to build up the string        

        # add the guess to guessed

        # if the player has no lives left, tell them they died
        # if they won the game, tell them they won

        # if the player either won or lost, ask them if they want to play again
        # they have to answer y or n, if they don't, ask them again
        # if they answer y, reset the game and select a new word
        # if they answer n, quit the game

if __name__ == "__main__":
    main()