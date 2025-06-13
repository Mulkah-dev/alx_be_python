try:
    file = open("sample.py", "r")
    contents = file.read()
    print(contents)

except FileNotFoundError:
    print("file does not exist")

