words = input().split(" ")
palindrome_list = []
palindrome = input()

for word in words:
    rev_list = reversed(word)
    rev_word = "".join(rev_list)
    if rev_word == word:
        palindrome_list.append(word)

print(palindrome_list)
palindrome_count = words.count(palindrome)
print(f"Found palindrome {palindrome_count} times")
