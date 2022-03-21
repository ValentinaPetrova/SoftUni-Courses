numbers = input(). split(", ")
numbers = list(map(int, numbers))
even_index = []
# even_index = map(lambda num: , numbers)

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_index.append(i)

print(even_index)