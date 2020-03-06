from deck import Deck
from deck import Megadeck
from deck import Backupdeck

bdeck = Backupdeck()
mdeck = Megadeck()
deck1 = Deck()
for q in range(0, deck1.decknum):
    deck1.shuffle()
    mdeck.cards = mdeck.cards + deck1.cards
    mdeck.sort()
drawnCards = []

e = 1

print("Available commands: (draw, shuffle, sort, deck, hand, insert, and exit)")

while e == 1:
    course = input("What do you wish to do with your cards?" )
    print('\n')
    
    if course == "draw":
        drawnum = int(input("Draw how many cards?"))
        for i in range(drawnum):
            drawn_card = mdeck.cards.pop(0)
            print(f"Drawn Card: {drawn_card}")
            bdeck.cards.append(drawn_card)
        print('\n')
        print(f"Updated Pile: {mdeck}")
        bdeck.cards.append(drawn_card)
        
        
    if course == "shuffle":
        mdeck.shuffle()
        print(mdeck)
        print('\n')

    if course == "sort":
        mdeck.sort()
        print(mdeck)
        print('\n')

    if course == "deck":
        print(mdeck)
        print('\n')

    if course == "hand":
        print(bdeck)

    if course == "insert":
        mdeck.cards = mdeck.cards + bdeck.cards
        mdeck.sort()

    if course == "exit":
        e = 2
        print("Thank you for using Cardsorter!")

    course = "baxter"
    
