from collections import Counter
from itertools import chain
from typing import List, Tuple


OPENNING_MATCHINGS = {
    ")": "(",
    "}": "{",
    ">": "<",
    "]": "[",
}

ILLEGAL_SCORES = {
    ")": 3,
    "}": 1197,
    ">": 25137,
    "]": 57,
}


# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.

INCOMPLETE_SCORES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def find_illegals(line: str) -> Tuple[bool, List[str]]:
    opennings = []
    illegals = []
    for c in line:
        if c in "({[<":
            opennings.append(c)
        if c in ")}]>":
            if opennings.pop() != OPENNING_MATCHINGS[c]:
                illegals.append(c)
    if illegals:
        return True, illegals
    else:
        return False, opennings

def main():

    with open("../data/day10", "r") as file:
        inputs = file.readlines()
    
    illegals, opennings = [], []
    for line in inputs:
        is_corrupted, characters = find_illegals(line)
        if is_corrupted:
            illegals.append(characters)
        else:
            opennings.append(characters)
    illegal_counts = Counter(list(chain.from_iterable(illegals)))
    print(sum(ILLEGAL_SCORES[c] * illegal_counts[c] for c in illegal_counts))
    
    autocompletion_scores = [0] * len(opennings)
    for id, line in enumerate(opennings):
        for c in reversed(line):
            autocompletion_scores[id] = autocompletion_scores[id] * 5 + INCOMPLETE_SCORES[c]
    autocompletion_scores.sort()
    print(autocompletion_scores[len(autocompletion_scores) // 2])
    

if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    main()
    os.chdir("../")
