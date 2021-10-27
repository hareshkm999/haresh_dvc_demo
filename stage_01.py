text = "this is demo"

with open("artifacts01.txt", "w+") as f:
    f.write(text)

print(text)