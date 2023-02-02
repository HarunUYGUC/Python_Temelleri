# Comment isminde bir sınıf oluşturunuz.
# Comment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.

class Comment:
    def __init__(self, _username, _text, _likes=0, _dislikes=0):
        self.username = _username
        self.text = _text
        self.likes = _likes
        self.dislikes = _dislikes

c1 = Comment("sadikturan", "güzel kurs")
c2 = Comment("ahmetyilmaz", "çok güzel bir kurs")
c3 = Comment("cinarturan", "idare eder bir kurs", 50, 10)
c4 = Comment("ahmetyilmaz", "kursu beğenmedim")
c5 = Comment("sadikturan", "süper bir kurs olmuş", 100)

comments = [c1, c2, c3, c4, c5]

for c in comments:
    print(f"{c.username}: {c.text}")
    print(f"likes: {c.likes} - dislikes: {c.dislikes}")
