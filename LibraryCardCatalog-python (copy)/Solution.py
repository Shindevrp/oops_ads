class card:
    def __init__(self,title,book,author):
        self.title=title
        self.book=book
        self.author=author

    def __str__(self):
        return f"Title: {self.title}, Book: {self.book}, Author: {self.author}"

class cardCatalog:
    def __init__(self):
        
        self.cardStore=[]
    def addACard(self,title,book,author):
        s=card(title,book,author)
        self.cardStore.append(s)
        print(f"added to card: {title},{book},{author}")
    def getATite(self):
        for card in self.cardStore:
            print(card.title)
    def getAnAuthor(self):
        for card in self.cardStore:
            print(card.author)
    def getASubject(self):
        for card in self.cardStore:
            print(card.book)
        
    
    def removeATitle(self, title):
        new_card_store = []
        for card in self.cardStore:
            if card.title != title:
                new_card_store.append(card)
        self.cardStore = new_card_store

    def printTheCatalog(self):
        for card in self.cardStore:
            print(card)



try:
    cclog=cardCatalog()
    while (True):
        
        i=input().split(" ")
        print(i)

        title=i[0]
        book=i[1]
        author=[2]
        cclog.addACard(title,book,author)
        print("input taken")

except EOFError:
    print()





