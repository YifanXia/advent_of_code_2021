"""Advent of Code 2021: Day 3."""

from typing import Iterable, Tuple
from collections import Counter
from itertools import tee

def find_most_common(bits: Iterable[str]):
    counts = Counter(bits)
    return int(counts["1"] >= counts["0"])

def find_gamma_and_epsilon(bits: Tuple[str]) -> Tuple[str]:
    gamma = find_most_common(bits)
    epsilon = 1 - gamma
    return str(gamma), str(epsilon)

def find_gamma_and_epsilon_rates(matrix: Iterable[Tuple[str]]) -> Tuple[str]:
    gamma_r = epsilon_r = ""

    for bits in matrix:
        g, e = find_gamma_and_epsilon(bits)
        gamma_r += g
        epsilon_r += e

    return int(gamma_r, 2), int(epsilon_r, 2)


def find_oxygen_rate(matrix_input: Iterable[Tuple[str]]):
    matrix = matrix_input
    n = len(matrix[0])
    for i in range(n):
        bits = [binary[i] for binary in matrix]
        most_common = str(find_most_common(bits))
        indices = list(filter(lambda j: bits[j] == most_common, range(len(matrix))))
        #breakpoint()
        matrix = [matrix[k] for k in indices]
        if len(matrix) == 1:
            return matrix[0]

def find_co2_rate(matrix_input: Iterable[Tuple[str]]):
    matrix = matrix_input
    n = len(matrix[0])
    for i in range(n):
        bits = [binary[i] for binary in matrix]
        least_common = str(1 - find_most_common(bits))
        indices = list(filter(lambda j: bits[j] == least_common, range(len(matrix))))
        #breakpoint()
        matrix = [matrix[k] for k in indices]
        if len(matrix) == 1:
            return matrix[0]
    
    
    
def main():

    with open("../data/day3", "r") as inputs:
        list_of_strings = inputs.readlines()
        matrix = [
            [
                str(digit) for digit in binary.strip()
            ] for binary in list_of_strings
        ]

        t_matrix_p1, t_matrix_p2 = tee(zip(*matrix))

        gamma_r, epsilon_r = find_gamma_and_epsilon_rates(t_matrix_p1)
        
        print(gamma_r * epsilon_r)
        oxygen_rate = find_oxygen_rate(list_of_strings)
        co2_rate = find_co2_rate(list_of_strings)
        print(int(oxygen_rate, 2) * int(co2_rate, 2))
    

if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    main()