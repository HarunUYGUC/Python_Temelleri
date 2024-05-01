# serialize
# Uygulama tarafında olan bir objeyi dosya tarafına bir .json 
# bir bilgi olarak aktarma işlemine denir.

import json

person = {
    "firstName": "Harun",
    "lastName": "Uyguç",
    "hobbies": ["bilgisayar oyunları", "spor"],
    "age": 21,
    "gameCharacters": [
        {
            "firstName": "Kyle",
            "lastName": "Crane",
            "age": 24
        },
        {
            "firstName": "Leon",
            "lastName": "S. Kennedy",
            "age": 22
        }
    ]
}

print(person)
print(type(person))

print(person["firstName"])

# Uygulamadaki "dictionary" veri yapısını "string"e çevirir.
# Daha sonra bu "string" veriyi "json" dosyasına kaydeteceğiz.
# "json" dosyasından veri okuduğumuzda tam tersi işlemleri yapıyoruz.
sonuc = json.dumps(person, ensure_ascii=False, indent=2)
# "ensure_ascii=False" diyerek Türkçe karakter sorununun önüne geçiyoruz.
# "indent=2" diyerek tek satırda gelen sonucu yukarıda yazdığımız hale getiriyoruz.
print(sonuc)
print(type(sonuc))

with open(r"C:\Users\Harun\Desktop\Python_Temelleri\JSON ile Dosya İşlemleri\person-2.json", "w") as file:
    # "file.write(person)" kodu hata verir çünkü .json dosyasına "dict" veri değil "str" veri yazılır.
    json.dump(person, file, ensure_ascii=False, indent=2)




# deserialize
# Yukarıdakinin tam tersidir.
