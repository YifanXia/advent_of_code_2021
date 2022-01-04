from typing import Dict, List
from itertools import product, chain

Grid = List[List[int]]

def get_grid_dict(grid: Grid, n: int) -> Dict[complex, int]:
    return {
        complex(*coord): grid[coord[0]][coord[1]]
        for coord in product(range(n), repeat=2)
    }

def find_neighbours(loc: complex) -> List[complex]:
    def is_valid(ngb: complex):
        return (
            ngb.real >= 0
            and ngb.imag >= 0
            and ngb.real < 10
            and ngb.imag < 10
            and ngb != loc
        )
    neighbours = [complex(*rel_coord) + loc for rel_coord in product([-1, 0, 1], repeat=2)]
    return [ngb for ngb in neighbours if is_valid(ngb)]

def step(grid_dict: Dict[complex, int]) -> List[complex]:
    for coord in grid_dict:
       grid_dict[coord] += 1
    flashing = {coord for coord, energy in grid_dict.items() if energy > 9}
    flashed_set = set()
    while flashing:
        flashing_octo = flashing.pop()
        neighbours = find_neighbours(flashing_octo)
        for ngb in neighbours:
            if ngb not in flashed_set:
                grid_dict[ngb] += 1
                if grid_dict[ngb] > 9:
                    flashing.add(ngb)
        flashed_set.add(flashing_octo)
    for flashed_octo in flashed_set:
        grid_dict[flashed_octo] = 0
    return list(flashed_set)


def main():

    with open("../data/day11", "r") as file:    
        grid = [list(map(int, line.strip())) for line in file.readlines()]
    
    grid_dict = get_grid_dict(grid, len(grid))
    n_step = 0
    total_flashes = 0
    while True:
        flashed_step = step(grid_dict)
        total_flashes += len(flashed_step)
        n_step += 1
        # Part 1
        if n_step == 100:
            print(total_flashes)
        # Part 2
        if len(flashed_step) == 100:
            print(n_step)
            break

        
    

if __name__ == "__main__":
    import os
    try:
        os.chdir(os.path.dirname(__file__))
        main()
    finally:
        os.chdir("../")