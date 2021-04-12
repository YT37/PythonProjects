def main():
    try:
        treeHeight = int(input("How Tall Is The Tree : "))
        if treeHeight > 2:
            spaces = treeHeight - 1

            hashes = 1

            stumpSpaces = treeHeight - 1

            while treeHeight != 0:

                for _ in range(spaces):
                    print(" ", end="")

                for _ in range(hashes):
                    print("#", end="")

                print()
                spaces -= 1
                hashes += 2
                treeHeight -= 1

            for _ in range(stumpSpaces):
                print(" ", end="")

            print("#")
        else:
            print("Enter a number bigger than 2")

    except:
        print("Enter a number")


if __name__ == "__main__":
    main()
