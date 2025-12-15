file_path = "data/aoc2.txt"

ex = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

with open(file_path, "r") as file:
    ranges = file.read().rstrip().split(",")
    # ranges = ex.strip().split(",")

#################### TASK 1 ####################

count = 0

for rng in ranges:
    p1, p2 = rng.split("-")
    for n in range(int(p1), int(p2) + 1):
        n = str(n)
        half1, half2 = n[: len(n) // 2], n[len(n) // 2 :]
        if half1 == half2:
            count += int(n)

print(count)


#################### TASK 2 ####################

count = 0

for rng in ranges:
    p1, p2 = rng.split("-")
    for n in range(int(p1), int(p2) + 1):
        n = str(n)
        for length in range(1, len(n) // 2 + 1):
            digits = [int(n[i : i + length]) for i in range(0, len(n), length)]

            # If the digits are all the same
            if len(set(digits)) == 1:
                count += int(n)
                break

print(count)
