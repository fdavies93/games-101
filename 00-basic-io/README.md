# 1.0 Writing Code

## Your First Program

Open up a file. Call it `hello.py`. Inside the file put the following:

```py
print("Hello world!")
```

Now run it in your choice of environment:
```sh
python hello.py
# Hello world!
```

We'll come back to this later. First let's talk about variables.

## What is a variable?

A variable is a name for some data you want to store.

Variables have types in Python, but you can’t always see them. In this course we
will use type hints to make the types of variables clear.

You can change between types using functions with the same name as the type.

### Example

I want to keep my student’s name and age in my program. Name is a string, while
age is an integer (a whole number).

```py 
name : str = “John Doe” 
age : int = 20 
age_as_str : str = str(age) # "20"
```

## Basic Types

### Strings

Used to store text information. They need to be wrapped in
quotes. They use the keyword `str`.

```py
name: str = "John Doe"
name: str = 'John Doe' # this is also valid
```

### Integers

Used to store whole (countable) numbers. They use the keyword `int`.

```py
age: int = 24
```

### Floats

Used to store numbers with a decimal point. They use the keyword `float`.

```py
temperature: float = 25.5
```

### Booleans

Used to store true or false values. They use the keyword `bool`. 
In Python `True` and `False` are always capitalised.

```py
isTrue : bool = True
isFalse : bool = False
```

### Converting between types

We can convert between types by using the keyword for a type:

```py
a : str = "-5" # -5
b : int = int("-5") # -5
c : float = float("-5") # -5.0
d : bool = bool("-5") # should fail
```

### Exercise

1. Which types of variable would I want for storing the following pieces of information?

    - The name of a player's character. 
    - Whether or not a player is poisoned.
    - How much damage the poison does every second.
    - What percentage of the player's health is remaining.

2. I want to let players pick their ability scores. I take their input (a
   string) and want to check if the value of their ability score is too high or
   too low. Fill in the blank.

```py
score_str : str = input("Enter your strength:")
score : int = pass # what should I put here?

if score >= 10 and score <= 20:
    print("All good!")
else:
    print("This is bad!")
```


## Operators

An operator lets you do something with a variable.

Most operators will behave the same way with different types of variable, but some behave differently depending on the types of variables you give to them.

E.g. I want to add `a` and `b` together and store the result in `sum`.

```py
a : int = 10
b : int = 5
sum : int = a + b # sum is 15 now
```

## Basic Operators

### Comment

This makes everything after a `#` sign a comment, which means it's not part of
the code. Usually you use this to help other programmers understand your code.

```py
# one line comment
c = log(a + b) / 2 ** 3 # wtf is this? an inline comment
```

### Assignment

Assignment means storing some value in a variable. We use the `=` operator to do
this in Python.

```py
a : int = 7
```

### Arithmetic (Math) Operations

These don't store values, but do give a result from two other values. The basic
math operations are `+`, `-`, `*` (multiply), and `/` (divide).

There's also `**`, which means "raise to the power of" and many other operations
available in the math library.

```py
a : int = 10
b : int = 15
sum : int = a + b # now sum is 15 
minus_one : int = sum - 1 # 14
twenty_eight : int = minus_one * 2 # 28
divided: int = twenty_eight / 4 # 7
```

### Math and Assignment (Compound) Operators

These combine the assignment and math operators by doing an operation and
storing the result. They are `+=`, `-=`, `*=` and `/=`.

```py
a : int = 10
b : int = 5
a -= b # now a is 5
```

### Modulus

This means 'divide by a number and return the remainder'. It's important in
programming for reasons we'll get onto later.

```py
a : int = 5
mod : int = a % 3 # mod is 2
mod = a % 5 # mod is 0
mod = a % 9 # mod is 4
```

### Parentheses

These work the same way as in math: they change the order that operations happen in.

```py
1 + 1 # 2
2 * 5 + 7 # 17
2 * (5 + 7) # 24
```

### Exercise

1. In the following piece of code, what are the final values of a, b, c, and d?

```py
a = 1 + 1

b = 5
b *= a

c = b * 6
c /= 3

d = ((6 * 4) / 2) % 5
```

