import random
# change python3 to python if use windows in eval.sh of line 15 
# =========================
# Part 1: Quiz and Question Classes
# =========================

class Question:
    # Todo
    pass


class MultipleChoiceQuestion(Question):
    # Todo
    pass


class TrueFalseQuestion(Question):
    # Todo
    pass


class FillInTheBlankQuestion(Question):
    # Todo
    pass


class Quiz:
    # Todo write the remaining methods

    def shuffle_questions(self) -> None:
        random.shuffle(self._questions)


# =========================
# Part 2: Person, Student, and Leaderboard Classes
# =========================

class Person:
    # Todo
    pass


class Student(Person):
    # Todo
    pass


class Leaderboard:
    # Todo
    pass
