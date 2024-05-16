from question_class import Question
File1 = open("questions.txt", "r")
QuestionsF = File1.readlines()
questions = []
for index in range(len(QuestionsF)):
    if index % 6 == 0:
        questions.append(Question(QuestionsF[index]+QuestionsF[index+1]+QuestionsF[index+2]+QuestionsF[index+3]+QuestionsF[index+4], QuestionsF[index+5]))


def run_exam(question_paper):
    score = 0
    for question in question_paper:
        answer = input(question.prompt)
        if answer[0] == question.answer[0]:
            score += 1
    print("you scored "+str(score)+"/"+str(len(QuestionsF)/6))


run_exam(questions)
File1.close()
