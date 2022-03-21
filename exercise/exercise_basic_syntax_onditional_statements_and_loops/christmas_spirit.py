quantity = int(input())
days = int(input())
christmas_spirit = 0
costs = 0
condition_5th_day = False

for day in range(1, days +1):
    condition_5th_day = False
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        christmas_spirit += 5
        costs += 2 * quantity
    if day % 3 == 0:
        christmas_spirit += 13
        costs += (5 * quantity) + (3 * quantity)
        condition_5th_day = True

    if day % 5 == 0:
        christmas_spirit += 17
        costs += quantity * 15
        if condition_5th_day:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        costs += 23

        if day == days:
            christmas_spirit -= 30

print(f"Total cost: {costs}")
print(f"Total spirit: {christmas_spirit}")
