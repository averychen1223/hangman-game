"""
File: hangman.py
Name: Chia-Yu Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def display(life):
    """
    This function visualize the hangman
    """
    if life == 7:
        print(
            """
            --------
            |      |
            |      
            |
            |
            |
            -
        """
        )
    elif life == 6:
        print(
            """
            --------
            |      |
            |      O
            |
            |
            |
            -
        """
        )
    elif life == 5:
        print(
            """
            --------
            |      |
            |      O
            |      |
            |      |
            |
            -
        """
        )
    elif life == 4:
        print(
            """
            --------
            |      |
            |      O
            |      |
            |      |
            |     /
            -
        """
        )
    elif life == 3:
        print(
            """
            --------
            |      |
            |      O
            |      |
            |      |
            |     / \\
            |
            -
        """
        )
    elif life == 2:
        print(
            """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     / \\
            |
            -
        """
        )
    elif life == 1:
        print(
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        """
        )
    else:
        print(
            """
            --------
            |      |
            |      O
            |    =====
            |     \\|/
            |      |
            |     / \\
            -
        """
        )


def random_word():
    """
    Generate a random word
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def construct(ans, orig, guess):
    """
    This function tries to construct the word based on the player's guess
    : param ans: str, the correct word
    : param orig: str, the orignal word
    : param guess: char, player's guess
    : return: str, the constructed word
    """
    tmp = ""
    for i in range(len(ans)):
        if guess == ans[i]:
            tmp += guess
        elif orig[i].isalpha():
            tmp += orig[i]
        else:
            tmp += "_"
    return tmp


def play(ans):
    """
    Main hangman function
    Let users guess a word in a limited amount of time
    : param ans: str, the correct word
    : return: bool, true if win, false if lose
    """
    life = N_TURNS
    print("The word looks like: " + "_" * len(ans))
    show_word = "_" * len(ans)

    while True:
        print("you have " + str(life) + " guesses left!")
        display(life)  # display hangman
        print("=============================")
        guess = str(input("Your guess: ")).upper()

        # if cannot find the guess char in the answer
        if guess not in ans:
            life -= 1
            print("There is no " + str(guess) + "'s in the word.")

        # construct word
        show_word = construct(ans, show_word, guess)
        print("The word looks like: " + str(show_word))

        # if got the right answer
        if show_word == ans:
            print("You got the correct answer!")
            return True

        # if use up all attemps
        if life == 0:
            display(life)
            print("Oh no you are dead:(")
            return False


def main():
    """
    The main function keep asking if the player wants to play a game
    Implement the hangman game
    Let users guess a word in a limited amount of time
    """
    print("Let's play Hangman!")
    word = random_word()
    play(word)

    # keep playing if the player wants to
    while input("\nPlay Again? (Y/N) ").upper() == "Y":
        print("\nLet's play Hangman!")
        word = random_word()
        play(word)


if __name__ == "__main__":
    main()
