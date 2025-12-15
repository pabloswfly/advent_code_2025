file_path = "data/aoc6.txt"

ex = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def process_text_part1(file):

    problems = []

    for line in file.split("\n"):

        vals = line.rstrip().split(" ")
        vals = [v for v in vals if v != ""]
        problems.append(vals)

    # Deal with empty lines
    problems = [p for p in problems if p != []]
    # Traspose the lists of list
    problems = list(map(list, zip(*problems)))

    return problems


def process_text_part2(file):

    problems = []

    # Parse the values from each line
    for line in file.split("\n"):
        vals = [c for c in line.rstrip()]
        vals = [v for v in vals if v != ""]
        problems.append(vals)

    # Deal with empty lines
    problems = [p for p in problems if p != []]

    # Assert that all lines have the same length
    longest = max([len(p) for p in problems])
    for i in range(len(problems)):
        while len(problems[i]) < longest:
            problems[i].insert(len(problems[i]), " ")

    # Keep a list of operations
    ops = problems[-1]
    ops = [op for op in ops if op != " "]
    ops = ops[::-1]

    # Traspose the lists of list and turn to right order
    problems = list(map(list, zip(*problems[:-1])))
    problems = problems[::-1]

    nums = []
    group = []

    # Convert lists to groups of integers
    for prob in problems:
        if all(p == " " for p in prob):
            nums.append(group)
            group = []
        else:
            group.append(int("".join(prob).strip()))
    nums.append(group)

    return nums, ops


def product(a):
    res = 1
    for n in a:
        res *= n
    return res


def apply_operation(nums, op):

    nums = [int(n) for n in nums]

    if op == "+":
        return sum(nums)
    elif op == "*":
        return product(nums)


#################### TASK 1 ####################

with open(file_path, "r") as file:
    problems = process_text_part1(file.read())
    # problems = process_text_part1(ex)

res = 0
for prob in problems:
    res += apply_operation(prob[:-1], prob[-1])
print(res)

#################### TASK 2 ####################

with open(file_path, "r") as file:
    # nums, ops = process_text_part2(ex)
    nums, ops = process_text_part2(file.read())

res = 0
for num, op in zip(nums, ops):
    res += apply_operation(num, op)
print(res)
