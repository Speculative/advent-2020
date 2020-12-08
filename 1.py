from itertools import combinations

expenses = [int(n) for n in open("1.in", "r").read().splitlines()]

# Part 1
for expense in expenses:
    matching_expense = 2020 - expense
    if matching_expense in expenses:
        print("Part 1:", expense * matching_expense)
        break

# Part 2
for trio in combinations(expenses, 3):
    if sum(trio) == 2020:
        print("Part 2:", trio[0] * trio[1] * trio[2])
        break
