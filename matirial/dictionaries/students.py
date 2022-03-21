text = input()
courses = {}

while ":" in text:

    # like tuple -> (name, id, course = text.split(":")
    data = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in courses.keys():
        courses[course] = {}

    courses[course][id] = name

    text = input()

text = text.replace("_", " ")

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")
