try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)
except ZeroDivisionError:
    print("y, 0 (sıfır) olamaz!")
except ValueError:
    print("x ve y, sayısal bir değer olmalıdır!")
except:
    print("Bilinmeyen bir hata oluştu!")



try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)
except (ZeroDivisionError, ValueError) as e:
    print("Hata oluştu!")
    print(e)
except Exception as e:
    print("Bilinmeyen bir hata oluştu!")
    print(e)


while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)
    except (ZeroDivisionError, ValueError) as e:
        print("Hata oluştu!")
        print(e)
    except Exception as e:
        print("Bilinmeyen bir hata oluştu!")
        print(e)
    else:
        break
    finally:
        print("Finally bloğu çalıştı!")

