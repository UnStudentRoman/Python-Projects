from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
correct_answer = True

for question in question_data:
    new_q = Question(q_text=question["text"], q_answer=question["answer"])
    question_bank.append(new_q)

game = QuizBrain(question_bank)

while game.still_has_questions():
    correct_answer = game.next_question()

print(game.final_score())