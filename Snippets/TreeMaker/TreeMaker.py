treeHeight = int(input("How Tall Is The Tree : "))

spaces = treeHeight - 1

hashes = 1

stumpSpaces = treeHeight - 1

while treeHeight != 0:

    for i in range(spaces):
        print(" ", end="")

    for i in range(hashes):
        print("#", end="")

    print()
    spaces -= 1
    hashes += 2
    treeHeight -= 1

for i in range(stumpSpaces):
    print(" ", end="")

print("#")
