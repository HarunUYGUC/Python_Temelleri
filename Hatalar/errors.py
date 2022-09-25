# Error

x = int(input("x: "))
y = int(input("y: "))

print(x + y)

"""
Böyle bir kod yazınca sayısal veri hariç bir bilgi girersek (örn: a) uygulama 
hata verecektir ve çalışmayı durduracaktır. 
Bunun önlenmesi için aşağıdaki gibi hata durumunda ne yapılacağını belirten bir kod
yazmalıyız.
"""

# Error Handling

try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x + y)
except:
    print("Hata Oluştu!")

