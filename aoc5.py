file_path = "data/aoc5.txt"

ex = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def process_text(file: str) -> tuple:
    mode_ranges = True
    ranges = []
    ids = []

    for line in file.split("\n"):
        if line in ["", " "]:
            mode_ranges = False
            continue

        if mode_ranges:
            a, b = line.split("-")
            ranges.append([int(a), int(b)])

        else:
            ids.append(int(line))

    return ranges, ids


def find_overlaps(ranges: list) -> list:
    merged = []
    for r in sorted(ranges):
        if not merged or merged[-1][1] < r[0] - 1:
            merged.append(r)
        else:
            merged[-1][1] = max(merged[-1][1], r[1])
    return merged


with open(file_path, "r") as file:
    ranges, ids = process_text(file.read())
    # ranges, ids = process_text(ex)

#################### TASK 1 ####################

res = sum(any(a <= i <= b for a, b in ranges) for i in ids)
print(res)

#################### TASK 2 ####################

merged = find_overlaps(ranges)
res = sum([b - a + 1 for a, b in merged])
print(res)
