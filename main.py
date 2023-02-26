import data, quiz_brain
import question_model



question_bank = []

for q in data.question_data['results']:
    question_bank.append(question_model.Question(q['question'], q['correct_answer']))

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score is {quiz.score}/{len(quiz.questions_list)}")