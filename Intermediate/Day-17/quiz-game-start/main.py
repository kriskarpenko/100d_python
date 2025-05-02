from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    text = str(i.get('text'))
    answer = str(i.get('answer'))
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("Yuppie! You have completed the quiz")
print(f"You're final score is {quiz_brain.u_score}/{len(question_bank)}")

