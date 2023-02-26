class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.questions_list = list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (T/F)? ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, current_q_answer):
        if user_answer == current_q_answer:
            print("You got it right!")
            self.score += 1
        else:
            print(f"You got it wrong!")

        if current_q_answer == "t":
            print(f"The correct answer is True")
        else:
            print(f"The correct answer is False")
        print(f"Your current score: {self.score}\n")