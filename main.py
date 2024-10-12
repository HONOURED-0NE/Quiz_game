
question_data = [
    {"text": "A slug's blood is green.", "answer":"True"},
    {"text": "The loudest animal is the african elephant.", "answer": "False"},
    {"text": "approximately one quarter of the human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of the human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virgina, USA, if you accidentaly hit an animal with your car you are free to take it home to eat.", "answer": " True"},
    {"text": "In London, UK, if you happen to die in the house of parliament, you are free to a state funeral." ,"answer": "False"},
    {"text": "It is a crime to pee in the ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow downstairs but not upstairs.", "answer": "False"},
    {"text": "Google was originally called Backrub.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded more than seven times", "answer": "False"},
    {"text": "A few small ounces of chocolate is enough to kill a small dog", "answer": "True"}
]

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0
    def is_still_running(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True
        # you can also say :
        # return self.question_number < len(self.question_list)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):\n")
        self.check_answer(user_answer, current_question.answer)
       
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Yay, you got it right")
            self.user_score += 1
        else:
            print("Wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.user_score}/{self.question_number}")
        print("\n")
quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.is_still_running():
    quiz.next_question()
if quiz.question_number == len(quiz.question_list):
    print("You've completed the quiz")
    print(f"Your final score is {quiz.user_score}/{quiz.question_number}")