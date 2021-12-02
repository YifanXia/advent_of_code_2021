"""
Advent of Code 2021: Day 2.
Use Python 3.10.x.
"""

from typing import Iterable, Tuple


def follow_path(path: Iterable) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    for step in path:
        match step:
            case ("forward", x):
                horizontal += x
            case ("up", y):
                depth -= y
            case ("down", y):
                depth += y
    return horizontal, depth

def follow_path_with_aim(path: Iterable) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    aim = 0
    for step in path:
        match step:
            case ("forward", x):
                horizontal += x
                depth += x * aim
            case ("up", y):
                aim -= y
            case ("down", y):
                aim += y
    return horizontal, depth

def get_step(input: str) -> Tuple[str, int]:
    input_l = input.strip().split()
    return input_l[0], int(input_l[1])

def main():
    
    with open("../data/day2", "r") as inputs:
        path = [
            get_step(input) 
            for input in inputs.readlines()
        ]
    end = follow_path(path)
    print(end[0] * end[1])

    end_with_aim = follow_path_with_aim(path)
    print(end_with_aim[0] * end_with_aim[1])


if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    main()

