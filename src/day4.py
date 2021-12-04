from typing import List, Set, Tuple
from itertools import chain

Board = List[List[int]]

def get_data() -> Tuple[List[int], List[Board]]:
    with open("../data/day4", "r") as inputs:
        nums_s = inputs.readline()
        nums = [int(num) for num in nums_s.strip().split(",")]
        inputs.readline()
        row = inputs.readline()
        matrices = []
        matrix = []
        while row:
            if row == "\n":
                matrices.append(matrix)
                matrix = []
            else:
                matrix.append([int(n) for n in row.strip().split()])
            row = inputs.readline()
        matrices.append(matrix)
    return nums, matrices

def check_rows(matrix: Board, nums: Set[int]) -> bool:
    return any(
        set(row).issubset(nums) for row in matrix
    )

def check_columns(matrix: Board, nums: Set[int]):
    return any(
        set(col).issubset(nums) for col in zip(*matrix)
    )

def find_winning_board(nums: List[int], mats: List[Board]) -> Tuple[Board, Set[int], int]:
    for i in range(5, len(nums) + 1):
        nums_set = set(nums[:i])
        for j, mat in enumerate(mats):
            if check_rows(mat, nums_set) or check_columns(mat, nums_set):
                return mat, nums_set, nums[i-1]

def find_last_winning_board(nums: List[int], mats: List[Board]) -> Tuple[Board, Set[int], int]:
    for i in range(len(nums) + 1, 0, -1):
        nums_set = set(nums[:i])
        for mat in mats:
            if not check_rows(mat, nums_set) and not check_columns(mat, nums_set):
                nums_set.add(nums[i])
                return mat, nums_set, nums[i]

def main():
    nums, matrices = get_data()
    board, numbers, last = find_winning_board(nums, matrices)
    last_board, last_numbers, last_last = find_last_winning_board(nums, matrices)
    flat_board = set(n for n in chain.from_iterable(board))
    last_flat_board = set(n for n in chain.from_iterable(last_board))
    sum_unmarked = sum(flat_board.difference(numbers))
    sum_unmarked_last = sum(last_flat_board.difference(last_numbers))
    print(sum_unmarked * last)
    print(sum_unmarked_last * last_last)
    


if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    main()