if (5 > 3):
    print("Merhaba")

isLoggedin = False
if (isLoggedin == True):
    print("Merhaba")

isLoggedin = True
if (isLoggedin == True):
    print("Merhaba")



_username = "sadikturan"
_password = "1234"

username = input("İsim: ")
password = input("Şifre: ")

isLoggedin = (_username == username) and (_password == password)

if (isLoggedin):
    print("Uygulamaya Hoş Geldiniz!")
else:
    print("Kullanıcı adı veya şifre hatalı!")



if (_username == username):
    if (_password == password):
        print("Uygulamaya Hoş Geldiniz!")
    else:
        print("Şifre hatalı!")
else: 
    print("Kullanıcı adı hatalı!")

