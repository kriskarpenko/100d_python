class QuizBrain:
    def __init__(self, question_list):
        self.question_index = 0
        self.question_list = question_list
        self.u_score = 0
    
    def still_has_questions(self):
        return self.question_index < len(self.question_list) #will return a boolean
        
    def check_answer(self, u_answer, correct_answer):
        self.u_answer = u_answer
        self.correct_answer = correct_answer
        if u_answer == correct_answer:
            self.u_score += 1
            print(f"Yay")
        else:
            print("Nay")
        print(f"You're score is {self.u_score}/{self.question_index}")
        print("\n")



    def next_question(self):
        current_question =  self.question_list[self.question_index]
        self.question_index += 1
        u_answer = input(f"Q.{self.question_index} {current_question.text} True/False?").capitalize()
        self.check_answer(u_answer, current_question.answer)
