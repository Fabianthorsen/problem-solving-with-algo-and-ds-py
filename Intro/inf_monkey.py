from random import choice
from string import ascii_lowercase
import sys


def generate_random_string(len: int) -> str:
    return "".join(choice(ascii_lowercase + " ") for _ in range(len))


def score_string(guess: str, goal: str) -> float:
    score = 0
    for i in range(len(guess)):
        if guess[i] == goal[i]:
            score += 1
    return score / len(goal)


def main(goal: str) -> float:
    best_score = 0
    best_string = ""
    n_count = 0
    while True:
        n_count += 1
        gen_string = generate_random_string(len(goal))
        score = score_string(gen_string, goal)
        if best_score == 1.0:
            return score
        elif score > best_score:
            best_score = score
            best_string = gen_string
        if n_count % 1000 == 0:
            print(n_count, best_string, best_score)


if __name__ == "__main__":
    main(sys.argv[1])
