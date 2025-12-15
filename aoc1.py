file_path = "data/aoc1.txt"

ex = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

#################### TASK 1 ####################

with open(file_path, "r") as file:
    ops = [l.rstrip() for l in file]
    # ops = ex.strip().split("\n")
    direc = [o[0] for o in ops]
    nums = [int(o[1:]) for o in ops]

pos = 50
sign = {"L": -1, "R": 1}
res = 0

for d, n in zip(direc, nums):
    pos = (pos + n * sign[d]) % 100

    if pos == 0:
        res += 1

print(res)

#################### TASK 2 ####################

pos = 50
res = 0

for d, n in zip(direc, nums):
    prev = pos
    pos = pos + n * sign[d]

    # Count how many 0-crossings
    wraps = abs(pos // 100 - prev // 100)
    res += wraps

    if d == "L":
        if pos % 100 == 0:
            res += 1
        if prev % 100 == 0:
            res -= 1

print(res)
