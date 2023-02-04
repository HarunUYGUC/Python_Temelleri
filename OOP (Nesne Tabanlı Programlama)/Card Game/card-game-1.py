# Kart sınıfı

# Kart sınıfından türetilen her bir nesne bir kart türünü temsil edecek. (sinek 5)
# Kart sınıfının tip ve deger isminde 2 instance özelliği olsun. (tip:sinek deger:5)
# Kart sınıfının kartıGetir() ismindeki instance metodu kart bilgilerini yazdırsın.
# Kart bilgilerini yazdırmak için __repr__ metodunu kullanın. (Araştırma...)

class Card:
    def __init__(self, _type, _value):
        self.type = _type
        self.value = _value

    # def get_card(self):
    #     return f"{self.type} {self.value}"

    def __repr__(self):
        return f"{self.type} {self.value}"

card = Card("Karo", 2)

#print(card.get_card())

print(card)
