import re

iterations = int(input("Please eneter the no of rows: "))

for _ in range(iterations):
    user_in = input("Please enter in 'salary  taxes' format: ").strip()
    match = re.search(r"^([0-9]+)  ([0-9]+)$", user_in)
    if match:
        print(match.group(2))
    else:
        print("Errorr")
