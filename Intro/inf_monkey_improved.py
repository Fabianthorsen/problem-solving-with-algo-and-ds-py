from random import choice
from string import ascii_lowercase
import sys


def generate_random_string(len: int) -> str:
    """Generate a random strings from the 26 letters in the alphabet and space

    Args:
        len (int): desired length of generated strings

    Returns:
        str: randomly generated string
    """
    return "".join(choice(ascii_lowercase + " ") for _ in range(len))


def score_string(guess: str, goal: str) -> float:
    """Scores a string against a goal string

    Args:
        guess (str): a string to be checked against the goal
        goal (str): the string to be checked against

    Returns:
        float: the score of the comparison in the range 0 - 1
    """
    score = 0
    for i in range(len(guess)):
        if guess[i] == goal[i]:
            score += 1
    return score / len(goal)


def main(goal: str) -> float:
    best_score = 0
    correct_guess = list(["_"] * len(goal))
    n_count = 0

    while True:
        n_count += 1
        string = generate_random_string(len(goal))

        for idx, letter in enumerate(string):
            if letter == goal[idx]:
                correct_guess[idx] = letter

                score = score_string("".join(correct_guess), goal)

                if score == 1.0:
                    print(n_count, "".join(correct_guess), score)
                    return score
                else:
                    if score > best_score:
                        best_score = score
                break

        if n_count % 5 == 0:
            print(n_count, "".join(correct_guess), best_score)


if __name__ == "__main__":
    main(sys.argv[1])
