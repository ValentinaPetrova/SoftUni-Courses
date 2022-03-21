search = input()
text = input()

# isPresent = search in text - True
while search in text:
    text = text.replace(search, "")
#     triabva da vurnem text v starata promenliva

print(text)
