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
       
        if self.userChoice == self.correctOption:
            return self.max_marks
        else:
            return self.penalty 
    


class Quiz:
    def __init__(self):
        self.questions = []
        self.total_score = 0

    def parseQuestions(self, data):
        data = data.split("\n")
        for i in data:
            ip = i.split(':')
            q = Question(ip[0], ip[1].split(','), int(ip[2]), int(ip[3]), int(ip[4]))
            self.questions.append(q)
    



    def startQuiz(self, l):
        i = 0
        for j in self.questions:
            j.userChoice = l[i]
            i += 1
            j.score = j.evaluateAnswer()
            
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