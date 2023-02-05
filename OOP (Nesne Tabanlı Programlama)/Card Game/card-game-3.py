# Destede kalan kart sayısı için kartSayisi() isminde bir metot.
# Destedeki kartları karıştırmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanılsın.

import random

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

    def number_of_cards(self):
        return len(self.cards)

    def shuffle_cards(self):
        random.shuffle(self.cards)
        return self.cards

    def deal_cards(self, _piece):
        self.piece = _piece
        self.dealedCards = random.sample(self.cards, self.piece)
        return self.dealedCards

    def new_number_of_cards(self):
        for card in self.dealedCards:
            for i in range(len(self.cards) - 1):
                if (card == self.cards[i]):
                    self.cards.pop(i)
        return len(self.cards)
    
    def throw_card(self):
        return random.choice(self.dealedCards)

deck = Deck()

print(f"Kartların karışmamış ve dağıtılmamış durumu: {deck.cards}")
print(f"Kartaların dapıtılmadan önceki sayısı: {deck.number_of_cards()}")
print(f"Kartarın karıştırılmış durumu: {deck.shuffle_cards()}")
print(f"Dağıtılan kartlar: {deck.deal_cards(5)}")
print(f"Dağıtılan kartlar arasından seçilen kart: {deck.throw_card()}")
print(f"Kartların dağıtıldıktan sonraki sayısı: {deck.new_number_of_cards()}")
print(f"Kartların dağıtıldıktan sonraki durumu: {deck.cards}")
