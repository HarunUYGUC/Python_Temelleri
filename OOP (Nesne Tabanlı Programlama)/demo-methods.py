# BankAccount isminde bir sınıf tanımlayınız.

# Üretilen her bir nesne owner isminde biz özelliğe sahip olmalıdır. 
# BankAccount("Harun Uyguç")

# Üretilen her bir nesne balance isminde bir özelliğe sahip olup başlangıçta 
# 0.0 değerinde olmalıdır.

# Üretilen her bir nesne için deposit metodu oluşturun ve dışarıdan yatırılacak 
# miktar bilgisini alıp balance üzerine ekleyin ve balance miktarını geriye döndürün.

# Üretilen her bir nesne için withdraw metodu oluşturun ve dışarıdan çekilecek miktar 
# bilgisini alıp balance değerinden çıkarıp geriye döndürün.

# hesap = BankAccount("Harun Uyguç")
# hesap.owner => Harun Uyguç
# hesap.balance => 0.0
# hesap.deposit(1200) => 1200.0
# hesap.withdraw(525) => 525.0

class BankAccount:
    def __init__(self, _owner):
        self.owner = _owner
        self.balance = 0.0

    def current_balance(self):
        return f"Mevcut bakiyeniz: {self.balance} TL"
    
    def deposit(self, _depositAmount):
        self.depositAmount = _depositAmount
        self.balance += self.depositAmount
        return f"{self.owner}, yatırdığınız miktar: {self.depositAmount} TL - toplam miktarınız: {self.balance} TL"
    
    def withdraw(self, _withdrawAmount):
        self.withdrawAmount = _withdrawAmount
        self.balance -= self.withdrawAmount
        return f"{self.owner}, çektiğiniz miktar: {self.withdrawAmount} TL - kalan miktarınız: {self.balance} TL"

hesap = BankAccount("Harun Uyguç")
print(hesap.current_balance())
print(hesap.deposit(1250))
print(hesap.withdraw(525))
print(f"Güncel {hesap.current_balance()}")
