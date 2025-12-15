import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=600)

file_path = "data/aoc9.txt"

ex = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


def process_text(file):
    reds = []

    for line in file.split("\n"):
        coor = line.rstrip().split(",")
        coor = [int(n) for n in coor if n != ""]
        if coor:
            reds.append(coor)

    return reds


def area(coor1, coor2):
    return abs(coor1[0] - coor2[0] + 1) * abs(coor1[1] - coor2[1] + 1)


with open(file_path, "r") as file:
    reds = process_text(ex)
    # reds = process_text(file.read())

#################### TASK 1 ####################


max_area = 0
for coor1 in reds:
    for coor2 in reds:
        if coor1 == coor2:
            continue

        max_area = max(max_area, area(coor1, coor2))

print(max_area)

#################### TASK 2 ####################


def diff(coor1, coor2):
    return [abs(coor1[0] - coor2[0]), abs(coor1[1] - coor2[1])]


reds.append(reds[0])

contour = [reds[0]]
for coor in reds[1:]:
    last = contour[-1]
    d = diff(coor, last)
    if d[0] == 0:
        smaller = min(last[1], coor[1]) + 1
        bigger = max(last[1], coor[1])
        for i in range(smaller, bigger):
            contour.append([coor[0], i])
    elif d[1] == 0:
        smaller = min(last[0], coor[0]) + 1
        bigger = max(last[0], coor[0])
        for i in range(smaller, bigger):
            contour.append([i, coor[1]])

    contour.append(coor)

# The last coordinate is going to be repeated
# at the beginning and at the end
contour = contour[:-1]


def get_mat(coors):
    height = max([c[1] for c in coors]) + 2
    width = max([c[0] for c in coors]) + 2

    mat = np.zeros((height, width), dtype=int)
    for coor in coors:
        mat[coor[1], coor[0]] = 1
    return mat


def fill(contour):
    max_x = max([c[1] for c in contour]) + 3
    max_y = max([c[0] for c in contour]) + 3
    fill = False

    shape = contour.copy()

    mat = get_mat(contour)
    mat = np.pad(mat, pad_width=1, mode="constant", constant_values=0)

    prev = 0

    for i in range(max_x):
        for j in range(max_y):
            print(i, j)
            if fill:
                if mat[i][j] == 0:
                    shape.append([j, i])
                elif mat[i][j] == 1:
                    if prev == 1:
                        continue
                    elif prev == 0:
                        fill = False

            else:
                if mat[i][j] == 1:
                    fill = True

    return shape


shape = fill(contour)
mat = get_mat(contour)
print(mat)

mat = get_mat(shape)
print(mat)

print(contour)
