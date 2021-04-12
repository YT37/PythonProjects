"""Problem"""
Num = int(input("Enter A Number : "))
Range = int(input("Enter A Limit : "))
for i in range(Range):
    print(Num * i)
"""Problem"""
def pattern(n):
    for i in range(1, n + 1):
        k = i if (i % 2 != 0) else i
        for g in range(k, n):
            if g >= k:
                print(end=" ")
        for j in range(0, k):
            if j == k - 1:
                print("*")
            else:
                print("*", end = " ")
n = 10
pattern(n)
"""Problem"""
big = 500
small = 300
req = big - small
print(req)
"""Problem"""
hotDog = 400
hotDogCont = 8
cont = 0
while(hotDog >= hotDogCont):
    hotDog -= hotDogCont
    cont += 1
print("Total Container :- {}.".format(cont))
"""Problem"""
seconds = [66,57,54,53,64,52,59]
l = len(seconds)
for i in range(l):
    for j in range(0,l-i-1):
        if seconds[j] > seconds[j+1]:
            seconds[j],seconds[j+1] = seconds[j+1],seconds[j]
print("The Best Time Is {}.".format(seconds[0]))
"""Problem"""
freeSize = int(input("Size Free : "))
usedSize = int(input("Size Used : "))
deletedSize = int(input("Size Of Deleted File : "))
newSize = int(input("Size Of New File : "))
usedSize -= deletedSize
usedSize += newSize
freeSize += deletedSize
freeSize -= newSize
totalSize = usedSize + freeSize
print("Size of Space Left Is {0} GB And Left Is {1} GB And Total Size Is {2} GB.".format(freeSize, usedSize, totalSize))
"""Problem"""
people = 1200000
days = 365
peopleYear = people * days
print(f"A Bus Can Carry {peopleYear:,} Peole Each Year.")
"""Problem"""
hours = [8,10,9,8,7,12]
nurses = len(hours)
avg = sum(hours) / nurses
print("The Average No. Of Hours = {}.".format(avg))
"""Problem"""
game = 75
sweater = 68
braclets = 43
calc = ((game + (3*sweater) + (2*braclets)) - braclets) - 10
print("The Final Price is {}.".format(calc))
"""Problem"""
miles = 2052
days = 6
stops = 2
km = 1.60934
avg = ((miles / days) / stops) * km
print("She Drove Average Of {:.2f} Km Between Each Stop.".format(avg))
"""Problem"""
firstMovie = 100
secondMovie = 110
hours = (firstMovie + secondMovie) / 60
print("The Movies Took {} Hours To Watch.".format(hours))
"""Problem"""
red = 5000000
white = 8000
ratio = int(red / white)
print("The Ratio Of Red And White Blood Corpuscles in one Cubic Millimeter is {}.".format(ratio))
"""Problem"""
karaGlass = int(input("Enter No. Of Glasses Sold By Kara : "))
raniGlass = int(input("Enter No. Of Glasses Sold By Rani : "))
karaPrice = 5
raniPrice = 7
karaMoney = karaGlass * karaPrice
raniMoney = raniGlass * raniPrice
if karaMoney > raniMoney:
    print("Kara Made More Money By {} Cents.".format(karaMoney - raniMoney))
else:
    print("Rani Made More Money By {} Cents.".format(raniMoney - karaMoney))
"""Problem"""
def Combination(Array):
    if len(Array) == 0:
        return []
    if len(Array) == 1:
        return [Array]
    l = []
    for i in range(len(Array)):
        m = Array[i]
        remList = Array[:i] + Array[i+1:]
        for j in Combination(remList):
            l.append([m] + j)
    return l

student = ["Ram", "Anuj", "Deepak", "Ravi"]
for c in Combination(student):
    print(c)
"""Problem"""
DVD = 42
percent = 12
saving = ((DVD * 100) / percent) - DVD
print("She Deposited {} $ In Her Savings Account".format(saving))
"""Problem"""
def getSum(n):
    total = 0
    while(n > 0):
        digit = n % 10
        total = total + digit
        n = n / 10
    return total

