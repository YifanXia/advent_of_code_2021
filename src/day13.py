from typing import List, Tuple
from itertools import product

def decode(n: int) -> str:
    return "#" if n == 1 else " "

def fold(grid: List[List[bool]], step: Tuple[str, int]) -> List[List[bool]]:
    match step:
        case ("x", x_fold):
            new_grid = [[0 for _ in range(x_fold)] for _ in range(len(grid))]
            for y, x in product(range(len(grid)), range(x_fold)):
                new_grid[y][x] = grid[y][x] | grid[y][2 * x_fold - x]
            return new_grid
        case ("y", y_fold):
            new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(y_fold)]
            for y, x in product(range(y_fold), range(len(grid[0]))):
                new_grid[y][x] = grid[y][x] | grid[2 * y_fold - y][x]
            return new_grid
            

def main():
    import pprint
    with open("../data/day13", "r") as file:
        coordinates = []
        instructions = []
        line = file.readline()
        x_max = y_max = 0
        while line != "\n":
            x, y = [int(c) for c in line.strip().split(",")]
            coordinates.append((x, y))
            line = file.readline()
        line = file.readline()
        while line:
            fold_along = line.strip().split(" ")[-1].split("=")
            instructions.append((fold_along[0], int(fold_along[1])))
            line = file.readline()
    
    x_max = instructions[0][1] * 2
    y_max = instructions[1][1] * 2
    grid = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for x, y in coordinates:      
        grid[y][x] = 1

    for step_n, step in enumerate(instructions):
        grid = fold(grid, step)
        if step_n == 0:
            print(sum((sum(n for n in grid[m]) for m in range(len(grid)))))
    
    for row in grid:
        print("".join(decode(n) for n in row))

if __name__ == "__main__":
    import os
    try:
        os.chdir(os.path.dirname(__file__))
        main()
    finally:
        os.chdir("../")