import time

class Question:
    
    numberOfQuestions = 0
    numberOfCorrectQuestions = 0

    @classmethod
    def display_score(cls):
        score = 100 // cls.numberOfQuestions * cls.numberOfCorrectQuestions
        return f"{cls.numberOfQuestions} sorudan {cls.numberOfCorrectQuestions} soru bildiniz. Toplam Puanınız: {score}".center(100, "*")

    def __init__(self, _text, _choices, _answer):
        self.text = _text
        self.choices = _choices
        self.answer = _answer

    def check_answer(self):
        if (userAnswer not in self.choices):
            Question.numberOfQuestions += 1 
            return f"{userAnswer} böyle bir cevap {self.choices} şıkları içerisinde yok!"
        elif (userAnswer == self.answer):
            Question.numberOfCorrectQuestions += 1
            Question.numberOfQuestions += 1 
            return f"Tebrikler cevabınız doğru, cevap {self.answer}'idi."
        else:
            Question.numberOfQuestions += 1 
            return f"Üzgünüz cevabınız doğru değil, cevap {self.answer}'idi."

question1 = Question("1) En iyi programlama dili hangisidir?: ", ["Python", "C#", "Java", "Dart"], "Python")
question2 = Question("2) En popüler programlama dili hangisidir?: ", ["Python", "Java", "C#", "Dart"], "Python")
question3 = Question("3) En çok kazandıran programlama dili hangisidir?: ", ["Python", "Java", "Dart", "C#"], "Python")
question4 = Question("4) En sevilen programlama dili hangisidir?: ", ["Python", "Java", "Dart", "C#"], "Python")
question5 = Question("5) En kolay programlama dili hangisidir?", ["Python", "Java", "Dart", "C#"], "Python")

questions = [question1, question2, question3, question4, question5]

for q in questions:
    print(q.text)

    for i in range(0, len(q.choices)):
        print(f"- {q.choices[i]}")

    userAnswer = input("Cevabınızı giriniz: ")
    print(q.check_answer())
    print(Question.display_score())
    time.sleep(1.7)
