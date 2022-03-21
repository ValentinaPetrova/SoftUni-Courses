characters = input().split(", ")
char_dict = {char: ord(char) for char in characters}
print(char_dict)

# for char in characters:
#     char_dict[char] = ord(char)
