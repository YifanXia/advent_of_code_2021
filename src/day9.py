
from typing import List, Set, Tuple
from math import prod


Grid = List[List[int]]

PAD_VALUE = 9

def pad_num(grid: Grid) -> Grid:
    padded_grid = grid.copy()
    padded_grid.insert(0, [PAD_VALUE] * len(grid[0]))
    padded_grid.append([PAD_VALUE] * len(grid[0]))
    for row in padded_grid:
        row.insert(0, PAD_VALUE)
        row.append(PAD_VALUE)
    return padded_grid

def find_low_points(padded_grid: Grid) -> List[Tuple[int, int]]:
    low_points = []
    n_rows = len(padded_grid)
    n_cols = len(padded_grid[0])
    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            is_low = all([
                padded_grid[i][j] < padded_grid[i - 1][j],
                padded_grid[i][j] < padded_grid[i + 1][j],
                padded_grid[i][j] < padded_grid[i][j - 1],
                padded_grid[i][j] < padded_grid[i][j + 1],
            ])
            if is_low:
                low_points.append((i, j))
    
    return low_points

def is_in_basin(point: Tuple[int, int], padded_grid: Grid, basin_points: Set[Tuple[int, int]]) -> bool:
    if padded_grid[point[0]][point[1]] >= 9:
        return False
    x, y = point
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return all(
        padded_grid[point[0]][point[1]] <= padded_grid[p[0]][p[1]] 
        for p in neighbors 
        if p not in basin_points
    )

def find_basin(point: Tuple[int, int], padded_grid: Grid) -> Set[Tuple[int, int]]:
    visited = set()
    points = [point]
    while points:
        current = points.pop()
        if is_in_basin(current, padded_grid, visited):
            for p in [
                (current[0] + 1, current[1]),
                (current[0] - 1, current[1]),
                (current[0], current[1] + 1),
                (current[0], current[1] - 1),
            ]:
                if p not in visited:
                    points.append(p)
            visited.add(current)
    return visited
            
            


def main():

    with open("../data/day9", "r") as file:
        inputs = file.readlines()
    grid = [
        [int(d) for d in digits.strip()] for digits in inputs
    ]
    padded_grid = pad_num(grid)
    low_points = find_low_points(padded_grid)
    print(sum(padded_grid[i][j] + 1 for i, j in low_points))

    basin_sizes = [len(find_basin(low_point, padded_grid)) for low_point in low_points]
    print(basin_sizes)
    basin_sizes.sort(reverse=True)
    print(basin_sizes)
    print(prod(basin_sizes[:3]))

if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    main()
    os.chdir("../")