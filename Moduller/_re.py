# Regular Expression Module (RE Module)

import re

result = dir(re)
print(result)


"""re Module (Arama işlemini re modülü methodları ile nasıl yapacağımızı öğreneceğiz.)"""

str = "Python Kursu: Python Programlama Rehberiniz | 40 Saat"

result = re.findall("Python", str)
print(result)

result = re.split(" ", str)
print(result)

result = re.sub(" ", "-", str)
print(result)
"""Yukarıdakinin aynısı:"""
result = re.sub("\s", "-", str)
print(result)

result = re.search("Python", str)
print(result)

# result = result.span()
# print(result)

# result = result.start()
# print(result)

# result = result.end()
# print(result)

# result = result.group()
# print(result)

# result = result.string
# print(result)


"""Regular Expression (Regular Expression İfadelerin nasıl yazılacağını öğreneceğiz.)"""

"""
    [] - Köşeli parantezler arasına yazılan bütün karakterler aranır.

        [abc] => a      : 1 match
                ac      : 2 match
                Pytohn  : No matches

        [a-e]   => [abcde]
        [1-5]   => [12345]
        [0-395] => [012395]  #[0-3] arasına ve 9 ve 5'e bakar.
        
        [^abc] => abc dışındaki karakterler
        [^0-9] => rakam olmayan karakterler
"""

result = re.findall("[abc]", str)
print(result)

result = re.findall("[sat]", str)
print(result)

result = re.findall("[a-e]", str)
print(result)

result = re.findall("[0-5]", str)
print(result)

result = re.findall("[^abc]", str)
print(result)

result = re.findall("[^0-9]", str)
print(result)


"""
        . => Herhangi bir karakteri belirtir.
                .. => a         : No match
                      ab        : 1 match
                      abc       : 1 match
                      abcd      : 2 matches
"""

result = re.findall("...", str)
print(result)

result = re.findall("Py..on", str)
print(result)


"""
        ^ => String ifade belirtilen karakterle ya da kelimeyle başlıyor mu?
                ^a => a         : 1 match
                      abc       : 1 match
                      bac       : No match
"""

result = re.findall("^P", str)
print(result)

result = re.findall("^Python", str)
print(result)


"""
        $ => String ifade belirtilen karakterle ya da kelimeyle bitiyor mu?
                a$ => a           : 1 match
                      lamba       : 1 match
                      Python      : No match
"""

result = re.findall("t$", str)
print(result)

result = re.findall("Saat$", str)
print(result)


"""
        * => Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
                ma*n => mn         : 1 match
                        man        : 1 match
                        maaan      : 1 match
                        main       : No match (a'nın arkasına n gelmediği için.)
"""

result = re.findall("Sa*t", str)
print(result)


"""
        + => Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.
                ma+n => mn         : No match
                        man        : 1 match
                        maaan      : 1 match
                        main       : No match (a'nın arkasına n gelmediği için.)
"""

result = re.findall("Sa+t", str)
print(result)


"""
        ? => Bir karakterin sıfır ya da bir kez olmasını kontrol eder.
                ma?n => mn         : 1 match
                        man        : 1 match
                        maaan      : No match
                        main       : No match (a ve n arasında başka bir karakter olduğu için.)
"""

result = re.findall("Sa?t", str)
print(result)


"""
        {} => Karakter sayısını kontrol eder.
                al{2}           => a karakterinin arkasındaki l karakteri 2 kez tekrarlamalı.
                al{2,3}         => a karakterinin arkasındaki l karakteri en az 2, en çok 3 kez tekrarlamalı.
                [0-9]{2,4}      => en az 2 en çok 4 basamaklı sayılar.
"""

result = re.findall("a{2}", str)
print(result)

result = re.findall("[0-9]{2}", str)
print(result)


"""
        | => Alternatif seçeneklerden birisinin gerçekleşmesi gerekir.
                a|b => a ya da b
                        cde     => No match
                        ade     => 1 match
                        acdbea  => 3 match
"""

result = re.findall("a|b", str)
print(result)


"""
        () => Gruplamak için kullanılır.
                (a|b|c)xz => a, b, c karakterlerinin arkasında xz olmalı.
"""

result = re.findall("(a|b|c)xz", str)
print(result)


"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string in başında mı?
        \Athe => the string in başında mı?
        # result = re.findall("\APython", str)

    \Z - Belirtilen karakter string in sonunda mı?
        the\Z => the string in sonunda mı?
        # result = re.findall("saat\Z", str)

    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı?
        \bthe => the kelimenin in başında mı?
        the\b => the kelimenin in sonunda mı?

    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mi?
        \Bthe => the kelimenin in başında değil mi?
        the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
        \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
        \D => 1ab44_50

    \s - Boşluk karakterlerini arar.  

    \S - Boşluk karakterleri dışındaki karakterleri arar.

    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakterleri arar.

    \W - \w nin tam tersini yapar.
"""
