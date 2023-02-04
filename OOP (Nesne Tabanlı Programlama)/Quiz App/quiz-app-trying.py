"""Soruları, şıkları ve cevabı kullanıcıdan aldıktan sonra bu sorular üzerinden bilgi 
yarışması yapmak istedim fakat soruları alırken farklı farklı class oluşturamadım, tek bir class oluşuyor ve 
hata veriyor."""

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
"""
question1 = Question("1) En iyi programlama dili hangisidir?: ", ["Python", "C#", "Java", "Dart"], "Python")
question2 = Question("2) En popüler programlama dili hangisidir?: ", ["Python", "Java", "C#", "Dart"], "Python")
question3 = Question("3) En çok kazandıran programlama dili hangisidir?: ", ["Python", "Java", "Dart", "C#"], "Python")

questions = [question1, question2, question3]
"""

choices = []
questions = []

def create_question():
    devamMı = input("Soru girmek için 'G', çıkmak için 'C'ye basınız: ")

    while (devamMı != "C"):
        textt = input("Soruyu giriniz: ")
        
        for i in range(1, 5):
            choicee = input(f"{i}. şıkkı giriniz: ")
            choices.append(choicee)

        answer = input("Sorunun doğru cevabını belirtiniz: ")
        question = Question(textt, choices, answer)
        questions.append(question)
        devamMı = input("Soru girmek için 'G', çıkmak için 'C'ye basınız: ")

create_question()

for q in questions:
    print(q.text)

    for i in range(0, len(questions) + 1):
        print(f"- {q.choices[i]}")

    userAnswer = input("Cevabınızı giriniz: ")
    print(q.check_answer())
    time.sleep(1.7)
