from ast import operator


def main():
    # ask the user for the first number
    print ("What's the first number?")
    # get the user input and convert it to a number
    n1 = float(input (">> "))
    # ask the user for the operator (+,-,/,*)
    print ("What's your operation?")
    # get the user input and don't convert it
    operator = input(">> ")
    # ask the user for the second number
    print ("What's the second number?")
    # get the user input and convert it to a number
    n2 = float(input (">> "))
    result : float = 0
    # using an if / elif / else statement, do something with your numbers to get a result
    if operator == "+":
        result = n1+n2
    elif operator == "-":
        result = n1-n2
    elif operator == "/":
        result = n1/n2
    elif operator == "*":
        result = n1*n2
    # output the result to the user
    print(f"Your result is {str(result)}.")

if __name__ == "__main__":
    main()