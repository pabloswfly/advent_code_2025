from collections import defaultdict


file_path = "data/aoc12.txt"

ex = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

from math import prod


def process_text(file: str) -> tuple[list[int], list[list[int]]]:
    areas = []
    presents = []

    for trees in file.split("\n\n")[-1:]:
        for line in trees.split("\n"):
            if line:
                size, *nums = line.split()
                area = prod([int(n) for n in size[:-1].split("x")])
                areas.append(area)
                presents.append(list(map(int, nums)))

    return areas, presents


#################### TASK 1 ####################

with open(file_path, "r") as file:
    # areas, presents = process_text(ex)
    areas, presents = process_text(file.read())

ok = sum([int(sum(pr) * 7 <= a) for a, pr in zip(areas, presents)])
print(ok)

#################### TASK 2 ####################
