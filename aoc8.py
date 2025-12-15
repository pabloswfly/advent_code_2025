from collections import Counter
from math import prod


file_path = "data/aoc8.txt"

ex = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def process_text(file: str) -> list:
    nums = []

    for line in file.split("\n"):
        num = line.rstrip().split(",")
        num = [int(n) for n in num if n != ""]
        nums.append(num)

    return nums


def distance(a: list, b: list) -> float:
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def coor2str(a: list) -> str:
    return ",".join([str(x) for x in a])


def str2coor(s: str) -> list:
    return [int(x) for x in s.split(",")]


with open(file_path, "r") as file:
    nums = process_text(file.read())
    # nums = process_text(ex)

dist2boxes = {}

for a in nums:
    for b in nums:
        if a == b:
            continue
        dist = distance(a, b)
        dist2boxes[dist] = (coor2str(a), coor2str(b))

#################### TASK 1 ####################

networks = [[coor2str(n)] for n in nums]
sorted_dic = sorted(dist2boxes.keys())

for dist in sorted_dic[:1000]:
    a, b = dist2boxes[dist]

    for net in networks:
        if a in net and b not in net:
            for other in networks:
                if net != other and b in other:
                    net.extend(other)
                    networks.remove(other)
                    break
        elif b in net and a not in net:
            for other in networks:
                if net != other and a in other:
                    net.extend(other)
                    networks.remove(other)
                    break

# count the length of each network
lengths = [len(net) for net in networks]
count = Counter(lengths)

# get the sizes of the three largest networks from the counter
largest = sorted(count.keys(), reverse=True)[:3]

res = prod(largest)
print(res)


#################### TASK 2 ####################

networks = [[coor2str(n)] for n in nums]

sorted_dic = sorted(dist2boxes.keys())
for dist in sorted_dic:
    a, b = dist2boxes[dist]

    for net in networks:
        if a in net and b not in net:
            for other in networks:
                if net != other and b in other:
                    net.extend(other)
                    networks.remove(other)
                    break

        elif b in net and a not in net:
            for other in networks:
                if net != other and a in other:
                    net.extend(other)
                    networks.remove(other)
                    break

    if len(networks) == 1:
        res = str2coor(a)[0] * str2coor(b)[0]
        break

print(res)
