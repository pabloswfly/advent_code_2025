file_path = "data/aoc7.txt"

ex = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def lookup(c: chr, s: str) -> list:
    return [i for i, char in enumerate(s) if char == c]


def process_beams(file: str) -> tuple:
    first = file.split("\n")[0]
    beams = lookup("S", first)
    orig = beams[0]
    active_splits = []

    line_len = len(file.split("\n")[0])

    for j, line in enumerate(file.split("\n")[2::2]):
        split_pos = lookup("^", line)
        if len(split_pos) > 0:
            for i, b in enumerate(beams):
                if b in split_pos:
                    active_splits.append([j, b])
                    beams[i] = b - 1
                    beams.insert(i + 1, b + 1)

        beams = sorted(list(set(beams)))

    return active_splits, line_len, orig


def walk_levels(pos: int, level: int, active_splits: list, origin: list) -> int:
    level_splits = [s for s in active_splits if s[0] == level]

    res = 0

    # Base case: reached origin level
    if level == -1:
        return 1 if pos == origin[1] else 0

    if any(ls[1] == pos - 1 for ls in level_splits):
        res += walk_levels(pos - 1, level - 1, active_splits, origin)
    if any(ls[1] == pos + 1 for ls in level_splits):
        res += walk_levels(pos + 1, level - 1, active_splits, origin)

    res += walk_levels(pos, level - 1, active_splits, origin)

    return res


#################### TASK 1 ####################

with open(file_path, "r") as file:
    n_splits = len(process_beams(file.read())[0])
    # n_splits = len(process_beams(ex)[0])
print(n_splits)


#################### TASK 2 ####################

with open(file_path, "r") as file:
    active_splits, line_len, orig = process_beams(file.read())
    # active_splits, line_len, orig = process_beams(ex)

max_depth = max(s[0] for s in active_splits)
beam = [0] * line_len
beam[orig] = 1

for level in range(max_depth + 1):
    level_splits = [s for s in active_splits if s[0] == level]
    for split in level_splits:
        _, pos = split
        beam[pos - 1] += beam[pos]
        beam[pos + 1] += beam[pos]
        beam[pos] = 0

print(sum(beam))
