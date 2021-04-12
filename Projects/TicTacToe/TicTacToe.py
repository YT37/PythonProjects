from random import randint


def displayBoard(board):
    print("\n" * 100)
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-|-|-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-|-|-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def playerInput():
    marker = " "

    while marker != "X" or marker != "O":
        marker = input("Player 1 : Pick A Marker (X or O) : ").upper()

        if marker == "X":
            return ("X", "O")

        else:
            return ("O", "X")


def placeMarker(board, marker, position):
    board[position] = marker


def win(board, mark):
    return (
        (board[1] == mark and board[2] == mark and board[3] == mark)
        or (board[4] == mark and board[5] == mark and board[6] == mark)
        or (board[7] == mark and board[8] == mark and board[9] == mark)
        or (board[7] == mark and board[8] == mark and board[9] == mark)
        or (board[7] == mark and board[4] == mark and board[1] == mark)
        or (board[8] == mark and board[5] == mark and board[2] == mark)
        or (board[9] == mark and board[6] == mark and board[3] == mark)
        or (board[7] == mark and board[5] == mark and board[3] == mark)
        or (board[9] == mark and board[5] == mark and board[1] == mark)
    )


def choose():
    return randint(1, 2)


def spaceCheck(board, position):
    return board[position] == " "


def boardCheck(board):
    for i in range(1, 10):
        if spaceCheck(board, i):
            return False

    return True


def playerChoice(board):
    pos = 0

    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not spaceCheck(board, pos):
        pos = int(input("Choose your next position (1-9) : "))

    return pos


def replay():
    return (
        input("Do you want to play again? Enter Yes or No : ").lower().startswith("y")
    )


def main():
    print("Welcome To Tic Tac Toe!")

    while True:
        theBoard = [" "] * 10

        player1Marker, player2Marker = playerInput()

        turn = choose()
        print(f"{turn} Will Go First.")

        playGame = input("Are you ready to play? Enter Yes or No : ")

        if playGame.lower()[0] == "y":
            gameOn = True

        else:
            gameOn = False

        while gameOn:
            if turn == 1:
                displayBoard(theBoard)
                position = playerChoice(theBoard)
                placeMarker(theBoard, player1Marker, position)

                if win(theBoard, player1Marker):
                    displayBoard(theBoard)
                    print("Congratulations! You Have Won The Game!")
                    gameOn = False

                else:
                    if boardCheck(theBoard):
                        displayBoard(theBoard)
                        print("The Game Is A Draw!")
                        break

                    else:
                        turn = 2

            else:
                displayBoard(theBoard)
                position = playerChoice(theBoard)
                placeMarker(theBoard, player2Marker, position)

                if win(theBoard, player2Marker):
                    displayBoard(theBoard)
                    print("Player 2 Has Won!")
                    gameOn = False

                else:
                    if boardCheck(theBoard):
                        displayBoard(theBoard)
                        print("The Game Is A Draw!")
                        break

                    else:
                        turn = 1

        if not replay():
            break


main()
