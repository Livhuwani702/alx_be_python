rows = 4
size = int(input("Enter the size of the pattern: "))

y = 1
while y <= rows:
    for j in range(1, size + 1):
        print("*", end=" ")
    print()
    y += 1
    size += 0
