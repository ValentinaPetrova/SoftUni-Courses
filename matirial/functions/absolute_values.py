numbers_list = input().split(" ")
abs_list = []

for n in numbers_list:
    current_abs = abs(float(n))
    abs_list.append(current_abs)

print(abs_list)
