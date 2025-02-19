class card:
    def __init__(self,value) -> None:
        self.value = value

    def getValue(self):
        pass

    def displayCard(self):
        pass

class Deck:
    def __init__(self,cards,currentIndex) -> None:
        self.cards = cards
        self.currentIndex = currentIndex

    def drawCard(self):
        pass

    def resetDeck(self):
        pass
class Hand:
    def __init__(self) -> None:
        self.cardsInHand=[]
        self.totalValue=0

    def addCard(self):
        pass

    def calculateScore(self):
        pass

    def getTotalValue(self):
        pass

    def displayHand(self):
        pass
    def isBlackjack(self):
        pass
    def hasBusted(self):
        pass


class Player:
    def __init__(self,hand) -> None:
        self.hand =hand
    
    def hit(self,deck):
        pass
    def stand(self):
        pass

    def getScore(self):
        pass

    def hasBlackjack(self):
        pass

    def displayHand(self):
        pass

class Dealer:
    def __init__(self,hand) -> None:
        self.hand=hand

    def hit(self,deck):
        pass

    def playTurn(self,scanner,deck):
        pass

    def getScore(self):
        pass

    def displayHand(self):
        pass

    def hasBusted(self):
        pass

class Game:
    def __init__(self,deck,player,dealer) -> None:
        self.deck = deck 
        self.player = player
        self.dealer = dealer

    def startGame(self):
        pass
    def playerTurn(self,scanner):

        pass

    def dealerTurn(self,scanner):
        pass
    def determineWinner(self):
        pass

    def playGame(scanner):
        pass

