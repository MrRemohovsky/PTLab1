import pytest
from src.TopStudentsCounter import TopStudentsCounter
from Types import DataType


class TestTopStudentsCounter:

    @pytest.fixture()
    def students_all_fail(self) -> DataType:
        return {
            "Иванов Иван Иванович": [("математика", 22), ("география", 33)],
            "Петров Петр Петрович": [("математика", 11), ("химия", 4)],
            "Сидоров Сидор Сидорович": [("математика", 87), ("литература", 90)]
        }

    @pytest.fixture()
    def students_all_pass(self) -> DataType:
        return {
            "Иванов Иван": [("математика", 95), ("география", 99)],
            "Петров Петр": [("математика", 90), ("химия", 92)],
        }

    @pytest.fixture()
    def students_borderline_scores(self) -> DataType:
        return {
            "Иванов Иван": [("математика", 89), ("география", 90)],
            "Петров Петр": [("математика", 91), ("химия", 90)],
        }

    def test_no_students(self):
        counter = TopStudentsCounter({})
        assert counter.calc() == 0

    def test_all_fail(self, students_all_fail: DataType):
        counter = TopStudentsCounter(students_all_fail)
        assert counter.calc() == 0

    def test_all_pass(self, students_all_pass):
        counter = TopStudentsCounter(students_all_pass)
        assert counter.calc() == 2

    def test_borderline_scores(self, students_borderline_scores):
        counter = TopStudentsCounter(students_borderline_scores)
        assert counter.calc() == 1
