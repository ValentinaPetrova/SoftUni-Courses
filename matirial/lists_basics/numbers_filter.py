n = int(input())
my_list = []

for i in range(n):
    numbers = int(input())
    my_list.append(numbers)

word = input()
filtered = []

for numbers in my_list:
    if word == "even":
        if numbers % 2 == 0:
            filtered.append(numbers)
    if word == "odd":
        if numbers % 2 != 0:
            filtered.append(numbers)
    if word == "positive":
        if numbers >= 0:
            filtered.append(numbers)
    if word == "negative":
        if numbers < 0:
            filtered.append(numbers)
print(filtered)
