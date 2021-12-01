"""Advent of Code 2021: Day 1."""

from typing import List

def get_increases(measurements: List[int], gap: int = 1) -> int:
    increases = [
        a < b for a, b in zip(measurements[:-1], measurements[gap:])
    ]
    return sum(increases)

def get_sum_of_three(measurements: List[int]) -> List[int]:
    sums = [
        a + b + c 
        for a, b, c in zip(measurements[:-2], measurements[1:-1], measurements[2:])
    ]
    return sums

if __name__ == "__main__":

    with open("/home/yifan_xia/advent_of_code/2021/data/day1", "r") as input:
        measurements = list(map(int, input.readlines()))
    print(get_increases(measurements))

    sums = get_sum_of_three(measurements)
    print(get_increases(sums))
    print(get_increases(measurements, gap=3))