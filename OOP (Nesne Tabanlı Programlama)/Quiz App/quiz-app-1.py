# Her bir soruyu temsil edecek question nesnesi oluşturunuz.

# Question sınıfı
#   - text    => soru
#   - choices => cevap şıkları
#   - answer  => soru

# checkAnswer() metodu ile cevap kontrolü yapınız.

# q1.checkAnswer('cevap') => True
# q1.checkAnswer('cevap') => False

import time

class Question:
    def __init__(self, _text, _choices, _answer):
        self.text = _text
        self.choices = _choices
        self.answer = _answer
        # print(_text, _choices) """Bu bulduğum yöntem yerine diğer bulduğum yöntem daha mantıklı."""

    def check_answer(self):
        if (userAnswer not in self.choices):
            return f"{userAnswer} böyle bir cevap {self.choices} şıkları içerisinde yok!"

        if (userAnswer == self.answer):
            return f"Tebrikler cevabınız doğru, cevap {self.answer}'idi."
        else:
            return f"Üzgünüz cevabınız doğru değil, cevap {self.answer}'idi."

question1 = Question("1) En iyi programlama dili hangisidir?: ", ["Python", "C#", "Java", "Dart"], "Python")
# userAnswer = input("Cevabınızı giriniz: ")
# print(question1.check_answer())
# time.sleep(1.8)

question2 = Question("2) En popüler programlama dili hangisidir?: ", ["Python", "Java", "C#", "Dart"], "Python")
# userAnswer = input("Cevabınızı giriniz: ")
# print(question2.check_answer())
# time.sleep(1.8)

question3 = Question("3) En çok kazandıran programlama dili hangisidir?: ", ["Python", "Java", "Dart", "C#"], "Python")
# userAnswer = input("Cevabınızı giriniz: ")
# print(question3.check_answer())
# time.sleep(1.8)

questions = [question1, question2, question3]

for q in questions:
    print(q.text, q.choices)
    userAnswer = input("Cevabınızı giriniz: ")
    print(q.check_answer())
    time.sleep(1.8)
