from collections import defaultdict
from typing import DefaultDict, List, Set

def find_path(start: str, visited: Set, adjacency_list: DefaultDict[str, Set], allow_twice: bool = False) -> List[List[str]]:
    if start == "end":
        return [[start]]
    res = []
    neighbours = adjacency_list[start]
    for node in neighbours:
        allow_twice_next = allow_twice
        if node.islower() and node in visited:
            if not allow_twice or node == "start":
                continue
            allow_twice_next = False    
        paths = [
            [start] + path
            for path in find_path(node, visited.union({start}), adjacency_list, allow_twice_next)
        ]
        res = res + paths
    return res
        



def main():

    adjacency_list = defaultdict(set)

    with open("../data/day12", "r") as file:    
        line = file.readline()
        while line:
            a, b = line.strip().split("-")
            adjacency_list[a].add(b)
            adjacency_list[b].add(a)
            line = file.readline()
    
    res_1 = find_path("start", set(), adjacency_list)
    print(len(res_1))
    res_2 = find_path("start", set(), adjacency_list, True)
    print(len(res_2))

if __name__ == "__main__":
    import os
    try:
        os.chdir(os.path.dirname(__file__))
        main()
    finally:
        os.chdir("../")