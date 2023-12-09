MAX_CLASS_SIZE = 11 # not inclusive

class TooManyStudents(Exception):
    pass

class Person:
    
    def __init__(self, name : str) -> None :
        self.name = name
        
        
class Teacher(Person):
    pass

class Student(Person):
    pass

class Classroom:
    
    def __init__(
        self, 
        teacher : Teacher, 
        students : list[Student], 
        course_title : str
    ) -> None :
        
        self.teacher = teacher
        self.students = students
        self.course_title = course_title
        
    def add_student(self, student : Student) -> None :
        
        if len(self.students) < MAX_CLASS_SIZE:
            self.students.append(student)
            return
        
        raise TooManyStudents
    
    def remove_student(self, name : str) -> None :
        for student in self.students:
            if student.name == name :
                self.students.remove(student)
                
    def change_teacher(self, new_teacher : str) -> None :
        self.teacher = new_teacher
        
