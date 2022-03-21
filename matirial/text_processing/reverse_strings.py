text = input()

while text != "end":
    new_text = reversed(text)
    # for char in new_text:
    #     print(char, end="")
    reversed_text = "".join(new_text)
    print(f"{text} = {reversed_text}")
    text = input()
