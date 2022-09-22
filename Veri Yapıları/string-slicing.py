ad = "Harun"
soyad = "Uyguç"
yas = "18"

msj = "Benim adım " + ad + ", soyadım " + soyad + " ve yaşım " + yas + "."

print(msj[0:5])
print(msj[6:16])
print(msj[:5]) # Başlangıçtan itibaren ilerler.
print(msj[10:]) # Sona kadar ilerler.

print("Eksili işlem")
print(msj[-10:-1])

print(msj[0:5:2])

print(msj[::1])
print(msj[:])
print(msj[::-1])