no = (int(input("Enter Number : ")))
sumOf = getSum(no)
print("The Total Sum Of {} is {}".format(no,sumOf))
"""Problem"""
def duplicate(name):
    x = name.split()
    sSize = len(x)
    r = []
    for i in range(sSize):
        k = i + 1
        for j in range(k,sSize):
            if x[i] == x[j] and x[i] not in r:
                r.append(x[i])
                print(x[i])

students = "Aman Ankit Deepak Aman Deepak Amit Ankit Vansh Aman Sagar"
duplicate(students)
"""Problem"""
fish = [12, 13, 8, 10, 17]
fish.sort()
large = fish[len(fish) - 1]
print(f"The Largest Fish Lefty Caught Was {large} Feet")
"""Problem"""
print(u"\u003B")
"""Problem"""
summ = 0
for i in range(0, 8):
    summ = summ + 8
print(f"The Square Of 8 Is {summ}")
"""Problem"""
h = int(input("Enter Hour : "))
m = int(input("Enter Minute : "))
if h < 0 or m < 0 or h > 12 or m > 60:
    print("Wrong Input!")
if h == 12:
    h = 0
if m == 60:
    m = 0
angleh = 0.5 * (h * 60 + m)
anglem = 6 * m
angle = abs(angleh - anglem)
angle = min(360 - angle, angle)
if angle == 0:
    print("The Hands Overlap")
else:
    print(f"The Angle Of The Clock Is {angle}")
"""Problem"""
year = int(input("Enter A Year : "))
flag = False
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            flag = True
        else:
            flag = False
    else:
        flag = True
else:
    flag = False
if flag:
    print(f"{year} Is A Leap Year")
else:
    print(f"{year} Is Not A Leap Year")
"""Problem"""
no = int(input("Enter A Nuber To Convert To Binary : "))
binary = format(no, "b")
print(f"{no} Is {binary} In Binary")
"""Problem"""
numMap = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def roman(num):
    ro = ""

    while num > 0:
        for i, r in numMap:
            while num >= i:
                ro += r
                num - +i

    return ro


j = int(input("Julius's Books : "))
n = int(input("Nancy's Books : "))
val = j + n
print(f"Books = {roman(val)}")
"""Problem""" 
pwd = input("Enter Password : ")
sym = ["$", "@", "#", "%"]
val = True

if len(pwd) < 6:
    print("Password should be at least 6 charecters")
    val = False

if len(pwd) > 20:
    print("Password should not be more than 20 charecters")
    val = False

if not any(char.isdigit() for char in pwd):
    print("Password should have at least 1 number")
    val = False

if not any(char.isupper() for char in pwd):
    print("Password should have at least 1 uppercase letter")
    val = False

if not any(char.islower() for char in pwd):
    print("Password should have at least 1 lowercase letter")
    val = False

if not any(char in sym for char in pwd):
    print("Password should have at least 1 special symbol")
    val = False

if val:
    print("Password is valid")

elif not val:
    print("Passwword is invalid")
"""Problem""" 
c = float(input("Enter Temperature In Celsius : "))
f = (c * 1.8) + 32
print(f"Temperature =  {f} °F")
"""Problem""" 
inch = 0.394
m = 0.01
km = 0.00001

cm = int(input("Enter Length In CM : "))

print(f"Inch = {inch*cm}")
print(f"Meter = {m*cm}")
print(f"KilloMeter = {km*cm}")
"""Problem""" 
year = 60 * 24 * 365
m = 13772160
years = int((m / year))
print(f"Dave is {years} old")
"""Problem""" 
d = float(input("Enter Distance In Meters : "))
hr = float(input("Enter Hours : "))
m = float(input("Enter Minutes : "))
s = float(input("Enter Seconds : "))

time = (hr * 3600) + (m * 60) + s
kph = (d / 1000.0) / (time / 3600.0)
mph = kph * 1.609

print(f"Speed is {mph} Miles Per Hour")
"""Problem""" 
first = int(input("Enter 1st No."))
second = int(input("Enter 2nd No."))

print(f"Sum = {first+second}")
print(f"Difference = {first-second}")
print(f"Product = {first*second}")
print(f"Average = {(first+second)/2}")
print(f"Max = {max(first,second)}")
print(f"Min = {min(first,second)}")