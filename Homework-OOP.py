class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def average_rate_student(self):
        _sum = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                _sum += i
                counter += 1
        if counter != 0:
            return round(_sum/counter,2)    
     
    def __str__(self):
        return(f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {self.average_rate_student()}\n'
        f'Курсы в процессе изучения: {self.courses_in_progress}\n'
        f'Завершенные курсы:{self.finished_courses}')

    def __lt__(self,other):
        if not isinstance(other,Student):
            print("Not a Student")
            return
        return self.average_rate_student() < other.average_rate_student()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate_lecturer(self):
        _sum = 0
        counter = 0
        for value in self.grades.values():
            for i in value:
                _sum += i
                counter += 1
            if counter != 0:
                return round(_sum/counter,2)

        
    def rate_lecturer(self,student,lecturer,course,grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate_lecturer()}'
        return res   

    def __lt__(self,other):
        if not isinstance(other,Lecturer):
            print("Not a Lecturer")
            return
        return self.average_rate_lecturer() < other.average_rate_lecturer()
    
class Reviewer(Mentor):
    def rate_hw(self,student,course,grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def average_students_rating(students_list,course):
    sum_rating = 0
    counter = 0
    for student in students_list:
        for course in student.grades:
            sum_person_rating = student.average_rate_student()
            sum_rating += student.average_rate_student()
            counter += 1
            average_rating = round(sum_rating / counter,2)
    return average_rating

def average_lecturers_rating(lecturers_list,course):
    sum_rating = 0
    counter = 0
    for lecturer in lecturers_list:
        for course in lecturer.grades:
            sum_person_rating = lecturer.average_rate_lecturer()
            sum_rating += lecturer.average_rate_lecturer()
            counter += 1
            average_rating = round(sum_rating / counter,2)
    return average_rating


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python','Git']
best_student.finished_courses += ['Введение в программирование']
worst_student = Student('Nikolay','Arsi','male')
worst_student.courses_in_progress += ['Python','Git']
worst_student.finished_courses += ['Введение в программирование']



cool_reviewer = Reviewer('Revi','Ewer')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some','Buddy')
cool_lecturer.courses_attached += ['Python']

bad_lecturer = Lecturer('Any','Body')
bad_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(worst_student,'Python', 2)
cool_reviewer.rate_hw(worst_student,'Python', 4)
cool_reviewer.rate_hw(worst_student,'Python', 6)

cool_lecturer.rate_lecturer(best_student,cool_lecturer,'Python',7)
cool_lecturer.rate_lecturer(best_student,cool_lecturer,'Python',7)
cool_lecturer.rate_lecturer(best_student,cool_lecturer,'Python',7)

bad_lecturer.rate_lecturer(best_student,bad_lecturer,'Python',5)
bad_lecturer.rate_lecturer(best_student,bad_lecturer,'Python',5)
bad_lecturer.rate_lecturer(best_student,bad_lecturer,'Python',5)

print(cool_reviewer)

print(bad_lecturer)

print(best_student)

print(worst_student < best_student)
print(bad_lecturer > cool_lecturer)

students = [best_student,worst_student]
lecturers = [bad_lecturer,cool_lecturer]

print(average_students_rating(students,'Python'))
print(average_lecturers_rating(lecturers,'Python'))