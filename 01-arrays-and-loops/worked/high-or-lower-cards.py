import random
from typing import Type

def generate_deck():
    deck = []
    faces = [str(v) for v in range(1,14)]
    faces[0] = "A"
    faces[10] = "J"
    faces[11] = "Q"
    faces[12] = "K"

    for suit in ["♣","♦","♥","♠"]:
        for face in faces:
            deck.append(face+suit)
    return deck

def shuffle(arr : list):
    copy : list = arr.copy()
    i : int = len(copy) - 1
    while i > 1:
        j = random.randint(0,i)
        temp = copy[j]
        copy[j] = copy[i]
        copy[i] = temp
        i -= 1
    return copy

def get_card_value(card : str):
    value_map = {"A": 1, "J": 11, "Q": 12, "K": 13}
    face = card[:-1]
    if face in value_map:
        return value_map[face]
    else:
        return int(face)

def main():
    print ("Welcome to higher or lower!")
    # prev_card : int = random.randint(1,13)

    win_streak : int = 0

    deck = generate_deck()

    print(deck)

    deck = shuffle(deck)
    print(deck)

    prev_card = deck.pop()
    prev_value = get_card_value(prev_card)

    while True:
        print (f"Your current win streak is {str(win_streak)}.")
        print (f"Last card was {prev_card}. (Value: {str(prev_value)})")
        current_guess : int = -1
        while current_guess != 0 and current_guess != 1:
            print ("Guess if it'll be higher or lower! (1 for higher, 0 for lower) ")
            # catch any strings in the file
            try:
                current_guess = int(input(">> "))
            except ValueError:
                pass
        cur_card = deck.pop()
        cur_value = get_card_value(cur_card)
        if ((cur_value > prev_value) and current_guess == 1) or ((cur_value < prev_value) and current_guess == 0): # win
            print (f"Number is {str(cur_card)} (Value: {str(cur_value)}). You won!")
            win_streak += 1
        # otherwise, they lose
        else:
            print (f"Card is {str(cur_card)}. (Value: {str(cur_value)}) You lost!")
            deck = generate_deck()
            deck = shuffle(deck)
            win_streak = 0
        print("------------------------------------------------------------------------------")
        prev_card = cur_card
        prev_value = cur_value

if __name__ == "__main__":
    main()