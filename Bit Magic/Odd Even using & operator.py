def check(num):
    if num & 1 == 1:
        return "Odd"
    return "Even"

for i in range(11):
    print("Number ",i,"is",check(i))

