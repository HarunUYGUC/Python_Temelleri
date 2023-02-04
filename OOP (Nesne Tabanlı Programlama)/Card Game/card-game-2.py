# Deste sınıfı

# kart tipleri   => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K
"""A = As, J = Joker, Q = Queen, K = King"""

# Deste sınıfındaki kartlar listesine 52 kartı for ve list comphension ile ekleyiniz.

class Card:
    def __init__(self, _type, _value):
        self.type = _type
        self.value = _value

    def __repr__(self):
        return f"{self.type} {self.value}"

class Deck:
    cardTypes = ["Karo", "Sinek", "Kupa", "Maça"]
    cardValues = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []

        for type in Deck.cardTypes:
            for value in Deck.cardValues:
                self.cards.append(Card(type, value))

        # self.cards = [Card(type, value) for type in Deck.cardTypes for value in Deck.cardValues]
        
        print(self.cards)

Deck()
