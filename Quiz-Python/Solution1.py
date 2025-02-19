class Question:
    def __init__(self, question_text, choices, correctOption, max_marks, penalty):
        self.question_text = question_text
        self.choices = choices
        self.correctOption = correctOption
        self.max_marks = max_marks
        self.penalty = penalty
        self.userChoice = -1
        self.score = -1
        
    
    def evaluateAnswer(self):
        # print(self.userChoice)
        if self.userChoice == self.correctOption:
            # print(self.max_marks)
            return self.max_marks
        else:
            return self.penalty 
    


class Quiz:
    def __init__(self):
        self.questions = []
        self.total_score = 0
    
# "Who is the current Chief Minister of Telangana?:KCR,Chandra Babu Naidu,President’s Rule,Jagan:1:3:-1\n"
    def parseQuestions(self, data):
        data = data.split("\n")
        for i in data:
            a = i.split(':')
            q = Question(a[0], a[1].split(','), int(a[2]), int(a[3]), int(a[4]))
            self.questions.append(q)
    

    def startQuiz(self, l):
        i = 0
        for j in self.questions:
            j.userChoice = l[i]
            i += 1
            j.score = j.evaluateAnswer()
            # print(j.score)
            self.total_score += j.score


    def scoreReport(self):
        print()
        print('Score Report:')
        for i in self.questions:
            print(f"Question: {i.question_text}")
            c = ", ".join(i.choices)
            print(f"Choices: {c}")
            print(f"Your Answer: {i.userChoice} | Correct Answer: {i.correctOption}")

            if i.userChoice == i.correctOption:
                print(f"Correct Answer! Marks Awarded: {i.max_marks}")
            else:
                print(f"Wrong Answer! Penalty Applied: {i.penalty}")
            print()
        print(f"Total Score: {self.total_score}")