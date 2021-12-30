def number_of_descendents(days_left: int, total_n_days: int) -> int:
    if total_n_days <= days_left:
        return 0
    if days_left == 8:
        days_left -= 2
        total_n_days -= 2
    direct_descendents = 1 + (total_n_days - days_left - 1) // 7
    undirect_descendents = 0
    n_days_first_dd = total_n_days - days_left - 1
    for i in range(0, direct_descendents):
        undirect_descendents += number_of_descendents(8, n_days_first_dd - i * 7)
    return undirect_descendents + direct_descendents

def main():
    with open("../data/day6", "r") as inputs:
        line = inputs.readline().split(",")
        print(line)
        fish = list(map(int, line))
    descendents = [number_of_descendents(days_left, 256) for days_left in fish]
    print(len(fish))
    print(sum(descendents) + len(fish))

if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    main()