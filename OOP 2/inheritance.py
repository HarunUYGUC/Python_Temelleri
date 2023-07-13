#  Inheritance (Kalıtım, Miras)

# OOP

# 1)

""" Bu şekildeki gibi bazı aynı özelliklere veya metotlara sahip (ad, soyad, ...) iki ayrı sınıf için 
aynı özellikleri tekrardan sınıflar içerisinde oluşturmak yerine Inheritance (Kalıtım, Miras)
mantığını kullanarak 2. şekildeki gibi sınıfları oluşturabiliriz.  """

# Ogrenci
    # ad, soyad, adres, cinsiyet, numara
    # yemek_ye(), ders_calis()

# Ogretmen
    # ad, soyad, adres, cinsiyet, brans
    # yemek_ye(), ders_anlat()


# 2)

""" Kisi sınıfına eklemiş olduğumuz bütün özellik ve methodlar, Ogrenci ve Ogretmen sınıflarına 
direkt olarak kalıtım yoluyla aktarılacaktır. Sonuçta her Ogretmen ve Ogrenci temelde bir Kisi'dir. """

""" Kisi sınıfı, 'Base Class' veya 'Parent Class' olarak adlandırılır. """
# Kisi
    # ad, soyad, adres, cinsiyet
    # yemek_ye()

""" Base Class'tan oluşturduğumuz Ogrenci ve Ogretmen sınıfları 'Child Class' olarak adlandırılır. """
# Ogrenci
    # numara
    # ders_calis()

# Ogretmen
    # brans
    # ders_anlat()


""" EvcilHayvan ve VahsiHayvan temelde bir Hayvan'dır. """
# Hayvan (En Temel Sınıf)

""" Kedi ve Kus temelde bir EvcilHayvandır, en temelde ise Hayvan'dır. """
# EvcilHayvan (Temel Sınıf)
# Kedi, Kus

""" Aslan ve Kaplan temelde bir EvcilHayvandır, en temelde ise Hayvan'dır. """
# VahsiHayvan (Temel Sınıf)
# Aslan, Kaplan
