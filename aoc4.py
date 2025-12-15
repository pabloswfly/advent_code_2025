import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=600)

file_path = "data/aoc4.txt"

ex = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def process_text(file):
    mat = np.array([list(line) for line in file.split("\n")[:-1]])
    mat = np.pad(mat, pad_width=1, mode="constant", constant_values=".")
    return mat


with open(file_path, "r") as file:
    # mat = process_text(ex)
    mat = process_text(file.read())

#################### TASK 1 ####################

res = 0

for i in range(1, mat.shape[0] - 1):
    for j in range(1, mat.shape[1] - 1):
        if mat[i, j] == ".":
            continue

        neighborhood = mat[i - 1 : i + 2, j - 1 : j + 2]
        # neighborhood minus the center cell which we know it's a @
        count = np.sum(neighborhood == "@") - 1
        if count < 4:
            res += 1

print(res)

#################### TASK 2 ####################

res = 0
prev_res = -1

while res != prev_res:

    prev_res = res

    for i in range(1, mat.shape[0] - 1):
        for j in range(1, mat.shape[1] - 1):
            if mat[i, j] == ".":
                continue

            neighborhood = mat[i - 1 : i + 2, j - 1 : j + 2]
            # neighborhood minus the center cell which we know it's a @
            count = np.sum(neighborhood == "@") - 1
            if count < 4:
                mat[i, j] = "."
                res += 1

print(res)
