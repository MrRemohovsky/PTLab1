from BaseCalc import BaseCalc
from Types import DataType


class TopStudentsCounter(BaseCalc):

    def __init__(self, students):
        self.students: DataType = students

    def calc(self) -> int:
        count = 0
        for student, grades in self.students.items():
            if all(score >= 90 for subj, score in grades):
                count += 1
        return count