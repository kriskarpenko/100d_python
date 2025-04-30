from question_model import Question
from data import question_data

question_bank = []
for i in question_data:
    text = str(i.get('text'))
    answer = str(i.get('answer'))
    new_question = Question(text, answer)
    question_bank.append(new_question)


        