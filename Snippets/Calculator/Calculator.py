import time


def calc(num1, num2, sym):
    if sym == 1 or sym == "+":
        print("Adding Numbers...")
        time.sleep(1)
        print(num1 + num2)

    elif sym == 2 or sym == "-":
        print("Subtracting Numbers...")
        time.sleep(1)
        print(num1 - num2)

    elif sym == 3 or sym == "*":
        print("Multiplying Numbers...")
        time.sleep(1)
        print(num1 * num2)

    elif sym == 4 or sym == "/":
        print("Dividing Numbers...")
        time.sleep(1)

        try:
            print(num1 / num2)

        except ZeroDivisionError:
            print("Can't Divide by Zero")
            print("0")


def result():
    valInt = False

    while not valInt:
        try:
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))
            sym = int(
                input(
                    "What Do You Want To Do ? 1. Add, 2. Subtract, 3. Multiply Or 4. Divide."
                    "Enter Number: "
                )
            )

            valInt = True

        except ValueError:
            print("Invalid Input. Please Try Again... ")

        except:
            print("Unknown Error")

        calc(num1, num2, sym)


result()

