import math


def getArea(shape):
    if shape == 1:
        rectangleArea()

    elif shape == 2:
        circleArea()

    elif shape == 3:
        parallelogramArea()

    elif shape == 4:
        rhombusArea()

    elif shape == 5:
        triangleArea()

    elif shape == 6:
        trapezoidArea()

    else:
        print("Please Enter A Corresponding Number")


def rectangleArea():
    length = float(input("Enter the Length : "))
    width = float(input("Enter the Width : "))

    area = length * width

    print("The Area Of The Rectangle = ", area)


def circleArea():
    radius = float(input("Enter the radius : "))

    area = math.pi * (math.pow(radius, 2))

    print("The Area Of The Circle = {:.2f} ".format(area))


def parallelogramArea():
    breadth = float(input("Enter The Breadth : "))
    height = float(input("Enter The Height : "))

    area = breadth * height

    print("The Area Of The Parallelogram = ", area)


def rhombusArea():
    diagonal1 = float(input("Enter The First Diagonal : "))
    diagonal2 = float(input("Enter The Second Diagonal : "))

    area = (diagonal1 * diagonal2) / 2

    print("The Area Of The Rhombus = ", area)


def triangleArea():
    breadth = float(input("Enter The Breadth : "))
    height = float(input("Enter The Height : "))

    area = (breadth * height) / 2

    print("The Area Of The Triangle = ", area)


def trapezoidArea():
    base1 = float(input("Enter The First Base : "))
    base2 = float(input("Enter The Second Base : "))
    height = float(input("Enter The Height : "))

    area = 0.5 * (base1 + base2) * height

    print("The Area Of The Trapezoid = ", area)


getArea(
    int(
        input(
            "Choose A Shape To Calcuae The Area Of : 1.Rectangle, 2.Circle, 3.Parallelogram, \n4.Rhombus, "
            "5.Triangle Or 6.Trapezoid : "
        )
    )
)
