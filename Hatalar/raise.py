# x = 10

# if (x > 5):
#     raise ValueError("x, 5'ten büyük olamaz!")


def colorize(text, color):
    colors = ("blue", "red", "White", "Black", "Orange")
    
    if type(text) is not str:
        raise TypeError("Text str tipinde olamaz!")
    
    if type(color) is not str:
        raise TypeError("Color str tipinde olamaz!")
    
    if color not in colors:
        raise ValueError("Geçersiz bir renk ismi!")

    print(f"'{text} {color}' olarak yazdırıldı.")

try:
    colorize("Hello!", "blue")
except Exception as ex:
    print(ex)

