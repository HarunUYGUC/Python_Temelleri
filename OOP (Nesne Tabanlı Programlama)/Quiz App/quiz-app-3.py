import time

class Question:
    
    score = 0

    @classmethod
    def display_score(cls):
        return f"Toplam {cls.score} tane soru bildiniz."

    def __init__(self, _text, _choices, _answer):
        self.text = _text
        self.choices = _choices
        self.answer = _answer

    def check_answer(self):
        if (userAnswer not in self.choices):
            return f"{userAnswer} böyle bir cevap {self.choices} şıkları içerisinde yok!"
        elif (userAnswer == self.answer):
            Question.score += 1
            return f"Tebrikler cevabınız doğru, cevap {self.answer}'idi."
        else:
            return f"Üzgünüz cevabınız doğru değil, cevap {self.answer}'idi."

question1 = Question("1) En iyi programlama dili hangisidir?: ", ["Python", "C#", "Java", "Dart"], "Python")
question2 = Question("2) En popüler programlama dili hangisidir?: ", ["Python", "Java", "C#", "Dart"], "Python")
question3 = Question("3) En çok kazandıran programlama dili hangisidir?: ", ["Python", "Java", "Dart", "C#"], "Python")

questions = [question1, question2, question3]

for q in questions:
    print(q.text)

    for i in range(0, len(q.choices)):
        print(f"- {q.choices[i]}")

    userAnswer = input("Cevabınızı giriniz: ")
    print(q.check_answer())
    print(Question.display_score())
    time.sleep(1.7)
