import random
class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer=correct_answer
        # self.max_marks = max_marks
        # self.penalty = penalty
        self.userChoice = -1
        self.score = -1
        
    def get_question_text(self):
        return self.question_text
    def get_option(self):
        return self.options
    def get_correct_answer(self):
        return self.correct_answer
    def set_question_text(self,question):
        self.question_text = question
    def set_options(self,option):
       self.option = option

    def set_correct_answer(self,correct):
        self.correct_answer=correct
    

    
    def validate_answer(self,answer):
       return  self.correct_answer.lower()==answer.lower()
class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, options, correct_answer):
        super().__init__(self, question_text, options, correct_answer)

    def validate_answer(self, answer):
        return  self.correct_answer.lower()==answer.lower()
class TrueFalseQuestion(Question):
    def __init__(self, question_text,correct_answer,options=["True", "False"]):
        super().__init__(self, question_text, options, correct_answer)

    def validate_answer(self, answer):
        return  self.correct_answer.lower()==answer.lower()


class FillInTheBlankQuestion(Question):
    def __init__(self, question_text, correct_answer,options=[]):
        super().__init__(self, question_text, options , correct_answer)

    def validate_answer(self, answer):
        return  self.correct_answer.lower()==answer.lower()


class Quiz:
    def __init__(self):
        self._questions = []
        self.total_score = 0

    def parseQuestions(self, data):
        data = data.split("\n")
        for i in data:
            ip = i.split(':')
            q = Question(ip[0], ip[1].split(','), int(ip[2]), int(ip[3]), int(ip[4]))
            self.questions.append(q)
    def add_question(self,question):
        self._questions.append(question)
    def remove_question(self,question):

        for  i in self._questions:
            if i.get_question_text==question:
                self._questions.remove(i)
            

    def get_questions(self):
    
        return self._questions

    def shuffle_Questions(self):
        random.shuffle(self._questions)
    def get_total_questions(self):
        return len(self._questions)

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
class Student:
    def __init__(self,name, age, student_id) -> None:
        super().__init__(self, name, age)
        self.student_id = student_id
        self.score =0

    def simulate_quiz(self,quiz,answers):
        print("")
        print(f"---{Student.get_name(self)} is taking the quiz ---")
        for i in quiz.get_qutions():
            if i.validate_answer(answers[j]):
                print("Correct!")
                self._score = self._score + 1
            else:
                print("Incorrect! Correct answer: " + {i.get_correct_answer()})
                j = j+ 1
        print("")
        print(f"{Student.get_name} scored {self._score} out of {len(answers)}." )

    
    def get_score(self):
        return self.score

class Leaderboard:
    def __init__(self) -> None:
        self.leaderboard=[]
    def add_student(self,student):
        self.leaderboard.append(student)
    def display_leaderboard(self):
        print()
        print("\n=== Leaderboard ===")
        for i in self.leaderboard:
            print(f"student{i.get_name()} | Score: {i.get_score()}")

       

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