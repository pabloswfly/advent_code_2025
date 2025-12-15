from collections import defaultdict
from z3 import *

import random


file_path = "data/aoc10.txt"

ex = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def process_text(file):

    machines = []

    for line in file.split("\n"):

        splitted = line.rstrip().split(" ")

        diagram = splitted[0][1:-1]
        diagram = [0 if n == "." else 1 for n in diagram]

        joltage = splitted[-1]
        joltage = [int(n) for n in joltage[1:-1].split(",") if n != ""]

        buttons = [b for b in splitted[1:-1]]
        buttons = [btn[1:-1].split(",") for btn in buttons]
        buttons = [[int(n) for n in btn] for btn in buttons]

        if buttons:
            machines.append([diagram, joltage, buttons])

    return machines


def on_indeces(diagram):
    return [i for i, ch in enumerate(diagram) if ch == 1]


def switch(diagram, index):
    diagram[index] = 1 - diagram[index]


def add(diagram, index):
    diagram[index] += 1


def simulate(diagram, buttons, n=100):

    min_n = 1000

    for _ in range(n):
        lights = [0] * len(diagram)

        seq = random.sample(buttons, k=len(buttons))
        for i, btn in enumerate(seq):
            for index in btn:
                switch(lights, index)
            if lights == diagram:
                min_n = min(min_n, i + 1)
                break

    return min_n


def solve_joltage(buttons, joltage):

    opt = Optimize()

    # Each button press is an integer with positive values
    btn_vars = [Int(f"b{i}") for i in range(len(buttons))]
    for var in btn_vars:
        opt.add(var >= 0)

    # Optimize the sum of button presses to match the joltage
    for pos, j in enumerate(joltage):
        affects = []
        for idx, btn in enumerate(buttons):
            if pos in btn:
                affects.append(btn_vars[idx])
        opt.add(Sum(affects) == j)

    opt.minimize(Sum(btn_vars))

    if opt.check() == sat:
        model = opt.model()
        return sum(model[c].as_long() for c in btn_vars)
    else:
        raise ValueError("No solution found")


with open(file_path, "r") as file:
    # machines = process_text(ex)
    machines = process_text(file.read())

#################### TASK 1 ####################

res = 0
for mach in machines:
    diagram, _, buttons = mach
    min_n = simulate(diagram, buttons, n=10000)
    res += min_n

print(res)

#################### TASK 2 ####################

res = 0
for mach in machines:
    _, joltage, buttons = mach
    res += solve_joltage(buttons, joltage)
print(res)
