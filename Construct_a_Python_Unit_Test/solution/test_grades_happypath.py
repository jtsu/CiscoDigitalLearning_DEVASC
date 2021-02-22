import pytest


@pytest.fixture
def student():
    from student import Student

    stud = Student('Luka Zauber')
    yield stud
    del stud


@pytest.fixture
def subject():
    from subject import Subject

    s = Subject('Unit Testing 101')
    yield s
    del s


@pytest.mark.usefixtures('student', 'subject')
class TestHappyPath:
    def test_add_subject_to_student(self, student, subject):
        assert student.add_subject(subject) is True

    def test_add_grade_to_subject(self, student, subject):
        student.add_subject(subject)
        assert student.set_grade(subject, 8) is True

    def test_get_subject_grade(self, student, subject):
        student.add_subject(subject)
        student.set_grade(subject, 8)
        student.set_grade(subject, 9)
        assert student.get_grades_for_subject(subject) == [8, 9]
        
