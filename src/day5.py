from typing import List
import re
from collections import Counter

def get_start_end_points(s) -> List[str]:
    return [int(c) for c in re.split(r',| -> ', s)]
    
def is_diagonal(x1: int, y1: int, x2: int, y2: int) -> bool:
    return not (x1 == x2 or y1 == y2)

def get_points(x1: int, y1: int, x2: int, y2: int):
    if x1 == x2:
        step = int((y2 - y1) / abs(y2 - y1))
        return ((x1, y) for y in range(y1, y2 + step, step))
    elif y1 == y2:
        step = int((x2 - x1) / abs(x2 - x1))
        return ((x, y1) for x in range(x1, x2 + step, step))
    else:
        step_x = int((x2 - x1) / abs(x2 - x1))
        step_y = int((y2 - y1) / abs(y2 - y1))
        return ((x, y) for x, y in zip(range(x1, x2 + step_x, step_x), range(y1, y2 + step_y, step_y)))

def main():
    points = []
    with open("../data/day5", "r") as inputs:
        line = inputs.readline()
        while line:
            start_end = get_start_end_points(line)
            # Uncomment the following line and reindent for Part 1.
            # if not is_diagonal(*start_end):
            points = points + [point for point in get_points(*start_end)]
            line = inputs.readline()
    
    point_counts = Counter(points)
    print(sum(value > 1 for key, value in point_counts.items()))

if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    main()
