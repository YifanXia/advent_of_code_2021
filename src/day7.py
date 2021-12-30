import math
from typing import List

def find_median(nums: List[int]):
    nums.sort()
    l = len(nums)
    if l % 2 == 1:
        return nums[l // 2]
    else:
        n1, n2 = nums[l // 2 - 1], nums[l // 2]
        mean_2 = (n1 + n2) / 2.0
        diffs = [abs(n1 - mean_2), abs(n2 - mean_2)]
        return n1 if diffs[0] < diffs[1] else n2

def compute_fuel_consumption(start: int, end: int, weighted: bool = False):
    if weighted:
        return sum(dis for dis in range(1, abs(start - end) + 1))
    else: 
        return abs(start - end)

def brute_force(nums: List[int], weighted: bool = False) -> int:
    min = float("inf")
    for spot in range(max(nums) + 1):
        total_fuel = sum(compute_fuel_consumption(start, spot, weighted) for start in nums)
        if total_fuel < min:
            min = total_fuel
    return min

def main():
    with open("../data/day7", "r") as inputs:
        nums = list(map(int, inputs.read().split(",")))
    median = find_median(nums)
    print(sum(abs(n - median) for n in nums))
    print(brute_force(nums))

        

if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    main()