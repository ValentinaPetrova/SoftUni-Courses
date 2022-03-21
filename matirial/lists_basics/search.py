number = int(input())
word = input()

strings = list()
filtered = []

for i in range(number):
    current_word = input()
    strings.append(current_word)
    if word in current_word:
        filtered.append(current_word)

print(strings)
print(filtered)
