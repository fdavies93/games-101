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
        # tell the player how many lives they have remaining
        print(f"Lives remaining: {lives}")

        # tell the player to input a single letter between A and Z; make them try again if it's not between A and Z or has a length > 1        
        while not (len(guess) == 1 and guess[0].lower() >= 'a' and guess[0].lower() <= 'z' and guess not in guessed ):
            print("Please enter your guess between A and Z.")
            print(f"Current word: { placeholder }")
            if len(guessed) > 0:
                print(f"Letters guessed: {','.join(guessed)}")
            guess = input()

        # if they got it right, tell them they got it right
        # else, tell them they got it wrong and take one life
        if guess in real_word:
            print (f"{guess} is in the word!")
        else:
            print (f"{guess} is not in the word.")
            lives -= 1

        # go through each character of the placeholder
        # if the player guess was the same as the real 
        # NOTE: you can't change a string directly in Python (e.g. string[0] = 'a') is not valid
        # so you will have to use slice syntax or a loop to build up the string        
        for i, char in enumerate(real_word):
            if placeholder[i] == "_" and guess == char and char not in guessed:
                new_placeholder = placeholder[:i] + char
                if i < len(placeholder) - 1:
                    new_placeholder = new_placeholder + placeholder[i+1:] 
                placeholder = new_placeholder

        # add the guess to guessed
        guessed.append(guess)

        # if the player has no lives left, tell them they died
        # if they won the game, tell them they won
        if lives == 0:
            print("You died...")
        elif placeholder == real_word:
            print(f"The word was {real_word}.")
            print("Congratualations! You won the game!")
            lives = 0

        # if the player either won or lost, ask them if they want to play again
        # they have to answer y or n, if they don't, ask them again
        # if they answer y, reset the game and select a new word
        # if they answer n, quit the game
        while lives == 0 and continue_input != "y" and continue_input != "n":
            print("Do you want to play again? Type y or n.")
            continue_input = input()
            if continue_input == "y":
                guessed = []
                real_word = word_bank[word_index]
                placeholder = "_" * len(real_word)
                lives = 10
                guess = ""
            elif continue_input == "n":
                continue_game = False


if __name__ == "__main__":
    main()