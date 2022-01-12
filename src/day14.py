from typing import Dict, List
from collections import Counter

def unit_polymerize(left: str, rules: Dict[str, str]) -> List[str]:
    right = rules.get(left)
    result = list(left)
    if right:
        result.insert(1, right)
    return result

def step(template: str, rules: Dict[str, str]) -> str:
    new_template_list = []
    new_template_list.append(template[0])
    for i in range(1, len(template)):
        left = template[i-1:i+1]
        new_template_list += unit_polymerize(left, rules)[1:]
    return "".join(new_template_list)

def polymerize(template: str, rules: Dict[str, str], steps: int) -> str:
    for _ in range(steps):
        template = step(template, rules)
    return template

def main():
    reactions = {}

    with open("../data/day14", "r") as file:
        data = file.read().strip()
    
    template, reactions_s = data.split("\n\n")
    template = template.strip()
    for reac in reactions_s.split("\n"):
        left, right = reac.split(" -> ")
        reactions[left] = right
        
    new_template = polymerize(template, reactions, 10)
    polymer_counts = Counter(list(new_template)).most_common()
    print(polymer_counts[0][1] - polymer_counts[-1][1])

    new_template = polymerize(template, reactions, 40)
    polymer_counts = Counter(list(new_template)).most_common()
    print(polymer_counts[0][1] - polymer_counts[-1][1])



        

if __name__ == "__main__":
    import os
    try:
        os.chdir(os.path.dirname(__file__))
        main()
    finally:
        os.chdir("../")