2. The pythagorean theorem says that in a triangle, a^2 + b^2 = c^2. Write a program to 
calculate c. Hint: `** 0.5` means square root (power of 1/2 = square root).

```py
a : float = float(input("Enter a >"))
b : float = float(input("Enter b >"))

# c = ...
print(c)
```

## User Input and Output

Remember our first program above?

```py
print("Hello world!")
```

This is an example of printing output to the console. As well as printing
strings, we can insert other types of value into the string. One way to do this
is by using a **string template**.

```py
a : int = int(input("Enter a number > ")) 
print("The number you entered was {}", a)
```

Another way is to use a **format string** (f-string), which automatically
inserts variables into the middle of the string.

```py
a : int = int(input("Enter a number > ")) 
print(f"The number you entered was {a}")
```

Notice the input statement above? The string in the parentheses is the prompt
that a user sees. Then, after the user enters their input, the `int()` statement
converts it into a number. You can use this to get input from users on the
console.

There are a lot of ways to take input from and give output to users, and we'll
cover more of these later, but for the first few lessons `print()` and
`input()` are all we need.

### Exercise

1. Take some user input and print it out to the screen.
2. Take two user inputs, a and b, and print them out as: `a is VALUE and b is
   VALUE`.
3. Make a and b into numbers, add them together, and print out the result. 

## If and else

If and else statements let you write code that only runs when something is true (or false).

You can write if, elif (else if), and else together to make a more complex statement.

You need to use them with a statement that returns a bool (since bool is always true or false).

For example: I only want over-21s at my party to be served alcohol. I also want over 60s to get a free drink.

```py
if age < 21:
	print("Sorry, I can't serve you a drink.")
elif age > 60:
	print("Here's your free drink.")
else:
	print("Here's your drink, that's $5.")
```

If and else statements will always exit after the first True statement:

```py
a = 20

if a > 10:
    print("Code stops here.")
elif a > 15:
    print("This never happens.")
else:
    print("Neither does this.")
```

## Logical Operators

Logical operators work on boolean values the same way arithmetic operators work
on numbers. This sounds complex, but it's actually quite intuitive:

```py
if a and b:
    do_something()
```

We can check the value of a single variable in two different ways:

```py
if a:
    do_something()

if a == True:
    do_something()
```

You can also use comparisons to get a True or False value by comparing other
types of variable:

```py
a = (1 == 1) # True
b = 1 < 2 # True
c = 500 <= 10 # False
```

### Exercise

```py
a = 1 < 2 # a is less than b
b = 1 > 2 # a is more than b
c = 1 >= 1 # a is more than or equal to b
d = 1 <= 0 # a is less than or equal to b
e = 1 == 1 # a is equal to b
```

Now figure out what the value of each line is.

### Truth tables

The operators `and` and `or` don't mean exactly the same thing they do in normal
English. We can look at this with a **truth table**. Given two variables, `a`
and `b`, we get different results from the same operation:

| `a`   | `b`    | `a and b` |
|-------|--------|-----------|
| True  | True   |    True   |
| True  | False  |    False  |
| False | True   |    False  |
| False | False  |    False  |


| `a`   | `b`    | `a or b`  |
|-------|--------|-----------|
| True  | True   |    True   |
| True  | False  |    True   |
| False | True   |    True   |
| False | False  |    False  |

As you can see, `or` in logic means **one or both** operands are true.

The other common logical operator is `not`, which reverses the value of `True`
and `False`.

| `a`   | `not a` |
|-------|---------|
| True  | False   |
| False | True    |

There are other operators which can be used to do **boolean arithmetic**, but as
this is less common we will not cover it here.

### Exercise

1. What are the values of a, b, c, and d at the end of this code?

```py
a = True or False
b = a and False
c = not b
d = (a and b) or b
```

2. What does the following program print out?

```py

a = True
b = False

if a:
    a = not a

if not (a and b):
    print("First option")
else:
    print("Second option") 

```

## Problem 1: Calculator

[Find it here](./problems/calculator.py)

For this exercise, you need to fill in the blanks in the code to make a simple
calculator app. The comments in the code should explain what to do.

Next time we'll make our first game: higher or lower.

