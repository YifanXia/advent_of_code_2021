from itertools import chain
from os import read
from typing import Callable, Dict, Optional

MATCHING_FUNCS = []

def parse_output(output: str) -> int:
    return len(output)

def is_in(small: str, big: str) -> bool:
    return all(
        l in big for l in small
    )

def sort_string(unsorted: str) -> str:
    return "".join(sorted(unsorted))
    
def get_1478(s: str, *args) -> Optional[int]:
    match len(s):
        case 2:
            return 1
        case 3:
            return 7
        case 4:
            return 4
        case 7:
            return 8
        case _:
            return None

def get_3(s: str, matched: Dict, *args) -> Optional[int]:
    if len(s) == 5 and is_in(matched[1], s):
        return 3
    return None

def get_690(s: str, matched: Dict, *args) -> Optional[int]:
    if len(s) == 6:
        if is_in(matched[7], s) and not is_in(matched[3], s):
            return 0
        if is_in(matched[7], s) and is_in(matched[3], s):
            return 9
        if not is_in(matched[7], s) and not is_in(matched[3], s):
            return 6
    return None

def get_25(s: str, matched: Dict, *args) -> Optional[int]:
    if len(s) == 5:
        if is_in(s, matched[9]):
            return 5
        return 2
    return None

MATCHING_FUNCS = [
    get_1478,
    get_1478,
    get_1478,
    get_1478,
    get_3,
    get_690,
    get_690,
    get_690,
    get_25,
    get_25,
]

def match_pattern(patterns_s: str) -> Dict:
    matched_pattern = {}
    patterns = patterns_s.split()
    for func in MATCHING_FUNCS:
        for id, pattern in enumerate(patterns):
            if (digit := func(pattern, matched_pattern)) != None:
                matched_pattern[digit] = pattern
                patterns = [p for p in patterns if p != pattern]
                # breakpoint()
                break
    # for pattern in patterns.split():
    #     for func in MATCHING_FUNCS:
    #         if digit := func(pattern, matched_pattern):
    #             matched_pattern[digit] = pattern
    #             break
    assert len(matched_pattern) == 10
    return {sort_string(s): d for d, s in matched_pattern.items()}

def decrypt_output(matched_pattern: Dict, output: str) -> int:
    return int("".join(str(matched_pattern[sort_string(s)]) for s in output.split()))

def main():

    patterns, outputs = [], []

    with open("../data/day8", "r") as inputs:
        line = inputs.readline()
        while line:
            pattern, output = line.split("|")
            patterns.append(pattern.strip())
            outputs.append(output.strip())
            line = inputs.readline()

    # part 1
    print(sum(get_1478(s) is not None for output in outputs for s in output.split()))
    # part 2
    digits = []
    for pattern, output in zip(patterns, outputs):
        matched_pattern = match_pattern(pattern)
        output_digit = decrypt_output(matched_pattern, output)
        digits.append(output_digit)
    print(sum(digits))

if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    main()