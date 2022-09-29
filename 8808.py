import random

def main():
    """Start a element guessing game."""
    print("Guess the element!")

    element = [
        "hydrogen",
        "helium",
        "lithium",
        "beryilium",
        "boron",
        "carbon",
        "nitrogen"
        ]

    x = random.choice(element)
    print(x)
    guess = None

    while x !=guess:

        guess = str(input("What element am i thinking of? "))

        if x == guess:
            print("You guessed {}. Congratulation you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

            
            
main()
