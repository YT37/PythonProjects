import random

def bubbleSort(numList):
    i = len(numList) - 1

    while i:
        j = 0

        while j < i:
            if numList[j] < numList[j + 1]:
                temp = numList[j]
                numList[j] = numList[j + 1]
                numList[j + 1] = temp

            else:
                pass

            j += 1

        i -= 1

    for k in numList:
        print(k, end=", ")
