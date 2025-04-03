class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade

    def get_grades(self):
        return self.students
