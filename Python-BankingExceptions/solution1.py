import random


class Question:
    def __init__(self, question_text, options, correct_answer):
        self._question_text = question_text
        self._options = options
        self._correct_answer = correct_answer

    def get_question_text(self):
        return self._question_text

    def get_options(self):
        return self._options

    def get_correct_answer(self):
        return self._correct_answer

    def set_question_text(self, question_text):
        self._question_text = question_text

    def set_options(self, options):
        self._options = options

    def set_correct_answer(self, correct_answer):
        self._correct_answer = correct_answer

    def validate_answer(self, answer):
        
        return answer == self._correct_answer


class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, options, correct_answer):
        Question.__init__(self, question_text, options, correct_answer)

    def validate_answer(self, answer):
        # Case-insensitive comparison after trimming spaces.
        if answer.strip().lower() == self._correct_answer.strip().lower():
            return True
        else:
            return False


class TrueFalseQuestion(Question):
    def __init__(self, question_text, correct_answer):
        # Automatically set options to ["True", "False"]
        Question.__init__(self, question_text, ["True", "False"], correct_answer)

    def validate_answer(self, answer):
        if answer.strip().lower() == self._correct_answer.strip().lower():
            return True
        else:
            return False


class FillInTheBlankQuestion(Question):
    def __init__(self, question_text, correct_answer):
        # No options needed; use an empty list.
        Question.__init__(self, question_text, [], correct_answer)

    def validate_answer(self, answer):
        if answer.strip().lower() == self._correct_answer.strip().lower():
            return True
        else:
            return False


class Quiz:
    def __init__(self):
        self._questions = []  # Dynamic list to store Question objects

    def add_question(self, question):
        self._questions.append(question)

    def remove_question(self, question):
        if question in self._questions:
            self._questions.remove(question)

    def get_questions(self):
        return self._questions

    def shuffle_questions(self):
        random.shuffle(self._questions)

    def get_total_questions(self):
        return len(self._questions)


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)
        self._student_id = student_id
        self._score = 0

    def simulate_quiz(self, quiz, simulated_answers):
        print("\n--- " + self.get_name() + " is taking the quiz ---")
        questions = quiz.get_questions()
        i = 0
        # Use a while loop with an index (avoid using enumerate)
        while i < len(questions):
            current_question = questions[i]
            simulated_answer = simulated_answers[i]
            if current_question.validate_answer(simulated_answer):
                print("Correct!")
                self._score = self._score + 1
            else:
                print("Incorrect! Correct answer: " + current_question.get_correct_answer())
            i = i + 1
        print("")
        print(self.get_name() + " scored " + str(self._score) + " out of " + str(len(questions)) + ".")

    def get_score(self):
        return self._score


class Leaderboard:
    def __init__(self):
        self._students = []  # List to store Student objects

    def add_student(self, student):
        self._students.append(student)

    def display_leaderboard(self):
        print("\n=== Leaderboard ===")
        i = 0
        while i < len(self._students):
            student = self._students[i]
            print("Student: " + student.get_name() + " | Score: " + str(student.get_score()))
            i = i + 1
