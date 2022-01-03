class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True / False)?: ").lower()
        self.check_answer(user_answer, current_question.answer.lower())
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"You got it right!\nThe correct answer was: {correct_answer}.\nYour current score is: {self.score}/{self.question_number + 1}\n")
        else:
            print(f"You were wrong!\nThe correct answer was: {correct_answer}.\nYour current score is: {self.score}/{self.question_number + 1}\n")

    def final_score(self):
        return f"You finished the quiz. Your final score was {self.score}/{len(self.q_list)}"
