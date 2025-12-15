file_path = "data/aoc3.txt"
ex = """987654321111111
811111111111119
234234234234278
818181911112111"""

with open(file_path, "r") as file:
    banks = [line for line in file.read().rstrip().split("\n")]
# banks = [line for line in ex.strip().split("\n")]

#################### TASK 1 ####################

res = 0

for bank in banks:

    high = 0

    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            num = int(bank[i] + bank[j])
            high = max(high, num)

    res += high

print(res)


#################### TASK 2 ####################

count = 0

for bank in banks:

    num = [0]

    for i in range(len(bank)):

        digit = int(bank[i])
        insert = True

        min_idx = max(0, 12 - (len(bank) - i))

        for j in range(min_idx, len(num)):
            if digit > num[j]:
                num = num[: j + 1]
                num[j] = digit
                insert = False
                break

        if insert:
            num.append(digit)

    num = num[:12]
    num = int("".join([str(n) for n in num]))
    count += num

print(count)
