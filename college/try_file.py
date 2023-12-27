import re

# with open("myfile.txt", "r") as f:
#     # f.write("abc\n")
#     # f.write("def\n")
#     for line in f:
#         ...


# def classify_input(input):
#     url = re.search(r"^(https://)?(w+).(w+).com|in", "https://www.google.com")
#     if url:
#         print(True)


url = re.search(r"^(https://)?www\.(\w\.+)\.com|in$", "http://www.djsce.ac.in")
if url:
    print(True, url.group(2))
else:
    print(False)
