from random import choice as c
from time import sleep as s

scorePlay = 0
scoreComp = 0
breaker = False

print(
    "This Is A Classic Game Of Rock, Paper And Scissor, \nGet To The Final Score You Decided \nBefore The Computer And You Win"
)

moves = ["Rock", "Paper", "Scissor"]
while True:
    try:
        s(2)
        scoreFin = int(input("What Is The Winning Score : "))

        while True:
            if scoreComp == scoreFin or scorePlay == scoreFin:
                if scoreComp > scorePlay:
                    print(
                        f"Computer Is The Overall Winner By {scoreComp-scorePlay} Points"
                    )

                    replay = input("Want To Play Again(Yes/No) : ")

                    if replay[0].lower() == "y":
                        s(2)
                        scoreFin = int(input("What Is The Winning Score : "))
                        scorePlay = 0
                        scoreComp = 0
                        continue

                    else:
                        breaker = True
                        break

                else:
                    print(
                        f"You Are The Overall Winner By "
                        f"{scorePlay-scoreComp} Points"
                    )
                    replay = input("Want To Play Again(Yes/No) : ")

                    if replay[0].lower() == "y":
                        s(2)
                        scoreFin = int(input("What Is The Winning Score : "))
                        scorePlay = 0
                        scoreComp = 0
                        continue

                    else:
                        breaker = True
                        break

            s(0.5)
            comp = c(moves)
            player = input("Enter A Move Rock, Paper Or Scissor : ")
            print(f"Computer Picked {comp}")

            if player[0].lower() == comp[0].lower():
                print("Its a Tie")
                print(f"Player = {scorePlay}\nComputer = {scoreComp}")
                s(0.5)
                print("\n" * 10)
                continue

            elif player[0].lower() == "s" and comp[0].lower() == "r":
                print("Computer Won")
                scoreComp += 1
                print(f"Player = {scorePlay}\nComputer = {scoreComp}")
                s(0.5)
                print("\n" * 10)
                continue

            elif player[0].lower() == "r" and comp[0].lower() == "s":
                print("You Won")
                scorePlay += 1
                print(f"Player = {scorePlay}\nComputer = {scoreComp}")
                s(0.5)
                print("\n" * 10)
                continue

            elif player[0].lower() == "r" and comp[0].lower() == "p":
                print("Computer Won")
                scoreComp += 1
                print(f"Player = {scorePlay}\nComputer = {scoreComp}")
                s(0.5)
                print("\n" * 10)
                continue

            elif player[0].lower() == "p" and comp[0].lower() == "r":
                print("You Won")
                scorePlay += 1
                print(f"Player = {scorePlay}\nComputer = {scoreComp}")
                s(0.5)
                print("\n" * 10)
                continue

            elif player[0].lower() == "p" and comp[0].lower() == "s":
                print("Computer Won")
                scoreComp += 1
                print(f"Player = {scorePlay}\nComputer = {scoreComp}")
                s(0.5)
                print("\n" * 10)
                continue

            elif player[0].lower() == "s" and comp[0].lower() == "p":
                print("You Won")
                scorePlay += 1
                print(f"Player = {scorePlay}\nComputer = {scoreComp}")
                s(0.5)
                print("\n" * 10)
                continue

    except ValueError:
        print("Enter A Number")
        continue

    except IndexError:
        print("Enter A String")
        continue

    if breaker:
        break
