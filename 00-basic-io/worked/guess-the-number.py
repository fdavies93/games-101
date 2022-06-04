import random

def main():

    number : int = random.randint(1,10)
    print ("Guess my number! (It's between 1 and 10)")
    guess : int = int(input(">> "))
    
    if guess == number:
        print ("Congratulations, you won!")
    else:
        print ("Oh no! You lost!")
    
    print (f"My number was {str(number)}.")

if __name__ == "__main__":
    main()