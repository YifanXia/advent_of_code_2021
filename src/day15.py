from typing import DefaultDict, List, Set, Tuple
from copy import deepcopy
from collections import defaultdict
from heapq import heapify, heappop, heappush, nsmallest

LOWEST_RISK = {}

def increment_risk(risk: int, delta: int) -> int:
    if (r := risk + delta) > 9:
        return r - 9
    else:
        return r

def get_neighbours(coord: Tuple[int, int], n_cols: int, n_rows: int) -> Set[Tuple[int, int]]:
    match coord:
        case (0, 0):
            return {(1, 0), (0, 1)}
        case (0, col) if col == n_cols - 1:
            return {(0, col - 1), (1, col)}
        case (0, col):
            return {(0, col - 1), (0, col + 1), (1, col)}
        case (row, 0) if row == n_rows - 1:
            return {(row, 1), (row - 1, 0)}
        case (row, 0):
            return {(row - 1, 0), (row + 1, 0), (row, 1)}
        case (row, col) if row == n_rows - 1 and col == n_cols - 1:
            return {(row - 1, col), (row, col - 1)}
        case (row, col) if row == n_rows - 1:
            return {(row, col + 1), (row, col - 1), (row - 1, col)}
        case (row, col) if col == n_cols - 1:
            return {(row + 1, col), (row - 1, col), (row, col - 1)}
        case (row, col):
            return {(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)}
        

def compute_least_risky_path(
    start: Tuple[int, int], end: Tuple[int, int], risk: List[List[int]]
) -> int:
    n_cols = len(risk[0])
    n_rows = len(risk)
    least_risky_paths = defaultdict(lambda: float("inf"), {start: 0})
    visited = set()
    current = start
    while current != end:
        neighbours = get_neighbours(current, n_cols, n_rows)
        for ngb in neighbours:
            if ngb not in visited:
                least_risky_paths[ngb] = min(least_risky_paths[ngb], least_risky_paths[current] + risk[ngb[0]][ngb[1]])
        del least_risky_paths[current]
        visited = visited | {current}
        current = nsmallest(1, least_risky_paths.keys(), key=lambda c: least_risky_paths[c])[0]
    return least_risky_paths[end]
        


def assess_risk(coord: Tuple[int, int], risk: List[List[int]]) -> int:
    if coord in LOWEST_RISK:
        return LOWEST_RISK[coord]
    match coord:
        case (0, 0):
            total_risk = 0
        case (0, col):
            total_risk = risk[0][col] + assess_risk((0, col - 1), risk)
        case (row, 0):
            total_risk = risk[row][0] + assess_risk((row - 1, 0), risk)
        case (row, col):
            total_risk = risk[row][col] + min(
                assess_risk((row, col - 1), risk),
                assess_risk((row - 1, col), risk)
            )
    LOWEST_RISK[coord] = total_risk
    return total_risk

def extend_grid(grid: List[List[int]]) -> List[List[int]]:
    int_grid = deepcopy(grid)
    for i in range(1, 5):
        for new_row, row in zip(int_grid, grid):
            new_row += [increment_risk(r, i) for r in row]
    final_grid = deepcopy(int_grid)
    for i in range(1, 5):
        final_grid += [[increment_risk(r, i) for r in row] for row in int_grid]
    return final_grid

def main():

    grid = []
    with open("../data/day15", "r") as file:
        line = file.readline().strip()
        while line:
            grid.append([int(r) for r in list(line)])
            line = file.readline().strip()

    
    coord_dest = (len(grid) - 1, len(grid[0]) - 1)
    print(compute_least_risky_path((0, 0), coord_dest, grid))

    extended = extend_grid(grid)
    extend_coord_dest = (len(extended) - 1, len(extended[0]) - 1)
    print(compute_least_risky_path((0, 0), extend_coord_dest, extended))

        

if __name__ == "__main__":
    import os
    try:
        os.chdir(os.path.dirname(__file__))
        main()
    finally:
        os.chdir("../")