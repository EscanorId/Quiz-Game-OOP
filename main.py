from question_model import Question
from data import  question_data
from quiz_brain import QuizBrain
import time

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz = QuizBrain(question_bank)


# Start program
while quiz.still_has_question():
    quiz.next_question()
