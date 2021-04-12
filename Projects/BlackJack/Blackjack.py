import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " Of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deckComp = ""
        for card in self.deck:
            deckComp += "\n " + card.__str__()
        return "The Deck Has:" + deckComp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        singleCard = self.deck.pop()
        return singleCard


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def addCard(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjustForAce(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def winBet(self):
        self.total += self.bet

    def loseBet(self):
        self.total -= self.bet


def takeBet(chips):
    while True:
        try:
            chips.bet = int(input("How Many Chips Would You Like To Bet :  "))

        except ValueError:
            print("Sorry, A Bet Must Be An No. ")

        else:
            if chips.bet > chips.total:
                print("Sorry, Your Bet Can't Exceed", chips.total)

            else:
                break


def hit(deck, hand):
    hand.addCard(deck.deal())
    hand.adjustForAce()


def hitOrStand(deck, hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand : ")

        if x[0].lower() == "h":
            hit(deck, hand)

        elif x[0].lower() == "s":
            print("Player Stands. Dealer Is Playing.")
            playing = False

        else:
            print("Sorry, Please Try Again.")
            continue

        break


def showSome(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(" " + dealer.cards[1].__str__())
    print("\nPlayer's Hand:", *player.cards, sep="\n ")


def show(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)


def playerBusts(player, dealer, chips):
    print("Player Busts!")
    chips.loseBet()


def playerWins(player, dealer, chips):
    print("Player Wins!")
    chips.winBet()


def dealerBusts(player, dealer, chips):
    print("Dealer Busts!")
    chips.winBet()


def dealerWins(player, dealer, chips):
    print("Dealer Wins!")
    chips.loseBet()


def push(player, dealer):
    print("Dealer and Player Tie! It's A Push.")


total = 100
while True:
    print(
        "Welcome To BlackJack! Get As Close To 21 As You Can Without Going Over!\n\
    Dealer hits Until She Reaches 17. Aces Count As 1 Or 11."
    )
    deck = Deck()
    deck.shuffle()

    playerHand = Hand()
    playerHand.addCard(deck.deal())
    playerHand.addCard(deck.deal())

    dealerHand = Hand()
    dealerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())

    playerChips = Chips(total)
    takeBet(playerChips)

    showSome(playerHand, dealerHand)

    while playing:
        hitOrStand(deck, playerHand)
        showSome(playerHand, dealerHand)

        if playerHand.value > 21:
            playerBusts(playerHand, dealerHand, playerChips)
            break

    if playerHand.value <= 21:
        while dealerHand.value < 17:
            hit(deck, dealerHand)

        show(playerHand, dealerHand)

        if dealerHand.value > 21:
            dealerBusts(playerHand, dealerHand, playerChips)

        elif dealerHand.value > playerHand.value:
            dealerWins(playerHand, dealerHand, playerChips)

        elif dealerHand.value < playerHand.value:
            playerWins(playerHand, dealerHand, playerChips)

        else:
            push(playerHand, dealerHand)

    print("\nPlayer's Winnings Stand At ", playerChips.total)

    newGame = input("Would You Like To Play Again : ")

    if newGame[0].lower() == "y":
        playing = True
        continue

    else:
        print("Thanks For Playing!")
        break
